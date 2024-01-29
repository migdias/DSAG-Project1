class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size
    
    def aslist(self) -> list:
        arr = []
        node = self.head
        while node:
            if node.value:
                arr.append(node)
            node = node.next
        
        return arr
    

def union(llist_1: 'LinkedList', llist_2: 'LinkedList') -> 'LinkedList':
    """
    Run time analysis: Since we are scanning the the two linked list at the same time, the worst case scenario will be O(n*2), which is the 
    scanning of both lists with the same size. Then adding elements that are not repeated, we use a hash map (set) that is O(1). Therefore,
    the run time is O(n).
    """
    l1_node = llist_1.head
    l2_node = llist_2.head

    llist_union = LinkedList()
    added_elements = set()
    
    # SCAN AT THE SAME TIME
    while l1_node or l2_node:
        # l1 node exists        
        if l1_node:
            # if l1 node exists, check if was added already. if not -> add to linked list, else do nothing
            if l1_node.value not in added_elements:
                llist_union.append(Node(l1_node.value))
                added_elements.add(l1_node.value)
            l1_node = l1_node.next
        # if node l2 exists
        if l2_node:
            # if l2 node exists, check if was added already. if not -> add to linked list, else do nothing
            if l2_node.value not in added_elements:
                llist_union.append(Node(l2_node.value))
                added_elements.add(l2_node.value)
            l2_node = l2_node.next # get next l2

    return llist_union

def intersection(llist_1: 'LinkedList', llist_2: 'LinkedList') -> 'LinkedList':
    """
    Run code analysis: In this case we again have to scan both lists in its entirety -> O(n) as above.
    Also, we use two hash maps (sets), which are both O(1). Therefore, the complexity is O(n)
    """
    l1_node = llist_1.head
    l2_node = llist_2.head

    llist_intersection = LinkedList()
    l1_elements = set()
    llist_added_elements = set()

    # SCAN ONE AFTER THE OTHER
    while l1_node:
        l1_elements.add(l1_node.value)
        l1_node = l1_node.next

    # Second Scan and check similar values
    while l2_node:
        if l2_node.value in l1_elements:
            if l2_node.value not in llist_added_elements:
                llist_intersection.append(Node(l2_node.value))
                llist_added_elements.add(l2_node.value)
        l2_node = l2_node.next

    return llist_intersection

if __name__ == '__main__':
    ## Test case 1

    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,21]
    element_2 = [6,32,4,9,6,1,11,21,1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print (union(linked_list_1,linked_list_2))
    print (intersection(linked_list_1,linked_list_2))

    ## Test case 2

    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,23]
    element_2 = [1,7,8,9,11,21,1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print (union(linked_list_3,linked_list_4))
    print (intersection(linked_list_3,linked_list_4))

    ## Add your own test cases: include at least three test cases
    ## and two of them must include edge cases, such as null, empty or very large values
    def build_llist(arr) -> LinkedList:
        l = LinkedList()
        for i in arr:
            l.append(i)
        return l


    ## Test Case 1 -- no repeated values
    a = build_llist([1, 2, 3, 4])
    b = build_llist([5, 6, 7, 8])

    assert str(union(a, b).aslist()) == str([1, 5, 2, 6, 3, 7, 4, 8]), 'Bad union'
    assert str(intersection(a, b).aslist()) == str([]), 'Bad intersection'


    ## Test Case 2 -- possible intersection 
    a = build_llist([1, 2, 3, 4])
    b = build_llist([2, 3, 5, 6, 7, 8])

    assert str(union(a, b).aslist()) == str([1, 2, 3, 5, 4, 6, 7, 8]), 'Bad union'
    assert str(intersection(a, b).aslist()) == str([2, 3]), 'Bad intersection'

    ## Test Case 3 -- no intersection with repeated value in the same list
    a = build_llist([1, 2, 3, 4, 3, 2, 1])
    b = build_llist([5, 6, 7, 8])

    assert str(union(a, b).aslist()) == str([1, 5, 2, 6, 3, 7, 4, 8]), 'Bad union'
    assert str(intersection(a, b).aslist()) == str([]), 'Bad intersection'

    ## Test Case 4 - union between null and normal
    a = build_llist([])
    b = build_llist([5, 6, 7, 8])

    assert str(union(a, b).aslist()) == str([5, 6, 7, 8]), 'Bad union'
    assert str(intersection(a, b).aslist()) == str([]), 'Bad intersection'
