nums=[15,35,45]
value=False
for num in nums:
    if num%2==0:
        print(num)
    else:
        value = True
if value == True:   
    print("not found")

# instead of flag variable ,we can use for else 


nums=[15,35,45]
for num in nums:
    if num%2==0:
        print(num)
else:
    print("not found")