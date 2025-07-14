from functools import reduce

nums=[2,3,4,5,6,7,8,9,1,23,45,32,67,34,6,3,4,34,343]
evens =list(filter(lambda a : a%2==0,nums))
multiple = list(map(lambda a:a*2,evens))
sum=reduce(lambda a,b:a+b,multiple)
print(sum)