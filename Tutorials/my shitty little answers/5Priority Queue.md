**Problem 1**. Come up with an instance showing that selection-sort takes Ω(n 2 ) time in the worst case.



**Problem 2**. Come up with an instance showing that insertion-sort takes Ω(n 2 ) time in the worst case.



**Problem 3**. Come up with an instance showing that heap-sort takes Ω(n log n) time in the worst case.

assuminbg being the min-heap sort being

{9,8,7,6,5,4,3,2,1}

in this case, every time a new element is added, it will need to traverse log(n) (max, because of the way the heap is) to go down the height of the tree everytime something is added. and would need to restore its AVL property every time something new is inserted, log(n) * n

then to return the heap, it would need to pop every integer off, which would take n time

**Problem 4**. Given an array A with n integers, an inversion is a pair of indices i < j such that A[i] > A[j]. Show that the in-place version of insertion-sort runs in O(n + I) time where I is the total number of inversions.



**Problem 5**. Given an array A with n distinct integers, design an O(n log k) time algorithm for finding the kth value in sorted order.



**Problem 6**. Given k sorted lists of length m, design an algorithm that merges the list into a single sorted lists in O(mk log k) time.

