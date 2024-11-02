import cmath
a=float(input('Enter a: '))
b=float(input('Enter b: '))
c=float(input('Enter c: '))
d = b**2 - 4*a*c
print('Determinant =', d)
if d > 0 :
  r1 = ((-b+cmath.sqrt(d))/(2*a))
  rounded_number = format(r1, ".2f")
  print(rounded_number)
  r2 = ((-b-cmath.sqrt(d))/(2*a))
  rounded_number2 = format(r2, ".2f")
  print(rounded_number2)
elif d == 0:
  print(-b/(2*a))
else:
  print('COMPLEX ROOTS ONLY')

x = []
s = int(input("Elements: "))
for a in range(0, s):
  elm = int(input())
  x.append(elm)
n=int(input('Enter n: '))


def fn(x,s,n):
  c=0
  print('(', end = " ")
  l = []
  for index, i in enumerate(x):
    if i < n:
      l.append(i)
      c+=1
  for i in range(len(l)):
    if i == len(l) - 1:
      print(l[i], "<", n, end = " ")
    else:
      print(l[i], "<", n, end = ", ")
  print(')')
  return c


c = fn(x,s,n)
print('Total Values less: ', c)

dup = [12,24,35,24,88,120,155,88,120,155]
newls = set()
res = []
for item in dup:
        if item not in newls:
            res.append(item)
            newls.add(item)
print(res)

s1=set([1,3,6,78,35,55])
s2=set([12,24,35,24,88,120,155])
s1 &= s2
print(s1)

w=int(input('Enter w: '))
h=int(input('Enter h: '))
print(w/h**2)

growth_multiplier = 1.3
sales=1000
sn = sales * (growth_multiplier ** 7)
print(round(sn,2))

mkg=int(input())
print(round((mkg*2.2)/14,2))

room = ["hall 11.3","kitchen 6","bedroom 12.5"]
for item in room:
    print(item)

s1 = {"name": "S1", "gpa": [3.5, 3.8, 3.2, 3.7, 3.6, 3.9]}
s2 = {"name": "S2", "gpa": [3.2, 3.1, 3.4, 3.6, 3.7, 3.8]}
s3 = {"name": "S3", "gpa": [3.9, 4.0, 3.8, 3.9, 3.7, 4.0]}

Students = [s1, s2, s3]

for i in Students:
    print(f"StudentName: {i['name']}")
    print("GPAs for each semester:", i["gpa"])
    print()
ds_lab01.py
Page 2 of 2 Page 1 of 2
