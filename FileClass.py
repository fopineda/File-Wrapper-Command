## Class wrapper for Python file open(...) read write functionality
## Class will modify file
import re
import sys

class File():
    def __init__(self, path):
        self.path = path

    # Description: removes all instances of the "\n" from the file
    def removeAllNewLines(self):
        with open(self.path, 'r+') as fileReadable:
            contents = fileReadable.read()
            newContents = contents.replace('\n', '')
        with open(self.path, 'w') as fileWritable:
            fileWritable.write(newContents)

    # Description: removes first occurrence of keyword from file
    def removeWord(self, keyword):
        with open(self.path, 'r+') as fileReadable:
            contents = fileReadable.read()
            newContents = contents.lower().replace(keyword.lower(), '', 1)
        with open(self.path, 'w') as fileWritable:
            fileWritable.write(newContents)

    # Description: removes all occurrences of keyword from file
    def removeAllWords(self, keyword):
        with open(self.path, 'r+') as fileReadable:
            contents = fileReadable.read()
            newContents = contents.lower().replace(keyword.lower(), '')
        with open(self.path, 'w') as fileWritable:
            fileWritable.write(newContents)
        
    # Description: removes everything in file
    def clearFile(self):
        with open(self.path, "w") as fileCleared:
            pass

    # Description: adds word to beginning
    def addStringAtBeginning(self, additionalString):
        with open(self.path, "r+") as fileReadableWritable:
            fileReadableWritable.write(additionalString)

    # Description: adds word to end of the file
    def addStringAtEnd(self, additionalString):
        with open(self.path, "a") as fileAppendable:
            fileAppendable.write(additionalString)

    # Description: returns path variable
    def getPath(self):
        return self.path

    # Description: sets path variable
    def setPath(self, path):
        self.path = path

    # Description: search for keyward and gives you line number and word number it is located at
    def search(self, keyword):
        with open(self.path, "r+") as fileReadableWritable:
            pattern = keyword.lower()+'+'
            for numLine,line in enumerate(fileReadableWritable, start=1):
                for numWord, word in enumerate(line.split(), start=1):
                    if (re.match(pattern, word.lower())): 
                        print("line: {}, word: {}".format(numLine, numWord))

    # Description: prints entire file
    def printFile(self):
        with open(self.path, "r") as fileReadable:
            print(fileReadable.read())

    # Description: prints help menu for command
    def printHelp(self):
        helpString = ''' 
NAME
    FileClass.py -- Wrapper for the python open file functionality.

SYNOPSIS
    python3 FileClass.py [file] [-h|-s [string]|-p|-ranl|-raw [string]|-rw [string]|-cf|-asb [string]|-ase [string]]

DESCRIPTION
    Opens a file (programmatically) and allows you view, edit, search, and delete the file.
    Be advised, you can only use one flag at time

            Options:
                -h      prints help plus examples text
                -s      searches file and display occurrences and line/word #
                -p      prints entire file onto display
                -ranl   removes all new lines from file
                -raw    removes all instances of a specified keyword
                -rw     removes single instance of a specified keyword
                -cf     clears entire file
                -asb    adds string to beginning
                -ase    adds string to end 
EXAMPLES
    python3 FileClass.py lorem.txt -h
        runs printHelp() function from File class
    python3 FileClass.py lorem.txt -s sit
        runs search(...) function from File class
        requires extra argument that is used for search keyword, if not provided it throws an error
    python3 FileClass.py lorem.txt -p
        runs printFile function from File class
    python3 FileClass.py lorem.txt -ranl
        runs removeAllNewLines() function from File class. Be advised, it alters the file
    python3 FileClass.py lorem.txt -raw sit
        runs removeAllWords(...) function from File class. Be advised, it alters the file
        requires extra argument that is used for removal keyword, if not provided it throws an error
    python3 FileClass.py lorem.txt -rw sit
        runs removeWord(...) function from File class. Be advised, it alters the file
        requires extra argument that is used for removal keyword, if not provided it throws an error
    python3 FileClass.py lorem.txt -cf
        runs clearFile(...) function from File class. Be advised, it alters the file
    python3 FileClass.py lorem.txt -asb tacos
        runs addStringAtBeginning(...) function from File class. Be advised, it alters the file
        requires extra argument that is added to file, if not provided it throws an error
    python3 FileClass.py lorem.txt -ase tacos
        runs addStringAtEnd(...) function from File class. Be advised, it alters the file
        requires extra argument that is added to file, if not provided it throws an error
            '''
        print(helpString)


if __name__ == "__main__":
    # try to create File object, print error if use did not provide an arguement
    try:
        lorem = File(sys.argv[1])
    except IndexError:
        File("").printHelp()
        
    ## dictionary to store flag to function association
    options = {
        '-h': lorem.printHelp,
        '-s': lorem.search,
        '-p': lorem.printFile,
        '-ranl': lorem.removeAllNewLines,
        '-raw': lorem.removeAllWords,
        '-rw': lorem.removeWord, 
        '-cf': lorem.clearFile,
        '-asb': lorem.addStringAtBeginning,
        '-ase': lorem.addStringAtEnd
    }

    # make shift switch statement, currently can only run command at a time
    try: 
        needExtraArgument = sys.argv[2] == '-s' or sys.argv[2] == '-raw' or sys.argv[2] == '-rw' or sys.argv[2] == '-asb' or sys.argv[2] == '-ase'
        if (needExtraArgument):
            options.get(sys.argv[2])(sys.argv[3])
        else:
            options.get(sys.argv[2])()
    except (IndexError, TypeError):
        File("").printHelp()
    

    


# Examples:

# python3 FileClass.py lorem.txt -h
    # runs printHelp() function from File class
# python3 FileClass.py lorem.txt -s sit
    # runs search(...) function from File class
    # requires extra argument that is used for search keyword, if not provided it throws an error
# python3 FileClass.py lorem.txt -p
    # runs printFile() function from File class
# python3 FileClass.py lorem.txt -ranl
    # runs removeAllNewLines() function from File class. Be advised, it alters the file
# python3 FileClass.py lorem.txt -raw sit
    # runs removeAllWords(...) function from File class. Be advised, it alters the file
    # requires extra argument that is used for removal keyword, if not provided it throws an error
# python3 FileClass.py lorem.txt -rw sit
    # runs removeWord(...) function from File class. Be advised, it alters the file
    # requires extra argument that is used for removal keyword, if not provided it throws an error
# python3 FileClass.py lorem.txt -cf
    # runs clearFile(...) function from File class. Be advised, it alters the file
# python3 FileClass.py lorem.txt -asb tacos
    # runs addStringAtBeginning(...) function from File class. Be advised, it alters the file
    # requires extra argument that is added to file, if not provided it throws an error
# python3 FileClass.py lorem.txt -ase tacos
    # runs addStringAtEnd(...) function from File class. Be advised, it alters the file
    # requires extra argument that is added to file, if not provided it throws an error



## open("filepath", "mode", "buffer")