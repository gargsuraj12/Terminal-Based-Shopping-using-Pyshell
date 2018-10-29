#!/usr/bin/python3

import os, sys
from stat import *
import stat
from itertools import islice
import time
from os import path

def head(fname, count):
    if isinstance(fname, str) == False:
        print("Please provide file name in a valid format..")
        return
    if isinstance(count, int) == False:
        print("Please provide count in a valid format..")
        return
    if os.path.exists(fname) == False:
        print("File does not exist..")
        return    
    try:
        f = open(fname, "rt")
        if count == 0:
            count = 10
        while count:
            print(f.readline())
            count -= 1
        f.close()
    except IOError:
        print("File is not accessible")
        
def tail(fname, count):
    if isinstance(fname, str) == False:
        print("Please provide file name in a valid format..")
        return
    if isinstance(count, int) == False:
        print("Please provide count in a valid format..")
        return
    if os.path.exists(fname) == False:
        print("File does not exist..")
        return  
    try:
        f = open(fname, "rt")
        if count == 0:
            count = 10
        lineCount = 1
        for ch in f:
            if ch[-1] == "\n":
                lineCount += 1
        cur = lineCount-count
        while cur < lineCount:
            f.seek(0,0)               
            line = next(islice(f, cur, cur+1))
            print (line)
            cur += 1  
        f.close()
    except IOError:
        print("File is not accessible")        
        
def grep(fname, pattern):
    if isinstance(fname, str) == False:
        print("Please provide file name in a valid format..")
        return
    if isinstance(pattern, str) == False:
        print("Please provide pattern in a valid format..")
        return
    if os.path.exists(fname) == False:
        print("File does not exist..")
        return    
    try:
        f = open(fname)
        found = False
        for line in f:
            if pattern in line:
                print(line)
                found = True
        if found == False:
            print("Pattern not found in file..")        
        f.close()
    except IOError:
        print("File is not accessible..")    

def touch(fname):
    if isinstance(fname, str) == False:
        print("Please provide file name in a valid format..")
        return
    if os.path.exists(fname):
        ts = time.time()
        os.utime(fname, (ts, ts))
    else:
        f = open(fname, "w")
        f.close()
        print("File created..")

def pwd():
    try:
        print(os.getcwd())
    except OSError:
        print("OSERROR: Unable to get the current working directory")    

#works for absolute path, relative path and ~ path
def changeDir(path):
    if isinstance(path, str) == False:
        print("Path format error..")
        return
    dest = ""
    if path[0] == "~":
        dest += "/home/suraj"
        path = path[1:]
        dest = dest+path
    elif path[0] == "/":
        dest = path
    else:
        dest = os.getcwd()
        dest += "/"
        dest += path    
    try:
        print("path before cd is: " , os.getcwd())
        os.chdir(dest)
        print ("path after cd is: " , os.getcwd())
    except OSError:
        print("dest path is not valid..")    

#Replaces all occrences of the pattern with the new patttern
def sed(fname, pattern, newPattern):
    if os.path.exists(fname) == False:
        print("File does not exist..")
        return
    try:
        f = open(fname, "a+")
        found = False
        for line in f:
            if pattern in line:
                found = True
            line = line.replace(pattern, newPattern, -1)
            print(line)
        if found == False:
            print("\nFrom App: Pattern not found in file..")    
        f.close()
    except IOError:
        print("File is not accessible..")

def list(path):
    if path=="":
        path = os.getcwd()
    try:
        dirEntries = os.scandir(path)
        for entry in dirEntries:
            info = entry.stat()
            # print(info)
            print(("-","d")[S_ISDIR(info[ST_MODE])], end="")
            print(("-","r")[bool(info[ST_MODE] & stat.S_IRUSR)], end="")
            print(("-","w")[bool(info[ST_MODE] & stat.S_IWUSR)], end="")
            print(("-","x")[bool(info[ST_MODE] & stat.S_IXUSR)], end="")
            print(("-","r")[bool(info[ST_MODE] & stat.S_IRGRP)], end="")
            print(("-","w")[bool(info[ST_MODE] & stat.S_IWGRP)], end="")
            print(("-","x")[bool(info[ST_MODE] & stat.S_IXGRP)], end="")
            print(("-","r")[bool(info[ST_MODE] & stat.S_IROTH)], end="")
            print(("-","w")[bool(info[ST_MODE] & stat.S_IWOTH)], end="")
            print(("-","x")[bool(info[ST_MODE] & stat.S_IXOTH)], end="")

            print("\t",info[ST_SIZE],"\t", entry.name, end="")
            print ("\t\t", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(info[ST_MTIME])))
    except OSError:
        print("Unable to read the given directory..")

fname = "demo.txt"
path = "/home/suraj/Desktop/"
# head(fname, 0)
# tail(fname, 2)
# grep(fname, "is")
# touch(fname)
# pwd()
# changeDir("~/Desktop")
# sed(fname, "the", "theeeeeee")
list(path)

# while True:
#     print ("Enter the command: ")
    