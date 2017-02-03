# Python Arrays and For Loops
Here's some pre-written JavaScript functions. Your job is to practice Python
by converting these functions from JavaScript to Python. You may run into some
errors along the way. If you find an error try to google for a solution. There
should be some good Stack Overflow results for the things we're trying to do.

Here are several commong errors I expect you to run into:

## IndexError: list index out of range
This means you accessed an array at an index beyond the number of things it has.

```python
a = [1,2,3]
print(a[99])
```

## TypeError: unsupported operand type(s) for +: 'int' and 'str'
Python won't automatically concatenate numbers and strings. You'll have to
pass a number through the `str()` function to manually convert it to a string
and get concatenation to work.

```python
"my favorite number is " + 1
```

```python
"my favorite number is " + str(1)
```

Or, use f-strings!

```
f"my favorite number is {1}"
```

## SyntaxError: invalid syntax `def a()`
Remember to append a colon at the end of a line when you define a function:

```pyhton
def print_hello()
  print("hello!")
```

```pyhton
def print_hello():
  print("hello!")
```

## IndentationError: expected an indented block / unexpected indent
Python is very, very particular about indendation. It literally uses indentation
to detect where functions begin and end. If you don't maintain perfect indentation
your code will not run.

You have some freedom. You can use tabs, two-spaces, or four-spaces or whatever
you like for your indentation. Python only requires that you be consistent.

### Bad
```pyhton
def print_hello():
print("hello!")
```

```pyhton
def print_hello()
  print("hello!")
    print("hello!")
```

### Good
```pyhton
def print_hello():
  print("hello!")
  print("hello!")
```

## Licensing
All content is licensed under a CC­BY­NC­SA 4.0 license.
All software code is licensed under GNU GPLv3. For commercial use or alternative licensing, please contact legal@ga.co.

