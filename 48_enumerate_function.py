#normal
li=[1,2,3,4,5,6]
index=0
for l in li:
    print(l)
    if(index==2):
        print('now it is showing third index')
    index+=1

#with enumerate funtion
marks=[33,88,90,33]
for ind,mark in enumerate(marks):
    print(mark)
    if(ind==2):
        print('you got A+')
    
#with string   
fruits=['mango','apple','cherry','berry']    
for inde,fruit in enumerate(fruits,start=1): 
    print(inde,fruit)
        
            
                
                        