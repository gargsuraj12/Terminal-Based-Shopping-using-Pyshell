import os
import difflib

def myDiff(file1, file2):
    if os.path.exists(file1) == False:
        print(file1, " does not exist")
        return
    if os.path.exists(file2) == False:
        print(file2, " does not exist")
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

file1 = "demo.txt"
file2 = "demo2.txt"

myDiff(file1, file2)