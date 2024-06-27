class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

ll1 = LinkedList(1)
ll2 = LinkedList(2)
ll3 = LinkedList(3)
ll1.next = ll2
ll2.next = ll3    # 1 -> 2 -> 3

current = ll1
while current:
    print(current.value)
    current = current.next