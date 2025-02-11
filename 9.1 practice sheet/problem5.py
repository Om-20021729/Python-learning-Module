words = ["Donkey", "bad", "ganda"]

with open("file1.txt", "r") as f:
    content = f.read()

contentNew = content  # Initialize with original content

for word in words:
    contentNew = contentNew.replace(word, "#" * len(word))  # Update contentNew correctly

with open("file1.txt", "w") as f:
    f.write(contentNew)
