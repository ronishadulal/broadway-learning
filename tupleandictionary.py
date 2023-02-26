tup1 = (1,2,3,1,1,4,4)
count = tup1.count(1)
print(count)
index = tup1.index(2)
print(index)
s = sum(tup1)
print("sum is",s)
print("maximum in tuple", max(tup1))
print("minimum in tuple", min(tup1))
print(sorted(tup1))
a = { 'name': 'abc', 'address': 'abcd'}
a["college"] = "gss"
print(a)
v = a.pop('name')
print(v)
print(all(a))
b = {'x': 1, 'z':3, 'y':2}
print(all(b))
print(any(b))
print(any({}))
print(all({'':2, 'x':3}))
print(any({'': 2, 'x': 3}))
print(len(b))
print(sorted(b))
print(sorted(b, reverse=True))
print(str(a))
print(b.keys())
print(b.values())
print(b.items())
x = b.copy()
print(x)
a = {'z':5}
b.update(a)
print(b)

#y.setdefault('c', 1)
#print(y)


