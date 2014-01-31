__author__ = 'ravo'

#safehammad.com/downloads/python-idioms-2014-01-16.pdf

def main():
    print('Doing stuff in module', __name__)


if __name__ == '__main__':
    print('Executed from the command line')
    main()
