__author__ = 'ravo'

#ex.18
def takeAnyNoOfArgs(*args):
    print "No. of args: ", len(args)
    print "type: ", type(args)

takeAnyNoOfArgs('hi', 'bye')