from flask import Flask, request, Response, abort
from flask_cors import cross_origin
import json
import example_data
import pymysql
import credentials
app = Flask(__name__)

connection = pymysql.connect(host = credentials.host,
                             user = credentials.user,
                             password = credentials.password,
                             db = credentials.db,
                             cursorclass=pymysql.cursors.DictCursor)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/results")
@cross_origin({"origins": "http://localhost:*"})
def getResults():
    queryString = request.args.get("query")
    page = request.args.get("page")
    if (queryString == None):
        return "Bad stuff!"

    #if (queryString == None) :
    #     page = 1
    # else:
    #     # TODO: actually parse the string to an int
    #     page = page

    # TODO: At some point we need to break down the query into keywords
    #       For now, we'll assume that it is a single keyword

    # if (queryString == "result0"):
    #     result = example_data.result0
    # elif (queryString == 'result1' and page != "2"):
    #     result = example_data.result1_1
    # elif (queryString == 'result1' and page == "2"):
    #     result = example_data.result1_2
    # else:
    #     result = {
    #         "results" : []
    #     }

    result = None

    with connection.cursor() as cursor:
        sql_request = "SELECT url, title FROM keywords LEFT JOIN pages ON pageID = ID WHERE word = %s";
        cursor.execute(sql_request, queryString)
        raw_results = cursor.fetchall()

        result = {
            "nextPage" : "",
            "prevPage" : "",
            "results" : []
        }

        for page in raw_results:
            p = {
                "snippet" : "",
                "link" : page["url"].decode("latin1"),
                "title" : page["title"].decode("latin1")
            }
            result["results"].append(p)

    return Response(json.dumps(result), mimetype="application/json")
