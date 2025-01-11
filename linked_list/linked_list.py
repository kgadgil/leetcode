from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

def main():
    linked_list = LinkedList()
    linked_list.head = Node("Mon")
    e2 = Node("Tue")
    e3 = Node("Wed")
    e4 = Node("Thu")
    e5 = Node("Fri")
    linked_list.head.next = e2
    e2.next = e3
    e3.next = e4
    e4.next = e5
    print(linked_list)

    llist = deque(['Mon', 'Tue', 'Wed', 'Thu'])
    llist.append('Fri')
    print(llist)
    llist.pop()
    print(llist)

if __name__ == '__main__':
    main()