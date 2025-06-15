#nested conditionals
import time
t= int(time.strftime('%H'))
print(t)
int(t)
if (5<=t<11):
    print("GOOD MORNING")
elif(t<22):
    if(t<16):
        print("GOOD NOON")
    elif(t<18):   
        print("GOOD AFTERNOON")
    elif(t<22):   
        print("GOOD EVENING")
else:
    print("GOOD NIGHT")
#if elif else    
num=int(input(print('inter your number:')))
if num>0:             
    print('YOUR NUMBER IS POSITIVE')   
elif num==0:                       
    print('YOUR NUMBER IS ZERO')
else:
    print('YOUR NUMBER IS NEGATIVE')              
                                                                            
                                                                                            