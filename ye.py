#!/bin/python
#26 January 2016 - Kuan-Lin Huang @ WashU - 
 
import sys
import getopt

def main():
    def usage():
        print """
    ye.py : why do I exist?

    USAGE: ye.py [-h] <filename>
     -h    print this message
     <filename>    input file
        """

    #use getopt to get inputs
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'h') #:after option meaning required arguments
    except getopt.GetoptError:
        print "ye.py <inputFile>"

    for opt, arg in opts: #store the input options
        if opt == '-h': # h means user needs help
            usage(); sys.exit()

    if len(args) < 1:
        usage(); sys.exit("input file missing")

    #open input file
    try:
        f = open(args[0],"r")
    except IOError:
        print("File , args[0], does not exist!")

    #read input file
    for line in f:
        line=line.strip("\t")
        F = line.split()

    f.close()

if __name__ == "__main__":
    main()
