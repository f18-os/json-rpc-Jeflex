from node import *
import json

leaf1 = node("leaf1")
leaf2 = node("leaf2")

root = node("root", [leaf1, leaf1, leaf2])

print("graph before increment")
root.show()

JsonNode = json.dumps(root, default=lambda o: o.__dict__)
# print(JsonNode)

# do this increment remotely:
# increment(root)
node = json.loads(JsonNode)
# print(node)
# print('zoz')
# print(node['children'])

newNode = recursiveBuilder(node)
increment(newNode)

print("graph after increment")
newNode.show()
