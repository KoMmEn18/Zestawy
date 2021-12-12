from node import Node

class SingleList:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def count(self):
        return self.length

    def insert_head(self, node):
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):
        if self.head:
            self.tail.next = node
            self.tail = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def remove_head(self):
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None
        self.length -= 1
        return node

    def remove_tail(self):
        if self.is_empty():
            raise ValueError("pusta lista")
        node_to_delete = self.tail
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            node = self.head
            while(node.next.next != None):
                node = node.next
            node.next = None
            self.tail = node
        self.length -= 1
        return node_to_delete

    def join(self, other):
        if self.is_empty() or other.is_empty():
            raise ValueError("pusta lista")
        if self.head:
            self.tail.next = other.head
        else:
            self.head = self.tail = other.head
        self.length += other.length
        self.tail = other.tail
        other.clear()

    def clear(self):
        self.length = 0
        self.head = None
        self.tail = None

    def print(self):
        tmp = self.head
        if(self.length == 0):
            print('lista jest pusta')
        else:
            for i in range(self.length):
                if(i + 1 < self.length):
                    print(tmp.data, end=" -> ")
                else:
                    print(tmp.data)
                tmp = tmp.next


if __name__ == "__main__":
    single_list = SingleList()
    single_list.insert_tail(Node(5))
    single_list.insert_tail(Node(6))
    single_list.insert_tail(Node(7))
    single_list.insert_tail(Node(8))
    single_list.print()

    other_list = SingleList()
    other_list.insert_tail(Node(1))
    other_list.insert_tail(Node(2))
    other_list.insert_tail(Node(3))
    other_list.print()
    
    other_list.join(single_list)
    other_list.print()

    print(other_list.remove_tail())
    other_list.print()

    other_list.clear()
    other_list.print()