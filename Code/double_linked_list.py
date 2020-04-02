class Node:
    def _init_(self, data):
        self.data=data
        self.previous=None
        self.next=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

#Add to the node list
    def addNode(self,data):
    #create new node
        newNode=Node(data)

    #IF LINKEDLIST IST EMPTY;head & tail point to new node
        if(self.head==None):
            self.head=self.tail=newNode
            self.head.previous=None
            self.tail.next=None
        else:
            self.tail.next=newNode
            newNode.previous=self.tail
            self.tail=newNode
            self.tail.next=None

    def display(self):
        current=self.head
        if(self.head==None):
            print('List is empty')
            return
        print('Nodes of doubly linked list:')
        while(current !=None):
        #print each node by incrementing pointer
            print(current.data)
            current=current.next

#Add nodes to the list
dList=DoublyLinkedList()
dList.addNode(1)
dList.addNode(2)
dList.addNode(3)
dList.addNode(4)
dList.addNode(5)

#display the nodes present in the list
#dList.display()