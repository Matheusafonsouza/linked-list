from __future__ import annotations


class Node:
    def __init__(self, data: str) -> None:
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return self.data


class List:
    def __init__(self) -> None:
        self.head = None

    def __repr__(self) -> str:
        node: Node = self.head
        nodes = list()

        while node is not None:
            nodes.append(node.data)
            node = node.next

        nodes.append("None")
        return " -> ".join(nodes)


if __name__ == "__main__":
    list = List()

    node_a = Node(data="a")
    list.head = node_a

    node_b = Node(data="b")
    node_a.next = node_b

    node_c = Node(data="c")
    node_b.next = node_c
