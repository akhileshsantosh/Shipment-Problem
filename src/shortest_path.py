from util_functions import Utilities, Constants
from data_classes import NodeFactory, Node, Edge, VisitedNode
from priority_queue import MinPriorityQueue


# This class implements the core logic of finding shortest path between
# source and destination and time taken to traverse it based on average speed.
# Shortest path algorithm implemented is based on Dijkstra's single source shortest path
# Naive method has time complexity of O(V^2), this class implements the priority
# queue to store the shortest distance edges using minimum priority queue, implemented
# using binary heap which makes the overall algorithm faster with the time complexity of
# O(E log V) , Where V is number of nodes and E is number of edges in graph.
class ShortestPathCalculator(object):

    # constructor, initializing vertices, edges
    def __init__(self):
        self.source = None
        self.destination = None
        self.shortest_distance = Constants.MAX_INFINITY.value
        self.speed = Constants.DEFAULT_SPEED.value
        self.adjacency_list = dict()
        self.bi_directional_edge = True
        self.distance_vector = []
        self.previous_nodes = []
        self.visited_vertices = []
        self.__initialize()

    # calculates shortest path and time taken to cover the distance
    # input is source, destination , average speed and a flag to indicate
    # whether the edges should be considered bidirectional or not
    # by default the speed is 40KM/HR and edges are uni directional.
    # returns infinity as distance if path is not found.
    def run(self):
        # If the necessary inputs are not present return path as infinity, equivalent to path not found.
        if self.__pre_check():
            # initializes the helping objects for calculating the shortest path.
            self.__init_objects()

            # For source node the distance to itself is 0
            source_node_id = NodeFactory.get_node(self.source).id
            self.distance_vector[source_node_id] = 0

            # initialize the priority queue by adding the source node.
            priority_queue = MinPriorityQueue()
            priority_queue.add(self.source, 0)

            # If all the nodes are visited the priority queue will be empty and we can exit.
            while not priority_queue.empty():
                # pop the element with minimum distance from min priority queue
                node_in_queue = priority_queue.remove()
                visited_node = VisitedNode(node_in_queue[0], node_in_queue[1])

                # Mark this node as visited.
                self.visited_vertices[visited_node.node.id] = True

                # if the distance of visited node is more than the current distance then no need to visit this node.
                if self.distance_vector[visited_node.node.id] < visited_node.distance:
                    continue

                # Get all the outgoing paths from this node.
                current_edges = self.adjacency_list.get(visited_node.node.name)
                if current_edges is not None:
                    for this_edge in current_edges:
                        if self.visited_vertices[this_edge.destination_node.id]:
                            continue
                        new_distance = self.distance_vector[this_edge.source_node.id] + this_edge.distance

                        # If the new distance is lower than the current distance then add the node with new priority
                        # update the distance vector and the node from which we reach this node.
                        if new_distance < self.distance_vector[this_edge.destination_node.id]:
                            self.previous_nodes[this_edge.destination_node.id] = this_edge.source_node.id
                            self.distance_vector[this_edge.destination_node.id] = new_distance
                            priority_queue.add(this_edge.destination_node.name, new_distance)

                # if we have reached the destination node , we can exit from here as
                # we are not interested in other nodes.
                # This is one small optimisation if we are interested in
                # single source and single destination path.
                if node_in_queue[0] == self.destination:
                    self.shortest_distance = self.distance_vector[NodeFactory.get_node(self.destination).id]
                    break
        # return the distance, path and time taken
        return self.shortest_distance, self.__get_shortest_path(), self.__time_taken()

    # Traverse the intermediate nodes visited and form the path.
    def __get_shortest_path(self):
        # if the destination node is not found
        if NodeFactory.find_node(self.destination) is None \
                or NodeFactory.find_node(self.source) is None:
            return None
        shortest_path = []
        node_id = NodeFactory.find_node(self.destination).id

        while node_id is not None:
            shortest_path.append(NodeFactory.get_node_name(node_id))
            node_id = self.previous_nodes[node_id]
        shortest_path.reverse()
        formatted_path = Constants.EMPTY_STRING.value
        for element in shortest_path:
            formatted_path = element if formatted_path == Constants.EMPTY_STRING.value\
                else formatted_path + Constants.PATH_SEPARATOR.value + element
        return formatted_path

    # Time taken to cover DC to warehouse in minutes
    def __time_taken(self):
        time_in_minutes = Constants.MINUTES_IN_HOUR.value * self.shortest_distance / self.speed \
            if self.shortest_distance is not Constants.MAX_INFINITY.value else None
        return time_in_minutes

    # Does the pre check about put parameters before calculating shortest path
    def __pre_check(self):

        # set the path to calculate as infinity
        self.shortest_distance = Constants.MAX_INFINITY.value

        # check if the source node and destination node exist in graph.
        if not NodeFactory.exists(self.source):
            Utilities.log(f"Node '{self.source}' is not present")
            return False
        elif not NodeFactory.exists(self.destination):
            Utilities.log(f"Node '{self.destination}' is not present")
            return False
        return True

    # initializes the helping objects for calculating the shortest path.
    def __init_objects(self):
        # initialize the distance vector for each vertices
        self.distance_vector = list(map(lambda element: Constants.MAX_INFINITY.value, NodeFactory.name_to_node))
        self.previous_nodes = list(map(lambda element: None, NodeFactory.name_to_node))
        self.visited_vertices = list(map(lambda element: False, NodeFactory.name_to_node))
        self.shortest_distance = Constants.MAX_INFINITY.value

    # It's a private method which reads the locations and distance from inputPS3 file.
    def __initialize(self):
        lines = Utilities.read_file(Constants.INPUT_FILE.value)
        for line in lines:
            line = line.strip()
            if line is not Constants.EMPTY_STRING.value:
                if Constants.DC_NODE.value in line or Constants.WH_NODE.value in line:
                    # this is input for DC and WH nodes
                    self.__add_source_and_destination(line)
                else:
                    # This is edge input for the graph.
                    self.__add_location(line)

    # reads the source and destination node from input file.
    def __add_source_and_destination(self, line):
        node_tokens = line.split(Constants.NODE_INPUT_TOKEN.value)
        if Constants.DC_NODE.value in line and len(node_tokens) is Constants.NODE_INFO_TOKEN_LENGTH.value:
            self.source = node_tokens[1].strip()
        elif Constants.WH_NODE.value in line and len(node_tokens) is Constants.NODE_INFO_TOKEN_LENGTH.value:
            self.destination = node_tokens[1].strip()

    # This is a private method which tokenize each location to extract
    # source, destination and distance between them.
    # it stores each location as edges and each source / destination as vertices
    def __add_location(self, line):
        if line is not None:
            locationRecord = self.get_location_record(line)
            if locationRecord is not None:
                self.__add_edge(locationRecord)
            else:
                Utilities.log(f'Invalid input found:{line.strip()}')
        else:
            Utilities.log(f'Invalid input found:{line.strip()}')

    # This is a private method which adds the bi directional edge
    def __add_edge(self, locationRecord):
        this_location_1 = Edge(locationRecord[Constants.SOURCE_NODE_INDEX.value],
                               locationRecord[Constants.DESTINATION_NODE_INDEX.value],
                               locationRecord[2])

        # Add the edge between source and destination
        if self.adjacency_list.get(locationRecord[Constants.SOURCE_NODE_INDEX.value]) is None:
            self.adjacency_list[locationRecord[Constants.SOURCE_NODE_INDEX.value]] = []
        self.adjacency_list.get(locationRecord[Constants.SOURCE_NODE_INDEX.value]).append(this_location_1)

        this_location_2 = Edge(locationRecord[Constants.DESTINATION_NODE_INDEX.value],
                               locationRecord[Constants.SOURCE_NODE_INDEX.value],
                               locationRecord[2])

        # Add the edge between destination and source
        if self.adjacency_list.get(locationRecord[Constants.DESTINATION_NODE_INDEX.value]) is None:
            self.adjacency_list[locationRecord[Constants.DESTINATION_NODE_INDEX.value]] = []
        self.adjacency_list.get(locationRecord[Constants.DESTINATION_NODE_INDEX.value]).append(this_location_2)

    @staticmethod
    def get_location_record(line):
        tokens = line.split(Constants.INPUT_SEPARATOR.value)
        locationRecord = None
        if len(tokens) != Constants.ADJACENCY_INFO_TOKEN_LENGTH.value:
            Utilities.log(f"invalid input in file: '{line.strip()}' , expected format is "
                          f"'<location 1> / <location 2> / <distance in km>'")
        else:
            try:
                locationRecord = tuple((tokens[0].strip(), tokens[1].strip(), float(tokens[2].strip())))
            except ValueError:
                Utilities.log(f"Invalid input value '{tokens[1]}' for distance, "
                              f"expected input type is a numeric for distance , "
                              f"original input: '{line.strip()}'")
        return locationRecord

