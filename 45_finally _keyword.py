def fun1():
    try:
        li=[1,2,3,4,5]
        x=int(input("Please inter your number:"))
        print(li[x])
        return 0
    except:
        print('wrong guess')
        return 1
    finally:
        print('it will be always printed')


print(fun1())


