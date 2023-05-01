# Задача 1.
# Необходимо реализовать метод разворота связного списка (двухсвязного или односвязного на выбор).


class Node:
   
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


head = Node(1, Node(2, Node(3, Node(4))))


def print_list(head, end='\n'):
    while head:
        print(head.data, end=' -> ' if head.next else '')
        head = head.next
    print(end=end)

print ("Список до разворота")
print_list(head)


def reverse_list(head, tail=None):
    while head:
        head.next, tail, head = tail, head, head.next
    return tail

print ()
print ("Список после разворота")
print_list(reverse_list(head))