# The most simple way to write some data in the file.
# The main action it's remember to call method close() to close file.
# Method close() helps to avoid a big quantity the opened files if occurs some error..
# Otherwise we will get an error 'TO MANY OPENE FILES'

text_list = ['The first line of text', 'The second line of text', 'The third line of thext']
text_dict = {4: 'The fourth line of text', 5: 'The fifth line of text', 6: 'The sixth line of text'}

file = open('store.txt', 'w')

for line in text_list:
    file.write(line + '\n')

for line in text_dict.values():
    file.write(line + '\n')

file.write('The seventh line of text\n')
file.write('And the End of the text...')
file.close()
