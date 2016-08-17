#!/usr/bin/env python

import argparse
import logging
import os
import sys

def FindBook(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
