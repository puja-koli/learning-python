#adding
set1={'red','blue'}
set2={'black','grey'}
list=['a','b']
set1.add('green')
print(set1)
#set1={'red','blue','green'}
set1.update(set2)
print(set1)

set2.update(list)
print(set2)
#removing
num={1,2,3,4}
print(num)

num.remove(2)
print(num)

num.discard(3)
print(num)

fruits={'apple','berry','orange'}
print(fruits)

fruits.pop()
print(fruits)

fruits.clear()
print(fruits)