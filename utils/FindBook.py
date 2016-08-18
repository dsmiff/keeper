# Dominic Smith <dosmith@cern.ch>
#!/usr/bin/env python

import argparse
import logging
import os
import sys

##__________________________________________________||
class BookUtils(object):
    def __init__(self):
        pass

    @staticmethod
    def FindBook(name, path):
        for root, dirs, files in os.walk(path):
            if name in files:
                return os.path.join(root, name)

    @staticmethod
    def touch(path):
        with open(path, 'a'):
            os.utime(path, None)

    @staticmethod
    def readlines(name,path):
        fileName = FindBook(name,path)
        if fileName:
            fd = open(fileName)
            i = 0
            spaces = 0
            tabs = 0
            for i, line in enumerate(fd):
                spaces += line.count(' ')
                tabs += line.count('\t')
            fd.close()
            return spaces, tabs, i+1
        else:
            print("File not found")
