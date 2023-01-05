def insertion_sort(n,arr):
    a = arr[n - 1]
    b = 0
    for i in range(n - 1, 0, -1):
        if i == 1 and arr[0] > a:
            j = arr[1]
            arr[i] = arr[i - 1]
            for i in arr:
                print(i, end=" ")
            print("")
            arr[1] = j
            z = arr[0]
            arr[0] = a
            arr[1] = z
            for p in arr:
                print(p, end=" ")
            print("")
            break
        if b != 0:
            break
        assert -10000 <= arr[i] <= 10000
        if a <= arr[i - 1]:
            arr[i] = arr[i - 1]
            # for i in arr:
            #    print(i, end=" ")
            # print("")
        else:
            arr[i] = a
            b += 1
        for i in arr:
            print(i, end=" ")
        print("")


