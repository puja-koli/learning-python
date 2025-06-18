for i in range(12):
    print("5 X",i+1,"=",(i+1)*5)
    if(i+1==10):    
        break
print("Done")

for x in range(1,10):
    print('7 X',x,'=',x*7)    
    if(x==7):       
        continue                
print('okay')                    

#do while loop emulate
a=1                                            
while True:
    print(a)
    a+=1
    if(a%10==0):                                                                                break