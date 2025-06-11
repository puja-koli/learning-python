#print the second iteam of the list
fruits=['apple','banana','cherry']
print(fruits[1])
#change the value from apple to kiwi
fruits=['apple','banana','cherry']
fruits[0]='kiwi'
print(fruits)
#add orange to the list(append)
fruits=['apple','banana','cherry']
fruits.append('orange')
print(fruits)
#add lemon to the list (insert)
fruits=['apple','banana','cherry']
fruits.insert(1,'lemon')
print(fruits)
#remove banana from the list 
fruits=['apple','banana','cherry']
fruits.remove('banana')
print(fruits)
#use negative indexing to print the last item in the list
fruits=['apple','banana','cherry']
print(fruits[-1])
#use a range of indexes to print third,fourth and fifth item in the list
fruits=['apple','banana','cherry','mango','kiwi','orange']
print(fruits[3:6])
#use the correct syntax to print the number of item in the list 
fruits=['apple','banana','cherry']
print(len(fruits))