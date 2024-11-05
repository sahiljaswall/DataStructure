def halfsquarepattern(n):
    for x in range(0,n):
        for y in range(0,x):
            print("*" ,end=" ")
        print(end="\n")
halfsquarepattern(int(input("how many stars:")))
