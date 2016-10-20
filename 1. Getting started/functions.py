def square(x):
    return x * x

print square(5)
print square(2) + square(3)
print square(square(3))
def sum_of_squares(x,y):
	return square(x) + square(y)

print sum_of_squares(2,3)

f = square
print f(4)

def fxy(f,x,y):
	return f(x) + f(y)

print fxy(square,2,3)

x = 0
y = 0
def incr(x):
	y = x + 1
	return y
incr(5)
print x,y

pi = 3.14
def area(r):
    return pi * r * r

numcalls = 0
def square(x):
    global numcalls
    numcalls = numcalls + 1
    return x * x
print square(5)
print square(2*5)
x = 1
def f():
    return x
print x


#Buidt-in functions
print min(2,3)
print max(3,4)
print len("helloworld")
print int("10")
print str(123)

#Methods
x = "hello"
print x.upper()

f = x.upper
print f()