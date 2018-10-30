#!/usr/bin/python3

import os, sys
from stat import *
import stat
from itertools import islice
import time
from os import path
import re
import difflib

def head(fname, count):
    if os.path.exists(fname) == False:
        print("File '",fname, "' does not exist..")
        return    
    try:
        f = open(fname, "r")
        if count == 0:
            count = 10
        while count:
            print(f.readline())
            count -= 1
    except IOError:
        print("File is not accessible")
    finally:
        f.close()

#Needs to be changed 
def tail(fname, count):
    if os.path.exists(fname) == False:
        print("File '",fname, "' does not exist..")
        return  
    try:
        f = open(fname, "r")
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
    except IOError:
        print("File is not accessible")
    finally:
        f.close()            

def grep(pattern, fname):
    if os.path.exists(fname) == False:
        print("File '",fname, "' does not exist..")
        return    
    try:
        pattern = re.compile(pattern)
        f = open(fname, "r")
        found = False
        for line in f:
            searchRes = re.search(pattern, line, re.I)
            if searchRes:
                print(line)
                found = True
        if found == False:
            print("Pattern not found in file..")
    except IOError:
        print("File is not accessible..")
    finally:
        f.close()        

def touch(fname):
    if os.path.exists(fname):
        ts = time.time()
        os.utime(fname, (ts, ts))
    else:
        try:
            f = open(fname, "w")
            print("File '",fname, "' created..")
        except IOError:
            print("Unable to open file")
        finally:
            f.close()        

def pwd():
    try:
        print(os.getcwd())
    except OSError:
        print("OSERROR: Unable to get the current working directory")    

#works for absolute path, relative path and ~ path
def changeDir(dest):    
    try:
        print("path before cd is: " , os.getcwd())
        os.chdir(dest)
        print ("path after cd is: " , os.getcwd())
    except OSError:
        print("dest path is not valid..")    

#Replaces all occrences of the pattern with the new patttern
def sed(pattern, newPattern, fname):
    if os.path.exists(fname) == False:
        print("File '",fname, "' does not exist..")
        return
    try:
        pattern = re.compile(pattern)
        f = open(fname, "r")
        found = False
        for line in f:
            searchRes = re.search(pattern, line) #, re.I|re.M)
            # if pattern in line:
            if searchRes:
                found = True
                # line = line.replace(pattern, newPattern, -1)
            line = re.sub(pattern, newPattern, line)
            print(line)
        if found == False:
            print("\nFrom App: Pattern not found in file..")
    except IOError:
        print("File is not accessible..")
    finally:
        f.close()    

def listNames(path):
    try:
        for name in os.listdir(path):
            if name.startswith("."):
                continue
            print(name,end="")
            if os.path.isdir(name):
                print("/",end="")
            print()
    except OSError:
        print("SystemError: Unable to read the given directory!!")    

def listAll(path):
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

            print ("\t", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(info[ST_MTIME])),end="")
            print("\t",info[ST_SIZE],"\t", entry.name)
    except OSError:
        print("SystemError: Unable to read the given directory..")

def tr(toReplace, withReplace):
    while True:
        string = input("Enter text: ")
        for char in string:
            index = toReplace.find(char)
            if index != -1:
                char = withReplace[index]
            print(char, end="")    
        print("")
        isExit = input("Do you want to terminate (y/n):")
        if isExit.lower() == "y":
            break
    print("\033[H\033[J")

def myDiff(file1, file2):
    if os.path.exists(file1) == False:
        print("File '",file1, "' does not exist..")
        return
    if os.path.exists(file2) == False:
        print("File '",file2, "' does not exist..")
        return    
    try: 
        f1 = open(file1, "r") 
        f2 = open(file2, "r")
        lines1 = f1.readlines()
        lines2 = f2.readlines()

        d = difflib.Differ()
        diff = d.compare(lines1, lines2)
        print("\n".join(diff))
    except IOError:
        print("Unable to read one of the files")
    finally:
        f1.close()
        f2.close()    

def headHandler(commandList):
    length = len(commandList)
    if length < 2:
        print("Insufficient Arguements..!!")
        return
    if length >= 4:
        print("Too many arguements..")
        return

    if length == 2:
        return head(commandList[1], 0)
    arg1 = ""
    arg1 = commandList[1]
    if arg1[0] != '-':
        print("Flag should start with a hyphon")
        return
    try:
        count = int(arg1[1:])    
        head(commandList[2], count)
    except ValueError:
        print("Please enter a valid flag containing a number")

