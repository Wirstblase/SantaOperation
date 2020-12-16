file1 = open("sample",'r')

nrr = 0
        
Lines = file1.readlines()

for line in Lines: 
    row = line.strip()
    if("n*r" in row):
        row = row.replace("n*r=", "")
        nrr = int(row)

print(str(nrr))
