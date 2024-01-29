# Problem 5 - BlockChain

In this case I added a pointer to the previous block since it was needed to traverse the list.

In a normal blockchain, each node hash is calculated based on the timestamp, data and previous hash.

Adding data blocks basically adds 0 if there are no blocks (genesis), or adds to the head, with a pointer to the previous block.

The overall time complexity is O(1) for adding blocks and for scan or print is O(n), so if we need to print, its O(n). In case of the space complexity it is O(N) where N is the number of blocks in the blockchain, since the blocks are stored in memory.