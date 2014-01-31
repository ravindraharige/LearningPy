__author__ = 'ravo'

class Parent(object):

    def implicit(self):
        print "PARENT implicit()"

class Child(Parent):
    # pass
    def implicit(self):
        print "CHILD, BEFORE PARENT implicit()"
        super(Child, self).implicit()
        print "CHILD, AFTER PARENT implicit()"

dad = Parent()
son = Child()

dad.implicit()
son.implicit()