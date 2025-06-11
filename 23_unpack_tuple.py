fruits=('apple','banana','cherry','kiwi')
(a,b,c,d)=fruits
print(a)
print(b)
print(c)
print(d)

color=('red','green','blue','black')
(*x,)=color
print(x)

num=(1,2,3,4)
(f,*g)=num
print(f)
print(g)
