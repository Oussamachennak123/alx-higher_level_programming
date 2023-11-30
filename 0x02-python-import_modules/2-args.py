#!/usr/bin/python3
if __name__ == "__main__" :
    """Print the number and list of arguments"""
    from sys import argv
    argument = len(argv)
    if argument == 1 :
        print ('0 arguments.')
    elif argument == 2 :
        print ('1 argument: ')
    else:
        print("{} arguments: ".format(argument - 1))
    for i in range(argument - 1):
        print("{}: {}".format(i + 1, argv[i+ 1]))
