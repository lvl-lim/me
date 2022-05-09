"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

# I think it will declare a variable called some_words
# and it'll put a list of strings into it
some_words = ['what', 'does', 'this', 'line', 'do', '?']

# I think it will print one word in the list at a time until the list is finished
for word in some_words:
    print(word) #it printed "what" followed by "does" etc until all the words in the list until the list is exhausted

# Same outcome as above
for x in some_words:
    print(x) #it printed the same outcome as above


# I think this will print the entire string as is like this: ['what', 'does', 'this', 'line', 'do', '?']
print(some_words) #it printed ['what', 'does', 'this', 'line', 'do', '?']

# len defines number of items in the list. No of items in the list >3, hence, this statement is true. 
# it will print "some_words contains more than 3 words"
if len(some_words) > 3:
    print('some_words contains more than 3 words') # it printed "some_words contains more than 3 words"

def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())

usefulFunction()
