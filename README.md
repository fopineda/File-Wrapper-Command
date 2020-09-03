# File-Wrapper-Command

Project contains a single python file that opens a file (programmatically) and allows you view, edit, search, and delete the file.

## Key Items
* [Python's Regex module](https://docs.python.org/3/library/re.html)
* [Python's system arguments module](https://docs.python.org/3/library/sys.html)


## Installation
I'm assuming you have python3 installed. If not, then you can easily download it by following these videos: [Windows](https://www.youtube.com/watch?v=4Rx_JRkwAjY), [MAC](https://www.youtube.com/watch?v=0hGzGdRQeak)

1. Clone or download project
    ```bash
    git clone https://github.com/fopineda/File-Wrapper-Command.git
    ```
That's all...


# Usage
1. Enter the project folder
    ```bash
    cd File-Wrapper-Command
    ```
2. Run the file's help documentation
    ```bash
    python3 FileClass.py -h
    ```
    It will display easy to follow documentation on how to run the file properly.

    Please see examples below for more help :)

    Also, the project has a dummy lorem.txt file so you can test the commands.
    If you wish to complete the operations on your own file just put it n the folder and replace "lorem.txt" with the path/name of your file.

    Enjoy 😊


# Examples
runs printHelp() function from File class
```bash
python3 FileClass.py lorem.txt -h
```

runs search(...) function from File class

requires extra argument that is used for search keyword, if not provided it throws an error
```bash
python3 FileClass.py lorem.txt -s sit
```
runs printFile() function from File class
```bash
python3 FileClass.py lorem.txt -p
```

runs removeAllNewLines() function from File class. Be advised, it alters the file
```bash
python3 FileClass.py lorem.txt -ranl
```

runs removeAllWords(...) function from File class. Be advised, it alters the file

requires extra argument that is used for removal keyword, if not provided it throws an error
```bash
python3 FileClass.py lorem.txt -raw sit
```

runs removeWord(...) function from File class. Be advised, it alters the file

requires extra argument that is used for removal keyword, if not provided it throws an error
```bash
python3 FileClass.py lorem.txt -rw sit
```
runs clearFile(...) function from File class. Be advised, it alters the file
```bash
python3 FileClass.py lorem.txt -cf
```
runs addStringAtBeginning(...) function from File class. Be advised, it alters the file

requires extra argument that is added to file, if not provided it throws an error
```bash
python3 FileClass.py lorem.txt -asb tacos
```
runs addStringAtEnd(...) function from File class. Be advised, it alters the file

requires extra argument that is added to file, if not provided it throws an error
```bash
python3 FileClass.py lorem.txt -ase tacos
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.