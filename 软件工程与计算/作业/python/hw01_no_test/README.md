# Homework01

这次作业我们暂时不给大家样例，看看大家能否自己通过自己测试找出代码的问题。

[toc]

## Problem 1: A Sub Abs B

Fill in the blanks in the following function for subtracting **a** with the absolute value of **b**, without calling `abs`. You may **not** modify any of the provided code other than the two blanks.

```python
from operator import add, sub, mul, neg

def a_sub_abs_b(a, b):
    """Return a-abs(b), but do not call abs.

    >>> a_sub_abs_b(2, 3)
    -1
    >>> a_sub_abs_b(2, -3)
    -1
    >>> # a check that you didn't change the return statement!
    >>> import inspect, re
    >>> re.findall(r'^\s*(return .*)', inspect.getsource(a_sub_abs_b), re.M)
    ['return h(a, b)']
    """
    if b >= 0:
        h = _____
    else:
        h = _____
    return h(a, b)
```

> 提示：你可能会想使用`add` ，`sub` ，`mul`  and/or `neg` 等操作符，可以阅读文档：https://docs.python.org/3/library/operator.html#mapping-operators-to-functions
>

## Problem 2: Two Of Three

在函数体中**只使用一行代码**（也就是只允许在横线处补充），请返回三个参数中最大的两个数的平方之和

Write a function that takes three positive numbers and returns the sum of the squares of the two largest numbers. **Use only a single line for the body of the function.**

```python
def two_of_three(x, y, z):
    """Return a*a + b*b, where a and b are the two largest members of the
    positive numbers x, y, and z.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    24
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    >>> # check that your code consists of nothing but an expression (this docstring)
    >>> # and a return statement
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(two_of_three)).body[0].body]
    ['Expr', 'Return']
    """
    return _____
```

提示：考虑使用max和min函数：

```
>>> max(1, 2, 3)
3
>>> min(-1, -2, -3)
-3
```



## Problem 3: Largest Factor

Write a function that takes an integer x that is **greater than** 1 and returns the largest integer that is smaller than x and evenly divides x.

```python
def largest_factor(x):
    """Return the largest factor of x that is smaller than x.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    "*** YOUR CODE HERE ***"
```

## Problem 4: If Function vs Statement

```python
def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result
```

Despite the doctests above, this function actually does not do the same thing as an `if` statement in all cases.

To prove this fact, write functions `c`, `t`, and `f` such that `with_if_statement` prints the number 2, but `with_if_function` prints both 1 and 2.

```python
def with_if_statement():
    """
    >>> result = with_if_statement()
    2
    >>> print(result)
    None
    """
    if c():
        return t()
    else:
        return f()

def with_if_function():
    """
    >>> result = with_if_function()
    1
    2
    >>> print(result)
    None
    """
    return if_function(c(), t(), f())

def c():
    "*** YOUR CODE HERE ***"

def t():
    "*** YOUR CODE HERE ***"

def f():
    "*** YOUR CODE HERE ***"
```

> 提示：在本题中，你需要补充`c()`, `t()`, `f()`的代码，使得`with_if_statement()`打印2，`with_if_function()`打印1和2，且两个函数的返回值都为`None`。也就是满足如下结果；
>
> ```python
> >>> result = with_if_statement()
> 2
> >>> print(result)
> None
>     
> >>> result = with_if_function()
> 1
> 2
> >>> print(result)
> None
> ```
>
> 注意，你不需要修改`if_function()`, `with_if_statement()`或`with_if_function()`部分的代码。
>
> 如果你在此题遇到了困难，可以尝试思考以下三个问题
>
> 1. 在`with_if_statement()`中，`t`和`f`是否一定会执行？
> 2. 当`c()`,`t()`,`f()`作为参数传入`if_function()`中时，`t`和`f`是否一定会执行？
> 3. `c`,`t`,`f`三个方法，哪个需要返回值，哪个不需要返回值？
>
> 如果还是觉得无从下手，可以阅读以下网址，进一步区分`if_statement`与`if_function`两者的区别
>
> http://composingprograms.com/pages/15-control.html#conditional-statements
>
> http://composingprograms.com/pages/12-elements-of-programming.html#call-expressions
>

## Problem 5: Hailstone

Douglas Hofstadter's Pulitzer-prize-winning book, *Gödel, Escher, Bach*, poses the following mathematical puzzle.

1. Pick a positive integer x as the start.
2. If x is even, divide it by 2.
3. If x is odd, multiply it by 3 and add 1.
4. Continue this process until x is 1.

The number x will travel up and down but eventually end at 1 (at least for all numbers that have ever been tried -- nobody has ever proved that the sequence will terminate). Analogously, a hailstone travels up and down in the atmosphere before eventually landing on earth.

This sequence of values of x is often called a Hailstone sequence. Write a function that takes a single argument with formal parameter name x, prints out the hailstone sequence starting at x, and returns the number of steps in the sequence:

```python
def hailstone(x):
    """Print the hailstone sequence starting at x and return its length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
```

> 提示：你需要在函数中打印hailstone序列，并返回序列长度。
>

## Problem 6: Falling Factorial

Let's write a function `falling`, which is a "falling" factorial that takes two arguments, n and k, and returns the product of k consecutive numbers, starting from n and working downwards. (This problem is an advanced version of Problem 2, Lab 01.)

```python
def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
```

## Problem 7: Double Ones 

Write a function that takes in a number and determines if the digits contain two adjacent 1s.

```Python
def double_ones(n):
    """Return true if n has two ones in a row.

    >>> double_ones(1)
    False
    >>> double_ones(11)
    True
    >>> double_ones(2112)
    True
    >>> double_ones(110011)
    True
    >>> double_ones(12345)
    False
    >>> double_ones(10101010)
    False
    """
    "*** YOUR CODE HERE ***"
```

