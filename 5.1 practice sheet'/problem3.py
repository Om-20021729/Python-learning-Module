s = set()

n = input("Enter number :  ")
s.add(int(n))
n = input("Enter string :  ")
s.add(str(n))
print(s)

#or
s = set()
s.add(18)
s.add("18")
print(s)