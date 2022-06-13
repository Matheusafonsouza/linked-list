from __future__ import annotations


class Node:
    def __init__(self, data: str) -> None:
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self) -> str:
        return self.data


class List:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def insert(self, data: str) -> None:
        node = Node(data=data)
        node.next = self.head

        if self.head != None:
            self.head.prev = node
        self.head = node

        aux_node = self.head
        while aux_node.next != None:
            aux_node = aux_node.next
        self.tail = aux_node

    def print_list(self) -> None:
        node = self.head
        while node != None:
            print(f"{node.data} -> ", end=" ")
            node = node.next
        print("\n")

    def print_list_backwards(self) -> None:
        node = self.tail
        while node != None:
            print(f"{node.data} <- ", end=" ")
            node = node.prev
        print("\n")


if __name__ == "__main__":
    list = List()

    list.insert(5)
    list.insert(8)
    list.insert(9)
    list.insert(12)
    list.insert(15)
    list.insert(33)
    list.insert(42)

    list.print_list()
    list.print_list_backwards()
