#Python script to read a text file, count the number of lines, words, and characters, and then save this information to another text file.
with open('content.txt', "r") as file:
    lines = 0
    #checking numbers of lines in file
    for i in file.readlines():
        lines += 1
    print(f"Total number of lines in file is {lines}")
    characters = 0
    file.seek(0)
    for i in file.read():
        characters += 1
    print(f"Total number of characters in file is {characters}")
    file.seek(0)
    words = file.read().split()
    print(f"Total number of words in file is {len(words)}")

with open('outpt.txt', "w+") as file:
    file.write(f"Total number of lines in file is {lines}\n"f"Total number of characters in file is {characters}\n"f"Total number of words in file is {len(words)}")
