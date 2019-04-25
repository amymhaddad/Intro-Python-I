"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

with open("foo.txt", mode="r", encoding="utf-8") as f_object:
    for content in f_object:
        print(content.strip())

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

with open('bar.txt', mode = 'wt', encoding = 'utf-8') as f_object:
    f_object.write("My name is Amy.\n")
    f_object.write("The month is April.\n")
    f_object.write("The day is Thursday.")

with open('bar.txt', mode = 'rt', encoding = 'utf-8') as f_object:
    for line in f_object:
        print(line.strip())