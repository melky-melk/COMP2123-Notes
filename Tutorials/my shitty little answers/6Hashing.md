**Problem 1.** Consider a hash table of size N > 1, and the hash function such that h(k) = k mod 2 for every k. We insert a dataset S of size n < N. After that, what is the typical running times of get for chaining and open addressing (as a function of n)?



**Problem 2.** Suppose you are given a hash function h mapping 10-digit strings to integers in {1, 2, . . . , 10000}. Show that there is some dataset S of size 1, 000, 000 such that all keys of S are hashed to the same value.



**Problem 3.** Work out the details of implementing cycle detection in cuckoo hashing based on the number of iterations of the eviction sequence.

if there are 2 hash tables, of size N, then if the eviction sequence has 2N runs. that means it has traversed at most every single entry in the cycle, meaning that there are no empty spaces it can get to any more

if there are 4N runs that means that the alternate positions and the initial positioning is bad

**Problem 4.** Work out the details of implementing cycle detection in cuckoo hashing based on keeping a flag for each entry.

**Solution 4.** We augment each entry to have a boolean attribute called flag. Assuming that initially all entries are unflagged (i.e., flag is set to false), the put routine sets the flag of every item it evicts. If we ever run into a flagged item, we have a cycle. However, if we successfully find an empty slot, we must trace back our steps along the eviction sequence to unflag all the entries flagged. That way when we need to execute the next put all entries are unflagged again. The running time is proportional to the length of the eviction sequence.

**Problem 5**. Design a sorted hash table data structure that performs the usual operations of a hash table with the additional requirement that when we iterate over the items, we do so in the order in which they were inserted into the hash table. Iterating over the items should take O(n) time where n is the number of items stored in the hash table. Your data structure should only add O(1) time to the standard put, get, and delete operations.

use a normal linear probing, but keep a doubly linked list whenever a new element is added to the hashtable

**Problem 6**. Given an array with n integers, design an algorithm for finding a value that is most frequent in the array. Your algorithm should run in O(n) expected time.

loop through the array and keep a hashmap of every new value.

add a new value every time you encounter a value you havent seen before

```python
def frequency:
	hashmap 
```

so every time you get an array number you try to get it if it exists. and if it doesnt then you add it to the hashmap as a new key with the value of 0. if it does exist you increment the value them to count. 

then when you have finished iterating you check the highest value and return the key 

**Problem 7**. A multimap is a data structure that allows for multiple values to be associated with the same key. The method get(k) should return all the values associated with key k. Describe an implementation where this method runs in O(1 + s) expected time, where s is the number of values associated with k.

Each entry, instead of having a single value, has a linked list of values associated with the key. When putting a new item (k, v) we add v to the list in the entry associated with k. When getting a key k, we find it in O(1) expected time and we go over the list in the entry associated with k (which takes O(s) time).

**Problem 8**. Suppose that you have a group of n people and you would like to know if there are two people that share a birthday. Design an O(1) time algorithm that given the information about the n people’s birthdays, finds a pair that shares a birthday, or reports that no such pair exists.

you make a hashmap and add values to the list like above, when you report a same value for 2 birthdays then you say that at least 2 people share a birthday then you return the birthday key. 

**Problem 9**. In computational linguistics, texts (such as a book or an article) are modelled as a sequence of words. A k-gram is a sequence of k consecutive words. A common task in language modelling requires that we compute the frequency of all k-grams that appear in the text.

