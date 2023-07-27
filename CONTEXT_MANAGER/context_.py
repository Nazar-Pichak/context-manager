# l = []
# for i in range(10000):
    # with open('store_.txt', 'w') as file:
        # l.append(file)

# There is a context-manager statemante for working with files of any type.
# The main advantage it is automatic invoking the close() method, despite on the 
# errors during the program execution.
# We cannot write or read any data outside of the block in the context manager.
# It will rise an error (I/O operation on closed file).
# Not all objects support context manager statemante depending on the their magic attributes.

with open('store_.txt', 'w') as file:
    file.write('Connection from the context manager...\n')
    file.write('Second connection from the context manager...')
# file.write('something else...')
print('end')