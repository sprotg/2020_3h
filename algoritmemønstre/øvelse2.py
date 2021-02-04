def størst(l):
    m = float("-inf")
    for i in l:
        if i > m:
            m = i
    return m

def mindst(l):
    m = float("inf")
    for i in l:
        if i < m:
            m = i
    return m

m = mindst([1,2,-4,5])
print(m)
s = størst([1,2,-4,5])
print(s)
