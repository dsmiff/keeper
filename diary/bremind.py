#!/usr/bin/env python

import argparse
import logging 
import os
import sys
import time

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)
log = logging.getLogger(__name__)

def Remind(notes, args):
    currentDir =  os.getcwd()
    
    if args.pushHome:
        if len(args.pushHome) == 1: currentDir = args.pushHome[0]
        else: pass
        
    fileName = currentDir+'/.bremind'

    if args.specify: accuracy = "%c"
    else: accuracy = "%x"

    date = time.strftime(accuracy)
    
    if args.chooseDate: 
        with open(fileName) as f:
            for line in iter(f):
                if notes in line:
                    sys.exit("Found contents %s" %line)
                else:
                    continue

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
    parser.add_argument('-f', '--chooseDate', 
                        help="Choose dates referring to note pushed",
                        action='store_true')
    parser.add_argument('-home', '--pushHome',
                        help='Push note to home directory',
                        nargs="*")
    parser.add_argument('-s', '--specify',
                        help='Specific time',
                        action='store_true',
                        default=True)
                       
    args = parser.parse_args()
    
    if not len(sys.argv) > 1:
        log.exception("Cannot find any input")
        sys.exit(0)

    if len(args.notes)==0:
        parser.print_help()
                
    for note in args.notes:
        Remind(note, args)

    sys.exit(0)
