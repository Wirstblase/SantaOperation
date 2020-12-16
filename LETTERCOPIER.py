#APPENDS file1 at the end of file2

file1 = open("2.txt",'r')
file2 = open("1.txt",'a')

Lines = file1.readlines()

file2.write("\n")

for line in Lines:
    row = line.strip()
    file2.write(row + "\n")

file1.close()
file2.close()

print("done")
