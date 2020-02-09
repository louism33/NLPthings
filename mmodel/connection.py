class Connection:
    def __init__(self, source_node, destination_node, weight=1):
        self.source_node = source_node
        self.destination_node = destination_node
        self.weight = weight

    def __gt__(self, other):
        if not isinstance(other, Connection):
            return False
        return self.weight > other.weight

    def boost(self, weight_boost=1):
        self.weight += weight_boost

    def get_source_connection(self):
        return self.source_node

    def get_destination_connection(self):
        return self.destination_node