with open("log.txt") as f:
    lines = f.readlines()

lineno = 1

for line in lines:
    if("Python" in line):
        print(f"yes python is present. Line no: {lineno}")
        break
    lineno += 1

else:
    print("No absent")    