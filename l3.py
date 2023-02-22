#arthimetic operator
print("arthimetic operator")
a=11
b=2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a//b)
print(a%b)

#assigment operator
print("assignment operator")
a=5
a+=1
print(a)
a-=1
print(a)

#comparison operator
print("comparison operator")
a=4
b=5 
c=10
print(a==b)
print(a>b)
print(b>c)
print(b<=c)
print(a==b==c)
print(a!=b)

#logical operators
print("logical operation start")
a=10
b=20
c=20
result = a<b and b==c
print(result)
print(not a<b)
print(a<b or b==c)

#identity operators
a=222
b=222
print(a is b)
print(a is not b)
a=[1]
b=[1]
print(a is b)
print(a is not b)

#membership operators
name="broadway"
result="b" in name
print(result)
vowels=['a','e','i','o','u']
result="a" in vowels
print(result)
a=[1,2,3,4,5]
print(1 in a)

