#!/usr/bin/env python

import argparse
import os
import sys
import time

def PushBack(notes):
    currentDir =  os.getcwd()
    fileName = currentDir+'/.bkeep'
    date = time.strftime("%x")

    try:
        with open(fileName, "a") as file:           
            file.write('\n' + date +": " + notes)
            file.close()
    except:
        file = open(fileName, 'w')
        file.write(notes)
        file.close()

if __name__=='__main__':
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--notes', 
                        help='Push back note',
                        nargs="*")
    args = parser.parse_args()
    
    if len(args.notes) ==0:
        parser.print_help()
        sys.exit(1)
                
    for note in args.notes:
        PushBack(note)

    sys.exit(0)
