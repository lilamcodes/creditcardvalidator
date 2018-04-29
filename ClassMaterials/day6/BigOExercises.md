Exercise 1.

Write your Binary Search function.

Start at the middle of your dataset.
If the number you are searching for is lower, stop searching the greater half of the dataset. Find the middle of the lower half and repeat.

Similarly if it is greater, stop searching the smaller half and repeat the process on that half. By continuing to cut the dataset in half, eventually you get your index number. 

Number to search for - 3
alist = [1,2,3,4,5,6,7]



Exercise 2.

Write your Bubble Search function.

A bubble sort is a sorting algorithm with a Big O complexity of O(n**2). It is called bubble sort, because the small numbers "bubble" to the top of the list.  
The general flow is to step through the list, continually comparing pairs of numbers. If the number on the left is larger than the number on the right, swap them and continue.

Write a function, `bubble_sort()`, that takes an `list`. It should return a sorted `list`, using the bubble sort algorithm.

alist = [54,26,93,17,77,31,44,55,20]


Exercise 3.

Write an inseartion sort function.

Insertion sort is a common sorting algorithm that, while still its worst case is still O(n**2), it is much more efficient than Bubble sort on average.

According to wikipedia, when people manually sort something, like a deck of cards for example, most use a method similar to insertion sort.

alist = [54,26,93,17,77,31,44,55,20]

Exercise 4.

Write a Selection sort function.

The algorithm divides the input list into two parts: the sublist of items already sorted, which is built up from left to right at the front (left) of the list, and the sublist of items remaining to be sorted that occupy the rest of the list. Initially, the sorted sublist is empty and the unsorted sublist is the entire input list. The algorithm proceeds by finding the smallest (or largest, depending on sorting order) element in the unsorted sublist, exchanging (swapping) it with the leftmost unsorted element (putting it in sorted order), and moving the sublist boundaries one element to the right.

alist = [54,26,93,17,77,31,44,55,20]






























