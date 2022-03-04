
### Given an integer, n, print the following values for each integer i from 1 to n: 
  1. Decimal 
  2. Octal 
  3. Hexadecimal (capitalized) 
  4. Binary 

### Function Description 
Complete the print_formatted function in the editor below. 
print_formatted has the following parameters: 
  • int number: the maximum value to print 

### Prints 
The four values must be printed on a single line in the order specified above for each i from 1 to number. Each value should 
be space-padded to match the width of the binary value of number and the values should be separated by a single space. 

### Input Format 
A single integer denoting n. 

### Constraints 
* 1 <= n <= 99 

### Sample Input
''' 
17
'''

### Sample Output
'''
    1     1     1     1<br/>
    2     2     2    10<br/>
    3     3     3    11<br/>
    4     4     4   100<br/>
    5     5     5   101<br/>
    6     6     6   110<br/>
    7     7     7   111<br/>
    8    10     8  1000<br/>
    9    11     9  1001<br/>
   10    12     A  1010<br/>
   11    13     B  1011<br/>
   12    14     C  1100<br/>
   13    15     D  1101<br/>
   14    16     E  1110<br/>
   15    17     F  1111<br/>
   16    20    10 10000<br/>
   17    21    11 10001<br/>
'''
