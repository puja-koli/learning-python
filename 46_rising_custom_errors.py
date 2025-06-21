a=int(input('Inter your number between 5 to 9 :'))
if(a<5 or a>9):
    raise ValueError('your number is not between 5 to 9')
else:
    print(f'your number is:{a}')







