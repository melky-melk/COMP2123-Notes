**Problem 3.** Given a singly linked list, we would like to traverse the elements of the list in reverse order. 

a) Design an algorithm that uses O(1) extra space. What is the best time complexity you can get?
keep a cursor of the element last counted

![[Pasted image 20220607133455.png]]
so it is O(n^2)

a) Design an algorithm that uses O( √n) extra space. What is the best time complexity you can get? 

![[Pasted image 20220607133834.png]]

O(n) time complexity 

you do an operation n^2, √n times

total time = √n * n^2
total time = $n^\frac{1}{2} \cdot n^2$
total time = $n^\frac{1 + 2}{2}$
total time = $n^\frac{3}{2}$


You are not allowed to modify the list, but you are allowed to use position/cursors to move around the list.

**Problem 6.** Using only two stacks, provide an implementation of a queue. Analyze the time complexity of enqueue and dequeue operations

![[Pasted image 20220607134751.png]]

when you want to enqueue push to the stack as per normal

when you want to dequeue you would pop all the elements from from the initial stack to another one
![[Pasted image 20220607135101.png]]

then pop that last element on the second stack

then repop that entire stack to the first one

**Problem 7**. We want to extend the queue that we saw during the lectures with an operation getAverage() that returns the average value of all elements stored in the queue. This operation should run in O(1) time and the running time of the other queue operations should remain the same as those of a regular queue. 

a) Design the getAverage() operation. Also describe any changes you make to the other operations, if any. 

while enqueing elements into the queue you keep a value called size and add 1 to it whenever a new element is added, also you would add to a value called sum while enqueing. similarly, when dequeing you subtract 1 and subtract the element you removed

when getting the average you would simply get the sum and divide it by the size

b) Briefly argue the correctness of your operation(s). 
the averages are calculated by the total sum of something divided the number of those things, since the queue keeps track of the sum whenever something is added, and the size. and thios sum and size are updated whenever something is dequeed or enqueued into the list, it can accurately callculate the time in O(1).

c) Analyse the running time of your operation(s).



