Exercise 1: 
A prime number is an integer greater than 1 that is only divisible by one and itself. Write a function that determines whether or not its parameter is prime, returning True if it is, and False otherwise. Write a main program that reads an integer from the user and displays a message indicating whether or not it is prime. Ensure that the main program will not run if the file containing your solution is imported
into another program.

Exercise 2:
A string is a palindrome if it is identical forward and backward. For example “anna”, “civic”, “level” and “hannah” are all examples of palindromic words. Write a program that reads a string from the user and uses a loop to determines whether or not it is a
palindrome. Display the result, including a meaningful output message.

Exercise 3:
Two words are anagrams if they contain all of the same letters, but in a different order. For example, “evil” and “live” are anagrams because each contains one e, one i, one l, and one v. Create a program that reads two strings from the user, determines whether or not they are anagrams, and reports the result.

Exercise 4:
One of the first known examples of encryption was used by Julius Caesar. Caesar needed to provide written instructions to his generals, but he didn’t want his enemies to learn his plans if the message slipped into their hands. As result, he developed what later became known as the Caesar Cipher.
The idea behind this cipher is simple (and as a result, it provides no protection against modern code breaking techniques). Each letter in the original message is shifted by 3 places. As a result, A becomes D, B becomes E, C becomes F, D becomes G, etc. The last three letters in the alphabet are wrapped around to the beginning: X becomes A, Y becomes B and Z becomes C. Non-letter characters are not modified by the cipher.
Write a program that implements a Caesar cipher. Allow the user to supply the message and the shift amount, and then display the shifted message. Ensure that your program encodes both uppercase and lowercase letters. Your program should also support negative shift values so that it can be used both to encode messages and decode messages. Hints: ord(), chr()
```
 https://learncryptography.com/classical-encryption/caesar-cipher
```

Exercise 5:
Did you know our numeral system - the symbols we use to represent numbers are called
Arabic numerals? Fun fact, because now it gets serious. You're going to be translating Arabic to Italian.

Have the input form accept a number from the user. When the form is submitted, have the function to_roman take an integer as an argument and return a roman numerals string. For example:
```
60 >> LX  
78 >> LXXVIII  
99 >> XCIX  
3000 >>> MMM  
```
Look up Roman Numerals to get a complete list and jog your memory on its ancient conventions. This is an easy challenge to code, but can be a difficult mental exercise. Don't overcomplicate it!
Hints: divmod(a, b)
```
https://en.wikipedia.org/wiki/Roman_numerals
```

Exercise 6:

- Create a function that will take in two numbers as parameters. The functions job will be able to evaluate how many times one number needs to be increased by itself in order to be divided by the other number without any remainder. The function should print what the number is and how many times the first number was increased.
- For example,
```
3,4 ==> remainder of 1
6,4 ==> remainder of 2
9,4 ==> remainder of 1
12,4 ==> remainder of 0
```

Exercise 7 - Reverse Polish Notation:

- For whatever reason, people in Poland put there numbers first and the the operator.
- For example:
```
3 4 + = 7
4 2 / = 2
3 4 - 5 + = 4
```
- Write a function that will take in the string, and print or return the answer to the arithmetic operation.

Exercise 8 - Factorial:

- Write a function that will calculate the factorial of a given number passed in as a parameter.
```
factorial(5) ====> 120
```




