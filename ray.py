from collections import deque

class Node:
    def __init__(self, node_id, has_token, holder):
        self.id = node_id
        self.has_token = has_token
        self.holder = holder
        self.request_queue = deque()
        self.network = {}

    def set_network(self, network):
        self.network = network

    def request_token(self):
        print(f"Node {self.id} requests the token.")

        if self.has_token:
            self.enter_critical_section()
            return

        self.request_queue.append(self.id)

        if len(self.request_queue) == 1 and self.holder != self.id:
            self.send_request_to_holder()

    def send_request_to_holder(self):
        print(f"Node {self.id} forwards request to Node {self.holder}")
        holder_node = self.network[self.holder]
        holder_node.receive_token_from(self.id)

    def receive_token_from(self, requester_id):
        self.has_token = True
        self.holder = self.id
        print(f"Node {self.id} received the token!")

        if self.request_queue:
            next_id = self.request_queue.popleft()
            if next_id == self.id:
                self.enter_critical_section()
            else:
                self.send_token(next_id)
        else:
            if requester_id != self.id:
                self.send_token(requester_id)

    def send_token(self, next_holder):
        self.has_token = False
        self.holder = next_holder
        print(f"Node {self.id} sends token to Node {next_holder}")
        next_node = self.network[next_holder]
        next_node.receive_token_from(self.id)

    def enter_critical_section(self):
        print(f"Node {self.id} enters the Critical Section!")
        self.has_token = False

        if self.request_queue:
            next_id = self.request_queue.popleft()
            self.send_token(next_id)


def main():
    network = {}

    n = int(input("Enter number of nodes: "))
    root_id = -1

    for i in range(n):
        parent = int(input(f"Enter parent (holder) for node {i} (-1 if root): "))
        has_token = (parent == -1)
        if has_token:
            root_id = i
        node = Node(i, has_token, i if has_token else parent)
        network[i] = node

    # Set network reference in each node
    for node in network.values():
        node.set_network(network)

    r = int(input("Enter number of token requests: "))

    for i in range(r):
        requester_id = int(input(f"Enter node ID making request {i + 1}: "))
        if requester_id in network:
            network[requester_id].request_token()
        else:
            print("Invalid node ID.")

if __name__ == "__main__":
    main()
