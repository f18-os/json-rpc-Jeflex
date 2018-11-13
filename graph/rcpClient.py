# minimalistic client example from
# https://github.com/seprich/py-bson-rpc/blob/master/README.md#quickstart

import socket
from bsonrpc import JSONRpc
from bsonrpc.exceptions import FramingError
from bsonrpc.framing import (
	JSONFramingNetstring, JSONFramingNone, JSONFramingRFC7464)
from node import *
import json
# Cut-the-corners TCP Client:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 50001))

rpc = JSONRpc(s,framing_cls=JSONFramingNone)
server = rpc.get_peer_proxy()
# Execute in server:
# result = server.swapper('Hello World!')
# "!dlroW olleH"
# print(result)

# print(server.nop({1:[2,3]}))

# From localDemo
leaf1 = node("leaf1")
leaf2 = node("leaf2")

root = node("root", [leaf1, leaf1, leaf2])

print("graph before increment")
root.show()


# Convert python object to json
JsonNode = json.dumps(root, default=lambda o: o.__dict__)
# do this increment remotely:

newGraph = server.incr(JsonNode)
newGraph = json.loads(newGraph)
newNode = recursiveBuilder(newGraph)


print("graph after increment")
newNode.show()

rpc.close() # Closes the socket 's' also
