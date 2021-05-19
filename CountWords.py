def WordCounter():
    A = input("Please Tell the name of your File: ")
    B = open(A)
    C = B.read()
    D = 0
    E = C.split()

    #Method 1:-
    for i in E:
        D = D + 1

    print(D,"words are in your File")

    #Method 2:-
    print(len(E))
        


WordCounter()