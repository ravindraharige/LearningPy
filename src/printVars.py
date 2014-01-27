# Some basic exercises on printing variables - examples are taken from
# Learning Python The Hard Way - http://learnpythonthehardway.org/book/


def ex5():
    my_name = 'Ravi'
    my_age = 27 # not a lie
    my_height = 74 # inches
    my_weight = 180 # lbs
    my_eyes = 'Brown'
    my_teeth = 'White'
    my_hair = 'Black'

    print "Let's talk about %s." % my_name
    print "He's %d inches tall." % my_height
    print "He's %d pounds heavy." % my_weight
    print "Actually that's not too heavy."
    print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
    print "His teeth are usually %s depending on the coffee." % my_teeth

    # this line is tricky, try to get it exactly right
    print "If I add %d, %d, and %d I get %d." % (
        my_age, my_height, my_weight, my_age + my_height + my_weight)

# ex. 6
# this is about %r Vs. %s -
def ex6():
    x = "You are %d times funnier than joe" % 10
    print "1. I said: %r." % x
    print "2. I said %s." % x
    # error
    # print "3. I said %%s.but here's the str: " % str(x)
    print "3. here's it: %%s symbol but str is= %s" % x

    print "4. here's it: %%s symbol but str is= %s", x

    print "5. here's it: %%s symbol but str is= %s"+x
    hilarious = False
    joke_evaluation = "Isn't that joke so funny?! %r"

    print joke_evaluation % hilarious

    w = "This is the left side of..."
    e = "a string with a right side."

    print w + e

# ex.7
def ex7():
    end1 = "hell"
    end2 = "o"
    end3 = "Wor"
    end4 = "ld"

    # watch that comma at the end.  try removing it to see what happens
    print end1 + end2,
    print end3 + end4

#ex.8

def ex8():
    formatter = "%r %r %r %r"

    print formatter % (1, 2, 3, 4)
    print formatter % ("one", "two", "three", "four")
    print formatter % (True, False, False, True)
    print formatter % (formatter, formatter, formatter, formatter)
    print formatter % (
        "I had this thing.",
        "That you could type up right.",
        "But it didn't sing.",
        "So I said goodnight."
    )

def ex9():
    # multi line string print

    print """
    There's something going on here.
    With the three double-quotes.
    We'll be able to type as much as we like.
    Even 4 lines if we want, or 5, or 6.
    """

# Console inputs -- notice the comma after print string (and)
# new variable on new line - you can't put that var = prompt() in same line as print
def ex11():
    print "How old are you?",
    age = raw_input()
    print "How tall are you?",
    height = raw_input()
    print "How much do you weigh?",
    weight = raw_input()

    # print "How much do you weigh?", weight = raw_input() -- ERROR!

    print "So, you're %r old, %r tall and %r heavy." % (
        age, height, weight)


# Console inputs!
def ex12():
    age = raw_input("How old are you? ")
    height = raw_input("How tall are you? ")
    weight = raw_input("How much do you weigh? ")

    print "So, you're %r old, %r tall and %r heavy." % (
        age, height, weight)

