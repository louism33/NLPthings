from chatbot.markovchatbot.mmodel.node import Node


class MarkovModel:
    def __init__(self):
        self.startNode = Node(None)
        self.endNode = Node(None)  # todo
        # optimisation, store a hash of the nodes / alphabetical
        self.nodes = [self.startNode, self.endNode]

    def __len__(self):
        return len(self.nodes) - 2

    def get_start_node(self) -> Node:
        return self.startNode

    def get_end_node(self) -> Node:
        return self.endNode

    def find_node_by_name(self, name) -> Node:
        name = name.lower()
        for node in self.nodes:
            if node.word == name:
                return node
        return None

    def get_node_or_new(self, name):
        name = name.lower()
        for node in self.nodes:
            if node.word == name:
                return node
        return Node(name)

    def add_node_if_not_present(self, name):
        name = name.lower()
        for node in self.nodes:
            if node.word == name:
                # print("exists")
                return
        self.nodes.append(Node(name))

    def connect(self, old_node, new_node):
        if old_node is None:
            self.startNode.boost_or_add_connection(self.get_node_or_new(new_node))
        else:
            self.get_node_or_new(old_node).boost_or_add_connection(self.get_node_or_new(new_node))
