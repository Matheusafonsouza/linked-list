package main

import "fmt"

type Node struct {
	prev *Node
	next *Node
	key  interface{}
}

type List struct {
	head *Node
	tail *Node
}

func (list *List) Insert(key interface{}) {
	node := &Node{
		next: list.head,
		key:  key,
	}

	if list.head != nil {
		list.head.prev = node
	}
	list.head = node

	aux_node := list.head
	for aux_node.next != nil {
		aux_node = aux_node.next
	}
	list.tail = aux_node
}

func PrintList(list *List) {
	node := list.head
	for node != nil {
		fmt.Printf("%v -> ", node.key)
		node = node.next
	}
	fmt.Println()
}

func PrintListBackwards(list *List) {
	node := list.tail
	for node != nil {
		fmt.Printf("%v <- ", node.key)
		node = node.prev
	}
	fmt.Println()
}

func main() {
	list := List{}
	list.Insert(5)
	list.Insert(8)
	list.Insert(9)
	list.Insert(11)
	list.Insert(29)
	list.Insert(25)

	PrintList(&list)
	PrintListBackwards(&list)
}
