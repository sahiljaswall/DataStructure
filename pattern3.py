def halfsquarepattern(n):
    for x in range(0,n):
        for y in range(n,0):
            print("*" ,end=" ")
        print(end="\n")
halfsquarepattern(int(input()))
