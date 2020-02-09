from chatbot.markovchatbot.mmodel.connection import Connection


class Node:
    def __init__(self, word: str):
        self.word = word
        self.connections = []

    def __str__(self):
        if (self.word == None):
            return "Root Node with " + str(len(self.connections)) + " connections."
        return "Node: '" + self.word + "' with " + str(len(self.connections)) + " connections."

    def add_connection(self, source_node, destination_node, weight):
        self.connections.append(Connection(source_node, destination_node, weight))

    def boost_or_add_connection(self, destination_node, weight=1):
        connected_node = self.get_connected_node(destination_node)

        if connected_node:
            # print("boost connection:")
            # print(connected_node)
            # print()
            connected_node.boost_connection(connected_node, weight)
        else:
            # print()
            # print("new connection:")
            # print(self)
            # print("dest: " + str(destination_node))
            self.connections.append(Connection(self, destination_node, weight))
            # print("length " + str(len(self.connections)))
            # print(self)
            # print()

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

    def get_strongest_connection_word(self) -> Connection:
        return max(self.connections).word