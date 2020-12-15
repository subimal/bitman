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
>>> from bitman import bitman
>>> a = bitman(size=5,init=1)
>>> print(a)
```

```
>>> print(a)
11111
```


