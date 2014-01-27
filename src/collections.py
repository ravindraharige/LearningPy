__author__ = 'ravo'

# ex38 - list append, pop(), negative index, join function!
def listOps():
    ten_things = "Apples Oranges Crows Telephone Light Sugar"

    print "Wait there's not 10 things in that list, let's fix that."

    stuff = ten_things.split(' ')
    more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

    while len(stuff) != 10:
        next_one = more_stuff.pop()
        print "Adding: ", next_one
        stuff.append(next_one)
        print "There's %d items now." % len(stuff)

    print "There we go: ", stuff

    print "Let's do some things with stuff."

    print stuff[1]
    print stuff[-1] # whoa! fancy
    print stuff.pop()
    print ' '.join(stuff) # what? cool!
    print '#'.join(stuff[3:5]) # super stellar!


# ex39 - dictionaries - the python hashmaps
def basicDisc():
    stuff = {'name': 'Zed', 'age': 36, 'height': 6*12+2}
    print stuff['name']
    print stuff['age']
    print stuff['height']

    # assign new keys, value pair
    stuff['city'] = "San Francisco"
    print stuff['city']

    # add keys to dict
    stuff[1] = "Wow"
    stuff[2] = "Neato"
    print stuff[1]
    print stuff[2]
    print stuff

    # delete keys from dict
    del stuff['city']
    del stuff[1]
    del stuff[2]
    print stuff

# ex39b - test on dictionary
def dictTest():
    # create a mapping of state to abbreviation
    states = {
        'Oregon': 'OR',
        'Florida': 'FL',
        'California': 'CA',
        'New York': 'NY',
        'Michigan': 'MI'
    }

    # create a basic set of states and some cities in them
    cities = {
        'CA': 'San Francisco',
        'MI': 'Detroit',
        'FL': 'Jacksonville'
    }

    # add some more cities
    cities['NY'] = 'New York'
    cities['OR'] = 'Portland'

    # print out some cities
    print '-' * 10
    print "NY State has: ", cities['NY']
    print "OR State has: ", cities['OR']

    # print some states
    print '-' * 10
    print "Michigan's abbreviation is: ", states['Michigan']
    print "Florida's abbreviation is: ", states['Florida']

    # do it by using the state then cities dict
    print '-' * 10
    print "Michigan has: ", cities[states['Michigan']]
    print "Florida has: ", cities[states['Florida']]

    # print every state abbreviation
    print '-' * 10
    for state, abbrev in states.items():
        print "%s is abbreviated %s" % (state, abbrev)

    # print every city in state
    print '-' * 10
    for abbrev, city in cities.items():
        print "%s has the city %s" % (abbrev, city)

    # now do both at the same time
    print '-' * 10
    for state, abbrev in states.items():
        print "%s state is abbreviated %s and has city %s" % (
            state, abbrev, cities[abbrev])

    print '-' * 10
    # safely get a abbreviation by state that might not be there
    state = states.get('Texas', None)

    if not state:
        print "Sorry, no Texas."

    # get a city with a default value
    city = cities.get('TX', 'Does Not Exist')
    print "The city for the state 'TX' is: %s" % city

# basicDisc()
dictTest()