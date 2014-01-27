__author__ = 'ravo'

# If-else stuff
def ex30():
    people = 30
    cars = 40
    buses = 15

    if cars > people:
        print "We should take the cars."
    elif cars < people:
        print "We should not take the cars."
    else:
        print "We can't decide."

# for loops & appending to lists
def ex32():
    the_count = [1, 2, 3, 4, 5]
    fruits = ['apples', 'oranges', 'pears', 'apricots']
    change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

    # this first kind of for-loop goes through a list
    for number in the_count:
        print "This is count %r" % number

    # we can also build lists, first start with an empty one
    elements = []

    # then use the range function to do 0 to 5 counts
    for i in range(0, 6):
        print "Adding %d to the list." % i
        # append is a function that lists understand
        elements.append(i)

    # now we can print them out too
    for i in elements:
        print "Element was: %d" % i

# While loops
def ex33():
    i = 0
    numbers = []

    while i < 6:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i


    print "The numbers: "


# If condition with and (&&) or (||)
def ex35():
    print "This room is full of gold.  How much do you take?"

    next = raw_input("> ")


    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        how_much = int(next)
        # print("Man, learn to type a number.")
        # exit(0)

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        print("You greedy bastard!")

ex35()