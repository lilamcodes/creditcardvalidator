def binary_search(n):
    alist = [1,2,3,4,5,6,7]
    lower = alist[0]
    upper = len(alist)

    while lower < upper:   
        x = lower + (upper - lower) // 2
        val = alist[x]
        if 3 == val:
            print (position)
            return x
        elif 3 > val:
            alist = alist[x:]
            lower = alist[0]
            if 3 == val:
                print (position)
                return x

            


        elif 3 < val:
            alist = alist[:x]
            if 3==val:
            print(position)
            return x




binary_search(3)