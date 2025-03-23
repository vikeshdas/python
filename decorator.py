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




# Application of decorator

"""
    One application of decorators can be logging. Define a logger decorator that prints information about the function, such as the execution date and time, and the function name. Then, use that decorator with all functions where you need the same kind of logging.
"""

def decorator(func):
    """
    The libraries below are placed inside the function because, let's say these decorators are in a module, and we want to use them in another module via import. In that case, we don't need to import them externally in the module where we are using them.

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
    what if we want to pass a function in multiple decorator at same time ,what will be order of excution of decorator
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
 so on function two decorator will be called ,very first decorator2 will be called and then decorator1. we can change the order based on our requirement.
"""
@decorator2
@decorator1
def func():
    print("func is called")

func()

# Onother application of decorator

"""
    Calculate the sum of the first n Fibonacci numbers using a decorator and closure.Use memoization because the Fibonacci function calls itself recursively on the same numbers repeatedly.In the code below, a closure is used, and you can see a dictionary for memoization.
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


print("**********************************************************************")
# decorator with parameter

"""
    lru_cache decorator is used for mamoization. can we send parameter in decorator while calling?. some built-in decorator of python like lru_cache(256) takes argument.as you can see below exmaple
"""
from functools import lru_cache
import random
"""
@lru_cache(max_szie=256) this is actually function call not decorator .it is funciton call which creates decorator.there will be decorator defined in that funciton.
"""
@lru_cache(256)
def func():
    pass


"""
Below is a custom (user-defined) lru_cache. The lru_cache from functools is defined similarly. We used a parameter to fix the maximum size of the cache. In lru_cache, we basically remove the least recently used key-value pair if the size of the cache exceeds the limit.

The lruCache() function below is called a decorator factory, which creates and returns a decorator.
"""
def lruCache(max_size):
    def decorator(func):
        print("inside decorator")
        cache={}
        def inner(n):
            print("inside inner")
            if n in cache:
                return cache[n]
            
            res=func(n)
            cache[n]=res

            if len(cache)>max_size:
                # remove some key value
                print("removing somekeys")
                random_keys = random.sample(list(cache.keys()), 5)
                for key in random_keys:
                    cache.pop(key)
            return res
        return inner
    return decorator 

@decorator(max_size=10)
def fibbonacci(n):
    if n<=2:
        return 1
    return fibbonacci(n-1)+fibbonacci(n-2)



print(fibbonacci(114))


print("*********************************************************************")
"""
    Decorator using class
"""

class MyClass:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __call__(self,c):
        """
            In Python, the __call__ method is a special method that allows an instance of a class to be called as a function.
        """
        print("called a={0} ,b={1}, c={2}".format(self.a,self.b,c))


obj=MyClass(10,20)
obj(30)

"""
    we can use __call__method as a decorator
"""
class MyClass:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __call__(self,func):
        def inner(*args,**kwars):
            print("inside inner")
        return inner


@MyClass(10,20)
def func():
    pass

func()



"""
So far, we have worked with decorating functions. This means we can decorate functions using the '@' symbol. Since class methods are essentially functions, they can also be decorated.

A class decorator takes a class as input, modifies or extends its behavior, and returns a new class, similar to how a function decorator works.
"""

from datetime import datetime, timezone

def debug_info(cls):
    def info(self):
        results = []
        results.append('time: {0}'.format(datetime.now(timezone.utc)))
        results.append('class: {0}'.format(self.__class__.__name__))
        results.append('id: {0}'.format(hex(id(self))))
        
        if vars(self):
            for k, v in vars(self).items():
                results.append('{0}: {1}'.format(k, v))
        
        
        return results
    
    cls.debug = info
    
    return cls

@debug_info
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    def say_hi():
        return 'say hi '
    
obj = Person('vikesh', "das")
res=obj.debug()
print(res)