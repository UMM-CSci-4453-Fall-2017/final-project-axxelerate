from flask import Flask, request, Response, abort
from flask_cors import cross_origin
import json
import example_data
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/results")
@cross_origin({"origins": "http://localhost:*"})
def getResults():
    queryString = request.args.get("query")
    f = request.args.get("from")
    if (queryString == None):
        return "Bad stuff!"

    #if (queryString == None) :
    #     page = 1
    # else:
    #     # TODO: actually parse the string to an int
    #     page = page

    # TODO: At some point we need to break down the query into keywords

    if (queryString == "result0"):
        result = example_data.result0
    elif (queryString == 'result1' and f != "2"):
        result = example_data.result1_1
    elif (queryString == 'result1' and f == "2"):
        result = example_data.result1_2
    else:
        result = {
            "results" : []
        }

    return Response(json.dumps(result), mimetype="application/json")
