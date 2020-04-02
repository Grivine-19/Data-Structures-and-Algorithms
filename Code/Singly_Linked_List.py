class Node(object):
    def __init__(self, data=None, reference=None):
        self.data = data
        self.reference = reference

    def get_data(self):
        return self.data

    def get_next(self):
        return self.reference

    def set_next(self, new_next):
        self.reference = new_next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        node = self.head
        n = []
        while node is not None:
            n.append(node.data)
            node = node.reference
        return f" Linked List: {n}"

    def traverse(self):
        if self.head is None:
            print("List has no item")
            return
        else:
            n = self.head
            while n is not None:
                print(n.get_data(), " ")
                n = n.reference

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
            if current is None:
                raise ValueError("Data not in list!")
            if previous is None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())

    def insert_before_item(self, x, data):
        if self.head is None:
            print("List has no element")
            return

        if x == self.head.items():
            new_node = Node(data)
            new_node.reference = self.head
            self.head = new_node
            return

        n = self.head
        print(n.reference)
        while n.reference is not None:
            if n.reference.get_data() == x:
                break
            n = n.reference
        if n.reference is None:
            print("Item not in the list")
        else:
            new_node = Node(data)
            new_node.reference = n.reference
            n.reference = new_node


arr = LinkedList()
arr.insert(34)
arr.insert(45)
arr.insert(68)
print(arr)
arr.delete(34)
arr.traverse()
x = arr.search(34)
