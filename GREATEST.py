x=input()
x=x.split()
a=int(x[0])
b=int(x[1])
c=int(x[2])
if a>b:
 if a>c:
  print(a)
 else:
  print(c)
elif b>c:
 print(b)
else:
 print(c)
