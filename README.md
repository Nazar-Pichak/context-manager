[![programming - python](https://img.shields.io/static/v1?label=programming&message=python&color=darkgreen&logo=python&logoColor=yellow)](https://docs.python.org/3/howto/functional.html)

# Practicing on context-manager

Context managers are used to set up and tear down temporary contexts, establish and resolve custom settings, and acquire and release resources. The ```open()``` function for opening files is one of the most familiar examples of a context manager and some
example:

```
f = open('random.txt', 'r')
contents = f.read()
f.close()
```


Context managers sandwich code blocks between two distinct pieces of logic:

- the enter logic - this runs right before the nested code block executes
- the exit logic - this runs right after the nested code block is done.

The most common way you'll work with context managers is by using the ```with statement```.

# The ```with``` statement

A ```with``` statement is the primary method used to call a context manager.
As an object oriented language, python compares all its entities to the object with specific behavior.
All objects which implement in his internal behavior magic methods ```__enter__``` and ```__exit__``` can call context manager.
The general syntax is as follows:

```
with SomeContextManager as context_variable:
    # do stuff with context_variable
```

This code works in the following order:

- ```SomeContextManager``` executes its enter (setup) logic via ```__enter__``` method before the indented code runs.
- ```SomeContextManager``` binds a value to ```context_variable```, which can be used in the indented code
- Inner code block runs: ```# do stuff.```
- ```SomeContextManager``` executes its exit (cleanup) logic via ```__exit__``` method.

So why is this useful? In the next section, we'll discuss why this programming pattern comes in handy and why it's worth making your context managers from time to time.

# Why use a context manager

Context managers keep our codebases much cleaner because they encapsulate administrative boilerplate and separate it from the business logic.

Additionally, context managers are structured to carry out their exit methods regardless of what happens in the code block they frame. So even if something goes wrong in the managed block, the context manager ensures the deallocations are performed and the default settings are restored.

See also [context manager](https://docs.python.org/3/library/contextlib.html) in python documentation.