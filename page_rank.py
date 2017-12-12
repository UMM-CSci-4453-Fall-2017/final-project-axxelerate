#! /usr/bin/env python

import time

damping = 0.85

def main():

    # assume we have a list of nodes and weights
    nodes_and_ranks = {
        "Home" : 1,
        "About" : 1,
        "Product" : 1,
        "More" : 1
    }

    # assume we have the linking table
    links = {
        "Home" : ["About", "Product", "More"],
        "About" : ["Home"],
        "Product" : ["Home"],
        "More" : ["Home"]
    }

    for i in range(1,40):
        export_strengths = {n: export_strength(nodes_and_ranks, links, n) for n in links}
        new_ranks = {n: compute_new_pr(export_strengths, links, n) for n in links}
        differences = []
        for node in new_ranks:
            diff =  abs(new_ranks[node] - nodes_and_ranks[node])
            differences.append(diff)
        print(differences)
        print(new_ranks)
        avg_diff = sum(differences)/len(differences)
        print avg_diff
        print
        nodes_and_ranks = new_ranks


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

