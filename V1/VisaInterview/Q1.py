#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'slowestKey' function below.
#
# The function is expected to return a CHARACTER.
# The function accepts 2D_INTEGER_ARRAY keyTimes as parameter.
#

# a = 0, b = 1, z = 25
# Times pressed
# [Character, times_pressed]
# [[0,2], [1,5], [0,9], [2,15]]
# keyTimes[i][0] ... ascii a-z
letter_dict = {'a':0,'b':1,'c':2, 'd':3, 'e':4,'f':5,'g':6,'h':7,
'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
letter_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def slowestKey(keyTimes):
    start_time = 0
    longest = 0
    char_key = ''
    for i in range(0, len(keyTimes)):
        cur_time = keyTimes[i][1] - start_time
        cur_char = letter_list[keyTimes[i][0]]
        if cur_time > longest:
            longest = cur_time
            char_key = cur_char
        start_time = keyTimes[i][1]
    return char_key
    # works in my IDE?





    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    keyTimes_rows = int(input().strip())
    keyTimes_columns = int(input().strip())

    keyTimes = []

    for _ in range(keyTimes_rows):
        keyTimes.append(list(map(int, input().rstrip().split())))

    result = slowestKey(keyTimes)

    fptr.write(str(result) + '\n')

    fptr.close()
