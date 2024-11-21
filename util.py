class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        """Agrega un nodo al final de la lista."""
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)

    def display(self):
        """Muestra los valores de la lista enlazada."""
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        print(" -> ".join(map(str, values)))
