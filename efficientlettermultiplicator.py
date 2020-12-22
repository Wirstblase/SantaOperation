def appendatob(a,b):
    file1 = open(a,'r+')
    file2 = open(b,'a+')

    while True:
        
        l = file1.readline()

        file2.write(l)
        #file2.write("\n")

        if not l:
            break


times = input("how many times you want to duplicate the data? : ")
for i in range(int(times)):
    appendatob("sample.txt","big.txt")
