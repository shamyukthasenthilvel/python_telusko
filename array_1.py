import array as arr
#arr->function
#array->module
vals =arr.array('i',[1,2,3,-8])
print(vals.buffer_info)
print(vals.typecode)
for i in vals:
    print(i)
for i in range(len(vals)):
    print(vals[i])
newArr = arr.array(vals.typecode,(a for a in vals))
for i in newArr:
    print(i)
