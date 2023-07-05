f = open("demofile2.txt", "a")
f.write("\nSee you soon!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())