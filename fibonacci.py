
list=[0,1]
for i in range(2,50):
    x= list[i-1]+list[i-2]
    list.append(x)
print(list)
#using recursion
fib =int(input("enter a number"))
def fibonaci(fib):
    if fib==1:
        return 1
    else:
        return fibonaci(fib-1)+fibonaci(fib-2)
print(fibonaci(fib))


        
