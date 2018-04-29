
Day 1 Week 2

Big-O notation

```
https://en.wikipedia.org/wiki/Big_O_notation
```

```
http://bigocheatsheet.com
```

Binary search
```
https://en.wikipedia.org/wiki/Binary_search_algorithm
```

In computer science, a binary search or half-interval search algorithm finds the position of a specified input value (the search "key") within an array **sorted** by key value. For binary search, the array should be arranged in ascending or descending order. 

An example
The next best example I can think of is the telephone book, normally called the White Pages or similar but it'll vary from country to country. But I'm talking about the one that lists people by surname and then initials or first name, possibly address and then telephone numbers.

Now if you were instructing a computer to look up the phone number for "John Smith" in a telephone book that contains 1,000,000 names, what would you do? Ignoring the fact that you could guess how far in the S's started (let's assume you can't), what would you do?

A typical implementation might be to open up to the middle, take the 500,000th and compare it to "Smith". If it happens to be "Smith, John", we just got real lucky. Far more likely is that "John Smith" will be before or after that name. If it's after we then divide the last half of the phone book in half and repeat. If it's before then we divide the first half of the phone book in half and repeat. And so on.

This is called a binary search and is used every day in programming whether you realize it or not.

This is an O(log n) operation, which is generally the fastest search.

Insertion sort
```
https://en.wikipedia.org/wiki/Insertion_sort
```

Bubble sort
```
https://en.wikipedia.org/wiki/Bubble_sort
```

Selection sort
```
https://en.wikipedia.org/wiki/Selection_sort
```

Merge sort
```
https://en.wikipedia.org/wiki/Merge_sort
```
