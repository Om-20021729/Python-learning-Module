"""



OTHER METHODS TO READ THE FILE.
We can also use f.readline() function to read one full line at a time.
f.readline() # Read one line from the file.



MODES OF OPENING A FILE
r – open for reading
w - open for writing
a - open for appending
+ - open for updating.
‘rb’ will open for read in binary mode.
‘rt’ will open for read in text mode.


"""
f = open("file.txt")

lines = f.readlines()

print(lines, type(lines))

f.close()