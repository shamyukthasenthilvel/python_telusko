#conventional method with 3rd variable
#a variable is wasted
a=10
b=20
print(a,b)
temp = a
a=b
b=temp
print(a,b)
#with a formula 
#a+b=6+5gives 11 wasting 1 bit
x=10
y=20
print(x,y)
x=x+y
y=x-y
x=x-y
print(x,y)
#using xor bits is not wasted
s=5
r=6
print(s,r)
s=s^r
r=s^r
s=s^r
print(s,r)
#in python ROT_TWO() swaps the two topmost stack items
shamy=20
malli=100
print(shamy,malli)
shamy,malli=malli,shamy
print(shamy,malli)