""""
Implementation of a Linked list
"""

""""
Operations:
==========
1. Create a list with given elements
2. Display the elements in a list
3. Find the number of elements in a list
4. Retrieve the element at a given position
5. Add or remove element(s)
6. Check if list is empty
7. Delete an element from list
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # check if the list is empty
    def is_empty(self) -> bool:
        return self.head is None

    # append node to the list
    def append(self, value) -> None:
        if self.is_empty():
            self.head = Node(value)
            return

        # list has some nodes
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = Node(value)
        return

    # print all elements to the console
    def print_elements(self) -> None:
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=" "),
            current_node = current_node.next
        print()
        return

    # find the length of the list
    def length(self) -> int:
        result = 0
        current_node = self.head

        while current_node is not None:
            result += 1
            current_node = current_node.next

        return result

    # find element at the given position
    def get_element(self, position: int) -> int or None:
        index = 0
        current_node = self.head

        while current_node is not None:
            if index == position:
                return current_node.data

            current_node = current_node.next
            index += 1

        return None

    # delement element from list
    def delete(self, data) -> None:
        if self.is_empty():
            print("\nList empty, cannot delete.")
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        trail_current_node = self.head
        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next

            if current_node.data == data:
                trail_current_node.next = current_node.next
                return

            trail_current_node = current_node

        print(f"\nElement {data} not found, cannot delete")
        return

    # reverse list
    def reverse(self) -> None:
        if self.head is None:
            return

        current_node = self.head
        prev_node = None

        while current_node is not None:
            # Track the next node
            next_node = current_node.next

            # Modify the current node
            current_node.next = prev_node

            # Update prev and current
            prev_node = current_node
            current_node = next_node

        self.head = prev_node
        return
