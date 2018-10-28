import os
import sys
import platform

def searchAWord(filename, old_str):
    file_data = open("{}.codereview".format(old_str), 'a+')
    WROTEFILENAME = False

    sysstr = platform.system()
    if(sysstr =="Windows"):
        with open(filename, "r", encoding='gb18030', errors='ignore') as f:
            lineCounter = 0
            for line in f:
                lineCounter += 1
                if old_str in line:
                    if not WROTEFILENAME: 
                        file_data.write("#e "+filename+'\n')
                        WROTEFILENAME = True
                    file_data.write(str(lineCounter) + ": " + line)
        file_data.write('\n')
        file_data.close()

    elif(sysstr[0] == "D"): # macbook
        with open(filename, "r") as f:
            lineCounter = 0
            for line in f:
                lineCounter += 1
                if old_str in line:
                    if not WROTEFILENAME: 
                        file_data.write("#e "+filename+'\n')
                        WROTEFILENAME = True
                    file_data.write(str(lineCounter) + ": " + line)
        file_data.write('\n')
        file_data.close()

def traverseFolder(search_folder,searchStr):
    for dirpath, dirnames, filenames in os.walk(search_folder): # using
        for filename in filenames:
            if '.js' in filename or '.java' in filename:
                searchAWord(os.path.join(dirpath,filename), searchStr)

traverseFolder('.', sys.argv[1])
