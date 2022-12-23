def Bubblesort(Arr):
    counter = 0
    for i in range(len(Arr)):
        for j in range(len(Arr)-1):
            if Arr[j]>Arr[j+1]:
                Arr[j],Arr[j+1]=Arr[j+1],Arr[j]
                counter+=1
    print("Array is sorted in",counter,"Swaps")
    new = Arr
    print("First Element: "+str(new[0]))
    print("Last Element: "+str(new[-1]))
Bubblesort([3,2,1])