def tailHandler(commandList):
    length = len(commandList)
    if length < 2:
        print("Insufficient Arguements..!!")
        return
    if length >= 4:
        print("Too many arguements..")
        return

    if length == 2:
        return tail(commandList[1], 0)
    arg1 = ""
    arg1 = commandList[1]
    if arg1[0] != '-':
        print("Flag should start with a hyphon")
        return
    try:
        count = int(arg1[1:])    
        tail(commandList[2], count)
    except ValueError:
        print("Please enter a valid flag containing a number")    

# Basic functionality supported
def grepHandler(commandList):
    length = len(commandList)
    if length < 3:
        print("Insufficient Arguements..!!")
        return
    if length >= 4:
        print("Too many arguements..")
        return
    grep(commandList[1], commandList[2])    

def pwdHandler(commandList):
    length = len(commandList)
    if length >= 2:
        print("Too many arguements..")
        return
    pwd()    

def touchHandler(commandList):
    length = len(commandList)
    if length < 2:
        print("Insufficient Arguements..!!")
        return
    if length >= 3:
        print("Too many arguements..")
        return
    touch(commandList[1])    

def cdHandler(commandList):
    length = len(commandList)
    if length < 2:
        print("Insufficient Arguements..!!")
        return
    if length >= 3:
        print("Too many arguements..")
        return
    dest = ""
    path = commandList[1]
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
    changeDir(dest)

def sedHandler(commandList):
    length = len(commandList)
    if length < 4:
        print("Insufficient Arguements..!!")
        return
    if length >= 5:
        print("Too many arguements..!!")
        return
    if not commandList[1].startswith("'") or not commandList[1].endswith("'"):
        print("Pattern to be replaced must be enclosed within single quotes..")
        return
    if not commandList[2].startswith("'") or not commandList[2].endswith("'"):
        print("New pattern must be enclosed within single quotes..")
        return  
    sed(commandList[1][1:-1], commandList[2][1:-1], commandList[3])

# Supports only -l
def lsHandler(commandList):
    length = len(commandList)
    if length > 3:
        print("Too many arguements..")
        return
    path = ""
    if length == 1:
        path = os.getcwd()
        return listNames(path)
    if length == 2:
        path = commandList[1]
        return listNames(path)    
    if length == 3:
        flags = ""
        flags = commandList[1]
        if not flags.startswith("-"):
            print("Flag must start with a hyphen")
            return
        flags = flags[1:]
        if len(flags) > 1:
            print("Application support only one flag..")
            return
        if flags != "l":
            print("Application support only -l flag..")
            return    
    path = commandList[2]    
    return listAll(path)

def trHandler(commandList):
    length = len(commandList)
    if length < 3:
        print("Insufficient Arguements..!!")
        return
    if length >= 4:
        print("Too many arguements..!!")
        return
    if len(commandList[1]) != len(commandList[2]):
        print("Length of replaced and replacing pattern must be same")
        return    
    tr(commandList[1], commandList[2])

def diffHandler(commandList):
    length = len(commandList)
    if length < 3:
        print("Insufficient Arguements..!!")
        return
    if length >= 4:
        print("Too many arguements..!!")
        return    
    myDiff(commandList[1], commandList[2])


# Execution starts from here
print("\033[H\033[J")
entered = ""
while True:
    entered = input("Enter your Command here: ")
    commandList = entered.split(" ")
    command = commandList[0]
    if command == "head":
        headHandler(commandList)
    elif command == "tail":
        tailHandler(commandList)
    elif command == "grep":
        grepHandler(commandList)
    elif command == "touch":
        touchHandler(commandList)
    elif command == "pwd":
        pwdHandler(commandList)
    elif command == "cd":
        cdHandler(commandList)
    elif command == "ls":
        lsHandler(commandList)    
    elif command == "sed":
        sedHandler(commandList)
    elif command == "tr":
        trHandler(commandList)
    elif command == "diff":
        diffHandler(commandList)
    elif command == "clear":
        print("\033[H\033[J")    
    elif command == "exit":
        break
    else:
        print("Invalid command!!")    

print("\033[H\033[J")
# Execution ends here