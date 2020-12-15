# bitman

## What is bitman?
This is a pure python module for MANaging an array of BITs. 

## How does it work?
bitman takes advantage of python's ability to handle big integers. The array of bits is simply an integer with its bit values set as desired. 

The array of bits is a class called bitman.

## Attributes of bitman

* **size**: It is an integer that holds the array size.
* **set(n, val)**: A function that sets the n-th bit to val.
* **get(n)**:	A function that returns the truth value of the n-th bit.
* **which(val)**: A list of positions with a value val (0 or 1).


## Examples

### Initializing a bitman instance

```python
>>> from bitman import bitman  		# import the bitman class
>>> a = bitman(size=5,init=1)  		# 'a' is now a bitman instance with 5 bits, all initialized to 1
>>> print(a)				# printing 'a' returns the string of bits as in a binary number
11111
>>> a					# simply typing 'a' at the command line also returns the bits in the same order
11111
>>> a.get(2)				# get the truth value of the bit at position 2
True
>>> a.set(0, 0)				# set the bit at position 0 to 0.
>>> a
11110
>>> a.set(2, 0)				# set the bit at position 2 to 0.
>>> a
11010

```



