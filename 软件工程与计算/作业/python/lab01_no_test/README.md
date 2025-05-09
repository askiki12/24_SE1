# Lab01

为了锻炼大家的英文阅读能力，从本次作业开始，题目描述均采用英文啦……如果真的看不懂的话，建议在群里和大家讨论一下（但是其实可能看一下几个样例就大概明白是什么意思了）。

## Problem 1

The following snippet of code doesn't work! Figure out what is wrong and fix the bugs.  

```python
def both_odd(a, b):
		"""Returns True if both a and b are odd numbers.
		>>> both_odd(-1, 1)
		True
		>>> both_odd(2, 1)
		False
		"""
    return a and b % 2 == 1 # You can replace this line!
```

## Problem 2

Write a function that takes a positive integer n and returns its factorial. 
Factorial of a positive integer n is defined as  $n! = \prod\limits_{i=0}^n i = 1 \times 2 \times 3... \times n$

```python
def factorial(n):
    """Return the factorial of a positive integer n.
    >>> factorial(3)
    6
    >>> factorial(5)
    120
    """
    "*** YOUR CODE HERE ***"
```

## Problem 3

Write a function that takes three integers (may be nonpositive) and returns `True` if the three integers can form the three sides of a triangle, otherwise returns `False`.

```python
def is_triangle(a, b, c):
    """Given three integers (may be nonpositive), judge whether the three
    integers can form the three sides of a triangle.

    >>> is_triangle(2, 1, 3)
    False
    >>> is_triangle(5, -3, 4)
    False
    >>> is_triangle(2, 2, 2)
    True
    """
    pass  # YOUR CODE HERE
```

> 注：`pass`的作用：`pass`是一条“空指令”，表示什么都不做。
>
> 通常，当我们定义一个函数，但没有想好函数怎么实现的时候，我们就会填入一个`pass`来保持程序结构的正确性。大家在完成lab和后续作业的时候，应该先把这一行`pass`语句删除，然后再编写自己的代码，请不要在提交的代码中包含`pass`。

## Problem 4

Write a function that takes a positive integer *n* and returns the number of 6 in each digit of it. (Using floor division and modulo might be helpful here!

```python
def number_of_six(n):
    """Return the number of 6 in each digit of a positive integer n.

    >>> number_of_six(66)
    2
    >>> number_of_six(123456)
    1
    """
    pass  # YOUR CODE HERE
```

## Problem 5

Write a function that takes in a positive integer and return its max digit. (Using floor division and modulo might be helpful here!)

```python
def max_digit(x):
    """Return the max digit of a positive integer x.

    >>> max_digit(10)
    1
    >>> max_digit(4224)
    4
    >>> max_digit(1234567890)
    9
    >>> # make sure that you are using return rather than print
    >>> a = max_digit(123)
    >>> a
    3
    """
    pass  # YOUR CODE HERE
```
