#! /usr/bin/env python

import sys
import pymysql.cursors
import credentials
import pprint

damping = 0.85

def main():

    pp = pprint.PrettyPrinter(indent=4)

    connection = pymysql.connect(host = credentials.host,
                                 user = credentials.user,
                                 password = credentials.password,
                                 db = credentials.db,
                                 cursorclass = pymysql.cursors.DictCursor)

    nodes_and_ranks = None
    links = None


    with connection.cursor() as cursor:

        sql_hash_list = "SELECT `fromHash`, `toHash` FROM `linksTo`"
        sql_page_list = "SELECT `urlHash` FROM `pages`"

        cursor.execute(sql_page_list)
        original_from_db = cursor.fetchall()
        print("fetched first chunk")

        links = { row['urlHash'] : [] for row in original_from_db}

        cursor.execute(sql_hash_list)
        all_hashes = cursor.fetchall()

        for row in all_hashes:
            src = row['fromHash']
            dst = row['toHash']
            links[src].append(dst)

        print("fetched last chunk")

        nodes_and_ranks = {h: 0.15 for h in links}

        iteration = 0
        avg_diff = float("inf")

        while avg_diff > 0.00001:
            export_strengths = {n: export_strength(nodes_and_ranks, links, n) for n in links}
            new_ranks = {n: compute_new_pr(export_strengths, links, n) for n in links}
            differences = []
            for node in new_ranks:
                diff =  abs(new_ranks[node] - nodes_and_ranks[node])
                differences.append(diff)
            avg_diff = sum(differences)/float(len(differences))
            nodes_and_ranks = new_ranks
            print("%s %s" % (iteration, avg_diff))
            iteration += 1

        print("start writing data")
        sql_update_result = "UPDATE `pages` SET `pagerank` = %s WHERE `urlHash` = %s"
        for h,rank in nodes_and_ranks.iteritems():
            cursor.execute(sql_update_result, (rank,h))
        print("done writing data")

    connection.commit()


def export_strength(prev_ranks, links, node):
    num_out = len(links[node])
    if num_out == 0:
        return 0
    else:
        return prev_ranks[node] / num_out

def compute_new_pr(export_strengths, links, node):
    contributions = 0
    for n in links:
        if node in links[n]:
            contributions += export_strengths[n]
    new_pr = (1 - damping) + (damping * contributions)
    return new_pr

if __name__ == "__main__":
    main()

