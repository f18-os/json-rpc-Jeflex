# minimalistic server example from
# https://github.com/seprich/py-bson-rpc/blob/master/README.md#quickstart

import socket
from bsonrpc import JSONRpc
from bsonrpc import request, service_class
from bsonrpc.exceptions import FramingError
from bsonrpc.framing import (
	JSONFramingNetstring, JSONFramingNone, JSONFramingRFC7464)
import node
from node import increment
import json
from node import recursiveBuilder

# Class providing functions for the client to use:
@service_class
class ServerServices(object):

  @request
  def incr(self, graph):
    f = open("request.json", "x")
    f.write(graph)
	#load json into an array
    graph = json.loads(graph)
	#make node object from json
    root = recursiveBuilder(graph)
    increment(root)
    #make back to json
    JsonNode = json.dumps(root, default=lambda o: o.__dict__)
    return JsonNode

# Quick-and-dirty TCP Server:
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(('localhost', 50001))
ss.listen(10)

while True:
  s, _ = ss.accept()
  # JSONRpc object spawns internal thread to serve the connection.
  JSONRpc(s, ServerServices(),framing_cls=JSONFramingNone)
