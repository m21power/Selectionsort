def SSort(l):
    i=0
    while i<len(l):
        j=i+1
        while j<len(l):
            if l[i]>l[j]:
                l[i],l[j]=l[j],l[i]
            else:
                pass
            j+=1
        i+=1
    return l
