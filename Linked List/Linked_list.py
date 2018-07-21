class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    # Inserting in the last
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        last_node = self.head

        # Last node is not nulll
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # Inserting in the begining
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Inserting at N position
    def insert_after_node(self, prev_node, data):

        if not prev_node:
            print("Node not found in the list !")
            return

        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    # Deleting node from the linkedlist
    def delete_node(self, key):

        cur_node = self.head
        # If the key is head of the linkedlist
        if cur_node and cur_node.data == key:
            # Shifting the head of the linkedlist
            # to the next element of the linked list
            self.head = cur_node.next
            cur_node = None
            return

        # To keep track of the previous node
        prev = None

        # If the key is in the n'th position
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        # Moves the current node to the end of the list
        if cur_node is None:
            print("Key not found in the LinkedList!")
            return

        # Points the previous node of the key
        # to the nex node of the key(here cur_node)
        prev.next = cur_node.next
        cur_node = None

        # Deleting a node when a certain index/position is
        # given in the linked list
        def delete_at_position(self, position):
            cur_node = self.head

            # If head is found at the index 0
            if position == 0:
                self.head = cur_node.next
                cur_node = None
                return

            # To check keep track of the previous node
            prev = None
            # To start the counter from 1 as index 0 done
            count = 1

            while cur_node and count != position:
                prev = cur_node
                cur_node = cur_node.next
                count = count + 1

            if cur_node is None:
                print("Postion not found in the LinkedList")
                return

            # Moving the pointer of the previous node
            # to the pointer of the next node of the current
            # node
            prev.next = cur_node.next
            cur_node = None

    # Caclulates the length of the linked list
    # iteratively

    def length_iterative(self):
        cur_node = self.head

        count = 0

        while cur_node:
            count = count + 1
            cur_node = cur_node.next
        return count

    # Caclulates the length of the linked list
    # recusively

    def len_recursive(self, node):
        # Base case
        if node is None:
            return 0
        # Recursive call
        return 1 + self.len_recursive(node.next)

    def swap_nodes(self, key_1, key_2):

        if key_1 == key_2:
            print("Enter two diffrent nodes to swap! ")
            return

        prev_1 = None
        curr_1 = self.head
        # Searching for the first node
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        # Searching for the second node
        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        # If either of the node is not in the list
        if not curr_1 or not curr_2:
            print("Node not found")
            return

        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2

        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
# llist.prepend(1)

llist.swap_nodes("A", "C")

# print(llist.len_recursive(llist.head))
# llist.insert_after_node(llist.head.next, "2")
# llist.delete_node("e")
llist.print_list()
