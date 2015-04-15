def order_of_seats(cinema):
    leng = len(cinema)
    wid = len(cinema[1])
    frees = []
    firstf = []
    for row in cinema:
        nf = 0
        for k in row:
            nf += k
        frees.append(wid - nf)
    i = 0
    while i < leng:
        for j in range(0,wid):
            if cinema[i][j] == 0:
                firstf.append(j)
                break
        i += 1    
    br = 0
    for row in cinema:
        for k in row:
            if k == 0:
                br += 1
    #print(br)            
    ans = []

    for t in range (0, br):
        minf = wid + leng + 1
        mini = 0
        for i in range(0, leng):
            if frees[i] > 0:
                if frees[i] < minf:
                    mini = i
                    minf = frees[i]
        #print(frees)        
        ans.append( (mini + 1,firstf[mini] + 1) )
        frees[mini] -= 1
        cinema[mini][firstf[mini]] = 1
        for j in range(firstf[mini], wid):
            if cinema[mini][j] == 0:
                firstf[mini] = j
                break
    return ans


           
