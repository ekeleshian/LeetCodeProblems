from pdb import set_trace


class LinkedList:
    def __init__(self, x):
        self.val = x
        self.next = None


    def get_size(self):
        counter = 0
        def helper(node, counter):
            if node:
                next_node = node.next
                return helper(next_node, counter + 1)
            else:
                return counter
        if self.next:
            return helper(self, counter)
        else:
            return 1


    def add_to_front(self, data):
        old_first = self
        new_first = LinkedList(data)
        new_first.next = old_first
        return new_first


    def remove_first(self):
        if self.next:
            return self.next
        else:
            return None #raise exception


    def add_to_end(self, data):
        def helper(node):
            if node.next:
                next_node = node.next
                return helper(next_node)
            else:
                return node
        last_node = helper(self)
        new_last = LinkedList(data)
        last_node.next = new_last
        # return self


    def remove_last(self):
        def helper(node,prev):
            if node.next:
                prev = node
                next_node = node.next
                return helper(next_node, prev)
            else:
                return prev

        second_to_last = helper(self, None)
        second_to_last.next = None
        # return self


    def add_at_index(self, index, data):
        curr_idx = 0
        curr_node = self
        size = self.get_size()
        if index > size - 1:
            print(f"OutOfBounds Error: Indexing at position {index} is not possible with a linkedlist of size {size}")
            return None
        while curr_idx < index:
            curr_idx += 1
            prev = curr_node
            curr_node = curr_node.next

        new_ith_node = LinkedList(data)
        prev.next = new_ith_node
        new_ith_node.next = curr_node
        # return self

    def remove_at_index(self, index):
        curr_idx = 0
        curr_node = self
        size = self.get_size()
        if index > size - 1:
            print(f"OutOfBounds Error: Indexing at position {index} is not possible with a linkedlist of size {size}")
            return None
        if index == 0:
            return self.remove_first()
        if index == size - 1:
            return self.remove_last()
        while curr_idx < index:
            curr_idx += 1
            prev = curr_node
            curr_node = curr_node.next
        next_node = curr_node.next
        prev.next = next_node
        return curr_node
        # return self












t = LinkedList(1)
m = LinkedList(2)
t.next = m
n = LinkedList(3)
m.next = n



result = t.remove_at_index(1)

print(result.val, result.next.val, result.next.next)
