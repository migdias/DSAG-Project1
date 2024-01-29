# Problem 6 - Union and Intersection

## Union

In the union operation, it traverses the two lists at the same time, while adding already used elements to a hash map. If the values have already been added, it doesnt need to add again.

Run time analysis for Union: Since we are scanning the the two linked list at the same time, the worst case scenario will be O(n*2), which is the 
scanning of both lists with the same size. Then adding elements that are not repeated, we use a hash map (set) that is O(1). Therefore,
the run time is O(n).

## Intersection

On the intersection, it traverses the first list and adds the elements on a set.
Then it traverses the second list and only adds elements to the result if they are also in the set. Duplicate elements are not readded with the help of another set.
Run code analysis: In this case we again have to scan both lists in its entirety -> O(n) as above.
Also, we use two hash maps (sets), which are both O(1). Therefore, the complexity is O(n)


The space complexity for both is O(n) in the worst case (intersection, both lists are the same, union, when are completely different O(2n)-> O(n))