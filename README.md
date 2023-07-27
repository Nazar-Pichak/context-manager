# Practicing on context-manager

Context managers are used to set up and tear down temporary contexts, establish and resolve custom settings, and acquire and release resources. The ```open()``` function for opening files is one of the most familiar examples of a context manager.

Context managers sandwich code blocks between two distinct pieces of logic:

- the enter logic - this runs right before the nested code block executes
- the exit logic - this runs right after the nested code block is done.

The most common way you'll work with context managers is by using the ```with statement```.

# The ```with``` statement

A ```with``` statement is the primary method used to call a context manager. The general syntax is as follows:

```
with SomeContextManager as context_variable:
    # do stuff with context_variable
```


