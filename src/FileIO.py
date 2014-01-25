__author__ = 'ravo'

text_file = '../data/dummy.txt'

# Read a file line by line;

def readFileLineByLine():
    with open (text_file) as f:
        for line in f:
            print(line.rstrip('\n'))

def readFileIntoList():
    with open(text_file) as f:
        lines = f.read().splitlines()

    print "total lines read: ", len(lines)

def readFileIntoString():
    data = ""
    data2 = ""
    with open (text_file, "r") as f:
        # data = f.read().replace('\n', '') # Without newline char
        data2 = f.read()

    print "content of file is: \n",data2

# readFileLineByLine()
# readFileIntoList()
readFileIntoString()