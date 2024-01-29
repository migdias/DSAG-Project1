# Creating an LRU Cache

In this problem it was clear I needed to create a CacheObject that will be a node in a DoubleLinkedList. A DoubleLinked list was necessary for quick O(1) functionalities like moving objects to the head of the list, or removing the tail object.

The Class LRU was created, which represented a DoubleLinkedList of CacheObjects. The idea was to, when the cache size was at max, it would removed the tail of the linked list (the Least Recently Used). Whenever a get() or set() method was used, the CacheObject was "hit" on the Linked list and moved it to the head. When performing a get() with the list was maxed out, it would remove the LRU and add the new object to the head.

For the cache I opted to used a Dictionary since there is also O(1) or getting checking whether an object exists, or simply getting it.

Run time complexity: 
    - Get Method -> O(1)
    - Set Method -> O(1)
    - Remove LRU -> O(1)

-> The overall time complexity therefore O(1)