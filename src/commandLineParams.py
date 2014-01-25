__author__ = 'ravo'

from sys import argv

# if len(argv)>4:
#     print "more args - can't pack it"
#     exit(0)
# else:
#     if len(argv)<4:
#         print "less than 3 args - can't pack it"

# print type of variable
print type(argv)

# so called 'unpacking!'
script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

