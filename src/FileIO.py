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

def classicWriteFile():
    data = "blah blah blah blah"
    text_file = open("../data/Output.txt", "w")
    text_file.write("@classicWriteFile data: %s"%data)
    text_file.close()

def writeFile():
    data = "blah blah blah blah"
    with open("../data/Output.txt", "w") as text_file:
        text_file.write("@writeFile data: %s"%data)

# readFileLineByLine()
# readFileIntoList()
# readFileIntoString()
# classicWriteFile()
writeFile()