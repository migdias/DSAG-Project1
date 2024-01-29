# Problem 2 - Find files recursively

In this problem I opted to used a Stack and Recursion. 

The stack would add folders to itself, allowing for a kind of memory, to revisit later. While there were folders to still visit, the function would call itself over and over with a new path until it found a match o files.

Since we needed to traverse the whole file structure in order to find all files with matching suffix, the time complexity is O(n).

The space complexity if dominated by the stack, which we can express as O(n + h) where n is the number of elements in the deque and h is the maximum depth of the directory structure.