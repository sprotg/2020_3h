def search(l, e):
    res = None
    for i in l:
        if i == e:
            res = i
    return res

def search_interval(l,min, max):
    items = []
    for i in l:
        if i >= min and i <= max:
            items.append(i)
    return items

items = [1,2,8,3,4,5]

print(search(items, 2))
print(search(items, 6))
print(search_interval(items, 2, 4))
