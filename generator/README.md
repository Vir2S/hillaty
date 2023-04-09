# Generator based file reader-writer

For completing this task you have to download the rockyou.txt file from this link - 

```
https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwisgfT2-ZT4AhVJxIsKHR9wB4IQFnoECAgQAQ&url=https%3A%2F%2Fgithub.com%2Fbrannondorsey%2Fnaive-hashcat%2Freleases%2Fdownload%2Fdata%2Frockyou.txt&usg=AOvVaw3snAERl1mU6Ccr4WFEazBd
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
