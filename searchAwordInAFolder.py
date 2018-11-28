import os
import sys
import platform

def searchAWord(filename, old_str, sysstr):
    old_str = old_str.replace('SPACE', ' ')
    file_data = open("{}.codereview".format(old_str), 'a+')
    WROTEFILENAME = False

    if(sysstr =="Windows"):
        with open(filename, "r", encoding='gb18030', errors='ignore') as f:
            lineCounter = 0
            for line in f:
                lineCounter += 1
                if old_str in line:
                    if not WROTEFILENAME: 
                        file_data.write("e "+filename+'\n')
                        WROTEFILENAME = True
                    file_data.write("\t"+str(lineCounter) + ": " + line)
            if WROTEFILENAME: file_data.write('\n')

    elif(sysstr[0] == "D"): # macbook
        with open(filename, "r") as f:
            lineCounter = 0
            for line in f:
                lineCounter += 1
                if old_str in line:
                    if not WROTEFILENAME: 
                        file_data.write("e "+filename+'\n')
                        WROTEFILENAME = True
                    file_data.write("\t"+str(lineCounter) + ": " + line)
            if WROTEFILENAME: file_data.write('\n')

    file_data.close()

def traverseFolder(search_folder,searchStr):
    sysstr = platform.system()
    for dirpath, dirnames, filenames in os.walk(search_folder): # using
        if 'codereview' in dirpath:
            continue
        for filename in filenames:
            if '.js' in filename or '.java' in filename:
                searchAWord(os.path.join(dirpath,filename), searchStr, sysstr)

traverseFolder('.', sys.argv[1])
