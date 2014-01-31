__author__ = 'ravo'

class demo:
    x = 0
    def __init__(self):
        print "in constructor"

    def assign(self):
        print("@assign")
        print(self.x)

    def __str__(self):
        return "I'm demo"

class fdemo(demo):
    def __init__(self):
        self.x = 90
        print "fdemo"

# d = fdemo()
# d.assign()
# pyIdioms.main()
# print(d)

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        print type(self.lyrics)
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

