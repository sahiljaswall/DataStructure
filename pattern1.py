def squarepattern(n):
    for x in range(0,n):
        for y in range(0,n):
            print("*" ,end=" ")
        print(end="\n")
squarepattern(int(input("how many stars:")))
