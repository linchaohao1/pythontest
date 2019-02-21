def kuaisupaixu(shuzu):
    if len(shuzu)<2:
        return shuzu
    else:
        a = shuzu[0]
        less = [b for b in shuzu[1:] if b <a]
        equql = [c for c in shuzu if c ==a]
        more = [d for d in shuzu[1:] if d >a]
        new = kuaisupaixu(less) + equql + kuaisupaixu(more)
        return new

def maopao(shuzu):
    for i in range(len(shuzu)-1):
        for j in range(len(shuzu)-1-i):
            if shuzu[j]>shuzu[j+1]:
                shuzu[j],shuzu[j+1] = shuzu[j+1],shuzu[j]
    return shuzu

def xuanze(shuzu):
    for i in range(len(shuzu)-1):
        for j in range(1,len(shuzu)-i):
            if shuzu[i]>shuzu[i+j]:
                shuzu[i],shuzu[i+j] = shuzu[i+j],shuzu[i]
    return shuzu

aa = [50,2,66,3,10,20,11,88,562,1,2,4,23]
print(xuanze(aa))