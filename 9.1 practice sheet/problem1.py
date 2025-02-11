f = open("poem.txt")
content = f.read()
if("RAM" in content):
    print("the shri ram present in the content ")
else:
    print("the shri ram is with hanuman")
f.close()