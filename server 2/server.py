#Receieve Json, Send CSV
from bottle import run, post, request

import json
import csv


@post("/server2")
def do():
    print(str(request))
    dataFromServer1 = json.load(request.body)
    print("############")
    print(dataFromServer1)

    responseNumber = str(float(str(dataFromServer1.get("XData").get("Number"))) * 3)

    print("#####################")
    print(responseNumber)

    responseString = "Number\n"

    responseString+= str(responseNumber)

    return responseString



run(host="127.0.0.1" , port=3333 , debug=True , reloader=True )