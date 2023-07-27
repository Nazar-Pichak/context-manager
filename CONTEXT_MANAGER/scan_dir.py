# Scanning directories with the os module and context manager statemante.

import os

with os.scandir('.') as entries:
    for entry in entries:
        print(entry.name, '->', entry.stat().st_size, 'bytes')

print()

with os.scandir('..') as entries:
    for entry in entries:
        print(entry.name, '->', entry.stat().st_size, 'bytes')

