# Generator based file reader-writer

For completing this task you have to download the rockyou.txt file from this link - 

```
https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
```
and put the file inside the directory ```generator```

Run
```python decoder.py```

or use following link to change file encoding

```https://www.freeformatter.com/convert-file-encoding.html```

Rename the file ```rockyou.txt``` into ```rockyou_utf8.txt```

Acceptance criteria:

    When the app runs it asks for user input which describes the search word

    After the user had entered the value - all lines from the rockyou file which
    include the requested line are added to the new file called results.txt

    Once the file is created the user sees the next information in the Console:
    - The number of lines of a cerated file
    - The total size of the created file (use Pympler 3-rd party library
