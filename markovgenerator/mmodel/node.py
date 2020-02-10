from chatbot.markovgenerator.mmodel.connection import Connection
from numpy.random import choice


class Node:
    def __init__(self, word: str):
        self.word = word
        self.connections = []

    def __str__(self):
        if (self.word == None):
            return "Root Node with " + str(len(self.connections)) + " connections."
        return "Node: '" + self.word + "' with " + str(len(self.connections)) + " connections."

    def __repr__(self):
        return self.__str__()

    def add_connection(self, source_node, destination_node, weight):
        self.connections.append(Connection(source_node, destination_node, weight))

    def boost_or_add_connection(self, destination_node, weight=1):
        connected_node = self.get_connected_node(destination_node)

        if connected_node:
            self.boost_connection(connected_node, weight)
        else:
            self.connections.append(Connection(self, destination_node, weight))

    def boost_connection(self, destination_node, weight_boost=1):
        for conn in self.connections:
            if conn.destination_node == destination_node:
                conn.boost(weight_boost)
                return

        raise Exception("Tried to boost connnection, but could not find connection")

    def get_connected_node(self, target_node):
        for conn in self.connections:
            if conn.destination_node == target_node:
                return target_node
        return None

    def get_strongest_connection(self) -> Connection:
        if not self.connections:
            return None
        return max(self.connections)

    def get_connection_next_connection_weighted(self) -> Connection:
        if not self.connections:
            return None

        if len(self.connections) == 1:
            return self.connections[0]

        weights = [connection.weight for connection in self.connections]
        total = sum(weights)
        weights[:] = [x / total for x in weights]

        values = choice(self.connections, p=weights)

        return values

    def get_strongest_connection_word(self) -> Connection:
        return max(self.connections).word
