import argparse
import datetime
import json
from object.account import *
import sys

arr = ['a','b','c','d','e','f']
index = 3

for i, v in enumerate(arr):
    if i < index:
        continue
    print(i, v)
