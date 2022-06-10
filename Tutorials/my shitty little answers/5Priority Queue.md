**Problem 1**. Come up with an instance showing that selection-sort takes Ω(n 2 ) time in the worst case.



**Problem 2**. Come up with an instance showing that insertion-sort takes Ω(n 2 ) time in the worst case.



**Problem 3**. Come up with an instance showing that heap-sort takes Ω(n log n) time in the worst case.

assuminbg being the min-heap sort being

{9,8,7,6,5,4,3,2,1}

in this case, every time a new element is added, it will need to traverse log(n) (max, because of the way the heap is) to go down the height of the tree everytime something is added. and would need to restore its AVL property every time something new is inserted, log(n) * n

then to return the heap, it would need to pop every integer off, which would take n time

**Problem 4**. Given an array A with n integers, an inversion is a pair of indices i < j such that A[i] > A[j]. Show that the in-place version of insertion-sort runs in O(n + I) time where I is the total number of inversions.





**Problem 5**. Given an array A with n distinct integers, design an O(n log k) time algorithm for finding the kth value in sorted order.

We use a priority queue that supports max and remove-max operations. We start by inserting the first k elements from A into the priority queue. Then we scan the rest of array comparing the current entry A[i] to the maximum value in the priority queue, if A[i] is greater than the current maximum, we can safely ignore it as it cannot be the kth value due to the fact that the priority queue holds k values smaller than A[i]. On the other hand, if A[i] is less than the current maximum, we remove the maximum from the queue and insert A[i]. After we are done processing all the entries in A, we return the maximum value in the priority queue. 

the priority queue must only have a height of O(log k)

have a max priority queue, insert the the first k element to the priority heap. then you check the rest of the array, (n - k) elements, one by one to see if the max in the queue value is greater. thrn that means it cannot be the kth value? 

To argue the correctness of the algorithm we can use induction to prove that after processing A[i], the k smallest elements in A[0, i] are in the queue. Since we return the largest element in the queue after processing the whole array A (which we just argued holds the k smaller elements in A), we are guaranteed to return the kth element of A. 

The time complexity is dominated by O(n) plus the time it takes to perform the remove-max and insert operations in the priority queue. In the worst case we perform n such operations each one taking O(log k) time, when we implement the priority queue as a heap. Thus, the overall time complexity is O(n log k).

**Problem 6**. Given k sorted lists of length m, design an algorithm that merges the list into a single sorted lists in O(mk log k) time.

