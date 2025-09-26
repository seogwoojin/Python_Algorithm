T=int(input())

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

for _ in range(T):
    string=input()
    start_node = Node(None)
    head_node = start_node
    stack=[]
    point=0

    for st in string:
        if st == '<':
            if head_node.prev != None :
                head_node = head_node.prev
        elif st == '>':
            if head_node.next != None:
                head_node = head_node.next
        elif st == '-':
            if head_node.prev != None:
                if head_node.next != None:
                    head_node.next.prev = head_node.prev
                    head_node.prev.next = head_node.next
                    head_node = head_node.prev
                else:
                    head_node.prev.next = None
                    head_node = head_node.prev
        else:
            new_node = Node(st)
            new_node.prev = head_node
            if head_node.next != None:
                new_node.next = head_node.next
                head_node.next.prev = new_node
            head_node.next = new_node
            head_node = new_node
    stack=[]
    while start_node.next != None:
        start_node = start_node.next
        stack.append(start_node.data)
    print(''.join(stack))


