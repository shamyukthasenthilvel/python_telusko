def fact_rec(fact):
    if fact==0:
        return 1
    else:
        return fact*fact_rec(fact-1)
    
num = int(input("enter the num "))
result=fact_rec(num)
print(result)
    