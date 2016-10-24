a = [1,2]
b=[1.5,1,a]
print b

print range(5)
print range(3,8)
print range(0,10,2)

print len(range(0,10,2))

a = [1,2]
b = [3,4,5,6]
print a + b
print a * 2
x = [1, 2, 3, 4]
print x
print x[-1]
print x[-2]
print x[0:2]
print x[:]
print x[::2]
print x[::-1]
print 7 in x
print 2 in x
x.append(5)
print x

x = [0, 1, [2]]
x[2][0] = 3
print x
x[2].append(4)
print x
x[2] = 2
print x

#The for statement
for x in [1, 2, 3, 4]:
    print x

for i  in range(10):
   print i, i*i, i*i*i

print zip(["a", "b", "c"], [1, 2, 3])
print zip(["a", "b", "c"], [1, 2])

names = ["a", "b", "c"]
values = [1, 2, 3]
for name, value in zip(names, values):
    print name, value
x = [1, 2, 3]
print sum(x)


#Sorting lists
a = [2, 10, 4, 3, 7]
print sorted(a)
print a
a.sort()
print a
