# Problem 3 - Huffman Encoding and Decoding

In this problem my main issue was creating a priority queue that can directly sort it whenever new elements are added. By using heapq to make a priority queue, we can have a complexity for insert and popmin of O(log n).

Initializing the tree loops throught the characters in the sentence and inserts the nodes in the priority queue, which makes the complexity O(n log n).

Building the huffman tree is also O(n log n) since it involves repeated popping and pushing into the priority queue until a single node remains for n nodes.

Traversing the tree is a recursive operation that needs to visit each node once. Worst case, it needs to visit all nodes, which makes it O(n)

Encoding and Decoding involves searching the tree for a specific node, m times (where m is the length of the string). Therefore its O(m).

Overall, the dominant factor is around the creation of the Huffman tree, which makes it at worst case be O(n log n).