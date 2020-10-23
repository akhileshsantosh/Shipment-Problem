"""
Node Factory class to track all the nodes in the graph
"""


class NodeFactory(object):
    # to store node name to Node object
    name_to_node = dict()
    # to map the node id to node name
    node_id_to_name = dict()
    # a static counter to assign the node id to a node.
    counter = 0

    # creates a node if it doesnt exist else returns the existing node.
    @staticmethod
    def get_node(name):
        if NodeFactory.name_to_node.get(name) is None:
            NodeFactory.name_to_node[name] = Node(name, NodeFactory.counter)
            NodeFactory.node_id_to_name[NodeFactory.counter] = name
            NodeFactory.counter = NodeFactory.counter + 1
        return NodeFactory.name_to_node.get(name)

    # returns node if found else none
    @staticmethod
    def find_node(name):
        return NodeFactory.name_to_node.get(name)

    # returns the name of the node based on the unique id assigned during creation
    @staticmethod
    def get_node_name(node_id):
        return NodeFactory.node_id_to_name.get(node_id)

    # checks if the node exists in the graph based on its name.
    @staticmethod
    def exists(name):
        return False if NodeFactory.name_to_node.get(name) is None else True


class Node(object):
    def __init__(self, name, node_id):
        self.name = name
        self.id = node_id


"""
An Edge class to represent a directed edge between two nodes with a certain cost.
"""


class Edge(object):

    def __init__(self, source, destination, distance):
        self.source_node = NodeFactory.get_node(source)
        self.destination_node = NodeFactory.get_node(destination)
        self.distance = distance


"""
Node class to track the nodes to visit while running Dijkstra's
"""


class VisitedNode(object):
    def __init__(self, name, distance):
        self.node = NodeFactory.find_node(name)
        self.distance = distance





