a=input('Please inter your number:')
print(f'Multification table of {a} is:')

try:
    for i in range(1,11):
        print(f'{int(a)} X {i} ={int(a)*i}')

except:
    print("Invalid Input")














