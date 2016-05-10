#!/usr/bin/env python

import argparse
import logging 
import os
import sys
import time

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)
log = logging.getLogger(__name__)

def PushBack(notes, args):
    currentDir =  os.getcwd()
    fileName = currentDir+'/.bkeep'
    date = time.strftime("%x")

    if args.findDate: 
        with open(fileName, "r") as f:
            contents = f.readlines()
            f.close()
            for i, line in enumerate(contents):
                if notes in line:
                    for l in contents[i:i+3]:  sys.exit("Found contents %s" %l)
                else:
                    sys.exit("Not found")

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
    parser.add_argument('-f', '--findDate', 
                        help="Find dates referring to note pushed",
                        action='store_true')
                       
    args = parser.parse_args()
    
    if not len(sys.argv) > 1:
        log.exception("Cannot find any input")
        sys.exit(0)

    if len(args.notes)==0:
        parser.print_help()
                
    for note in args.notes:
        PushBack(note, args)

    sys.exit(0)
