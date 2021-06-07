package main

import "fmt"

// Node of a doubly-linked list
type Node struct {
	prev  *Node
	value int
	next  *Node
}

func CreateNode(value int, prev *Node, next *Node) *Node {
	var node Node
	node.next = next
	node.value = value
	node.prev = prev

	if prev != nil {
		prev.next = &node
	}

	return &node
}

func printLinkedList(start *Node, end *Node, traverse_reverse bool) {
	if traverse_reverse {
		node := end
		for node.prev != nil {
			fmt.Print(node.value, " <--> ")
			node = node.prev
		}
	} else {
		node := start
		for node.next != nil {
			fmt.Print(node.value, " <--> ")
			node = node.next
		}
	}

	fmt.Print("\n")
}

func main() {
	first := CreateNode(0, nil, nil)
	lastadded := first
	last := first

	for i := 1; i < 10; i++ {
		lastadded = CreateNode(i, lastadded, nil)
	}
	last = lastadded

	printLinkedList(first, last, false)
}
