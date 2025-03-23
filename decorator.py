# clouser

def auth(fun):
    cache={}
    def inner(*args,**kwargs):
        print("cache",cache.items())
        username=kwargs.get("username")
        password=kwargs.get("passward")

        if username in cache:
            print("authentcation from cache")
            if password==cache[username]:
                print("valid user")
                return
            else:
                print("invalid username or passwar")

            return

        print("authenticaiton from databse")
        cache[username]=password

        # print(username,password)
        # if res:
        #     func(args,kwargs)
    return inner


@auth
def func():
    pass

func(username="vikesh",passward="123")
func(username="vikesh",passward="1235")
func(username="vikes8h",passward="1823")




# Application of decoretor

"""
    One application of decorator can be logger,define a logger decoretor which print inforation about funcion like excution date and time, function name.Then use that decorator with all funciton where you need same kind of logger.
"""

def decorator(func):
    """
        below libraries inside fuction because ,when lets say this docorator are in a module and using import we want to use in some other module that time we don't need to import externally in that model where we are using it .
    """
    from functools import wraps
    from datetime import datetime,timezone

    @wraps(func)
    def inner(*args,**kwargs):
        date_time=datetime.now(timezone.utc)
        res=func(*args,**kwargs)
        print('{0} called {1}'.format(date_time,func.__name__))
        return res

    return inner


@decorator
def func1():
    pass

@decorator
def func2():
    pass

func1()
func2()

print("*"*20)



"""
    what if we want to pass a function in mutiple decorator at same time ,what will be order of excution of decorator
"""

def decorator1(func):
    def inner():
        res=func()
        print("decorator 1")
        return res
    return inner

def decorator2(func):
    def inner():
        res=func()
        print("decorator 2")
        return res
    return inner
    
"""
 so on funciton two decorator will be called ,very first decorator2 will be called and then decorator1. we can change the order based on our requirement.
"""
@decorator2
@decorator1
def func():
    print("func is called")

func()

# Onother application of decorator

"""
    calculate sum of n fibbonacci number using decorator and clouser.Do memoization because febonacci funciton call recurssivly again and again on same number.In below code used closur,as you can see dictionary for memoization
"""


def feb_decorator(febonacci):
    cache={1:1,2:1}
    def inner(n):
        if n in cache:
            return cache[n]
        s=0
        for i in range(n):
            
            res=febonacci(i)
            cache[n]=res
            s+=res
        return s
    return inner


@feb_decorator
def febonacci(n):
    print("called on {0}th".format(n))
    if n<=2:
        return 1
    
    return febonacci(n-1)+febonacci(n-2)


print(febonacci(6))



