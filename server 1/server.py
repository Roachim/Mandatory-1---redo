#Receive XML, send Json - Receive and send CSV

from bottle import run, post, request
import requests
import json
from lxml import etree
import csv
#import xml.etree.ElementTree as ET
#from xml.etree import ElementTree
import xmltodict, json

# def to_bytes(s):
#         if type(s) is bytes:
#             return s
#         elif type(s) is str or (sys.version_info[0] < 3 and type(s) is unicode):
#             return codecs.encode(s, 'utf-8')
#         else:
#             raise TypeError("Expected bytes or string, but got %s." % type(s))

@post("/server1")
def do():
    parser = etree.XMLParser(encoding='UTF-8')
    
    #xml = to_bytes(request.body)
    #variable = request.body.read()
    #tree = ElementTree.parse(request.body)
    tree = etree.fromstring(request.body.read(), parser=parser) 
    #.encode('utf-16-be') ---AttributeError: '_io.BytesIO' object has no attribute 'encode'
    
    
    

    for number in tree.iter('Number'):
        new_number = int(number.text) + 10
        number.text = str(new_number)

    jsonr = xmltodict.parse(etree.tostring(tree))
    jsonr = json.dumps(jsonr)

    response = requests.post("http://127.0.0.1:3333/server2", 
        headers={"Content-Type": "application/json"}, data=jsonr
    )


    #return etree.tostring(tree)
    return str(response.text)


run(host="127.0.0.1" , port=2222 , debug=True , reloader=True )