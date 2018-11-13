import json
class node:
    def __init__(self, name, children = []):
        self.name = name
        self.children = children
        self.val = 0
    def show(self, level=0):
        print("%s%s val=%d:" % (level*"  ", self.name, self.val))
        for c in self.children:
            c.show(level + 1)

def increment(graph):
    graph.val += 1;
    for c in graph.children:
        increment(c)

def recursiveBuilder(root):
    if not root['children']:
        leaf = node(root['name'])
        leaf.val = root['val']
        return leaf
    else:
        branch = []
        for c in root['children']:
            branch.append(recursiveBuilder(c))
        leaf = node(root['name'], branch)
        leaf.val = root['val']
        return leaf
