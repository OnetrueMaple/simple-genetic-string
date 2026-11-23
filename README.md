## Simple Genetic String
A Python program for finding arbitrary strings of text through random brute force with selection bias.

## Features
    * Allows the user to choose a string
    * Has a built in PRNG with real entropy (timing variance)
    * Only uses the standard library

## Technologies
    * Python for portability
    * Oversimplified ML algorithm to score and select good strings

## Usage
If you have python installed on your computer, download 'sample-genetic.py' and 'util.py', ensure they are both in the same directory and run 'python3 sample-genetic.py' in your
terminal. Once you enter a string, the program will rebuild it from an empty string.

## Preview
```
user@User:~$ python3 sample-genetic.py
What string should the program find?
any
Closest string: 'Ha' for Generation 1
Closest string: 'H?a' for Generation 2
Closest string: 'u?a' for Generation 3
Closest string: 'uya' for Generation 4
Closest string: 'uyy' for Generation 5
Closest string: 'uXy' for Generation 6
Closest string: 'uHy' for Generation 7
Closest string: 'uxy' for Generation 8
Closest string: '&xy' for Generation 9
Closest string: 'xxy' for Generation 10
Closest string: 'xpy' for Generation 11
Closest string: 'xcy' for Generation 12
Closest string: 'x9y' for Generation 13
Closest string: 'xny' for Generation 14
Closest string: 'Xny' for Generation 15
Closest string: 'any' for Generation 16
Generation '16': {0: 'Xny', 1: 'X(ny', 2: 'Xn&', 3: 'ny', 4: 'XnJ', 5: 'tny', 6: 'XnA', 7: 'mXny', 8: 'any', 9: 'X:ny', 10: 'Xn', 11: 'Xmy', 12: '1ny', 13: 'XnW', 14: 'Xn', 15: 'Xnq', 16: 'rXny', 17: 'Xy', 18: '*Xny', 19: 'Xn-', 20: 'Xn1', 21: 'Xy', 22: 'Xn#', 23: 'Xey', 24: 'Xy'}
Found the target string: 'any' in 16 Generations!
```