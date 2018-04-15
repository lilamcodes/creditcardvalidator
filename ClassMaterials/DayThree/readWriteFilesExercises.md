Exercise 1:
Please write a program which count and print the numbers of each character, from file letters.txt, in a string input by console.

Example:
If the following string is given as input from file letters.txt to the program:

abcdefgabc

Then, the output of the program should be:

a,2
c,2
b,2
e,1
d,1
g,1
f,1

Hints:
Use dict to store key/value pairs.
Use dict.get() method to lookup a key with default value.


Exercise 2:

Write a program that takes a filename and a parameter `n` and prints the `n` most common words in the file, and the count of their occurrences, in descending order.

For example:

        word_stats("article.txt", 5)

        "the", 39
        "device", 21
        "start", 14
        "pidgeon", 9
        "box", 3

Import the included `article.txt` file and use that to test your program. What are the top 10 words and their frequency?



HOMEWORK Exercise 3:

1st Part.

Create functionS that would read file book.csv, clean data and save cleaned data with a new csv file.

Sample Output is cleanfile.csv

2nd Part.

Take your newly created csv file and calculate the diffirence in Original Fico and Current Fico. Hint: use DictReader from csv module.

Sample Output:

Betty,Yakich,162
Edgar,Elkareh,77
Justin,Bosse,147
Philip,Clementi,149
Dan,Noska,239









