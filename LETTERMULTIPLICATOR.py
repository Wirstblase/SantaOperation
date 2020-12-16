#Multiplicates file1 at the end of file2

def modIndex(inf,opf,startnr):
    file1 = open(inf,'r')
    file2 = open(opf,'w')

    nrr = 0
        
    Lines = file1.readlines()

    for line in Lines: 
        row = line.strip()
        if("n*r" in row):
            row = row.replace("n*r=", "")
            nrr = int(row)

    print(str(nrr))

    i = 0
    i = startnr
    #i = int(input("Number to start counting from: "))

    for line in Lines:
        row = line.strip()
        if("n*r" in row):
            row = row.replace("n*r=", "")
            file2.write("n*r="+str(i)+"\n")
            i=i+1
        else:
            file2.write(row + "\n")


    file1.close()
    file2.close()


def appendatob(a,b):
    file1 = open(a,'r')
    file2 = open(b,'a')

    Lines = file1.readlines()

    file2.write("\n")

    for line in Lines:
        row = line.strip()
        file2.write(row + "\n")

    file1.close()
    file2.close()

print("done")


times = input("how many times you want to duplicate the data? : ")
for i in range(int(times)):
    appendatob("sample.txt","big.txt")

modIndex("big.txt","sample.txt",0)
    
    



