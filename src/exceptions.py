import sys

__author__ = 'ravo'

'''
examples taken from:
http://docs.python.org/2/tutorial/errors.html
'''
# try, except (catch) , finally, pass
def err():
    while True:
     try:
         x = int(raw_input("Please enter a number: "))
         x = x%0
         break
     except ValueError:
         print "Oops!  That was no valid number.  Try again.. msg: %s, args: %r, obj: %r" % (ValueError.message, type(ValueError.args), ValueError)
     except:
         print "some error..pass"
         pass
     finally:
         print "exiting try/catch block.. finally!"



# raise exception & format function
def raiseException():
    try:
        f = open('myfile.txt')
        s = f.readline()
        i = int(s.strip())
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise

# try, except - else demo
def tryExcept():
    for arg in sys.argv[1:]:
        try:
            f = open(arg, 'r')
        except IOError:
            print 'cannot open', arg
        else:
            print arg, 'has', len(f.readlines()), 'lines'
            f.close()
            
# print exception details

def printException():
    try:
        raise Exception('spam', 'eggs')
    except Exception as inst:
        print type(inst)     # the exception instance
        print inst.args      # arguments stored in .args
        print inst           # __str__ allows args to printed directly
        x, y = inst.args
        print 'x =', x
        print 'y =', y

# this is cool stuff - you'll know if you come from Java bg
def implicitThrow():
    x = 1/0

try:
    implicitThrow()
except ZeroDivisionError as detail:
    print 'Handling run-time error:', detail

# tryExcept()
#printException()

#raiseException()
# passException()