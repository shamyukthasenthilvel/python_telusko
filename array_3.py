import array as arr
mine=arr.array('i',[1,2,34,96])
for i in range(len(mine)):
    if i ==2:
        del mine[i]
print(mine)
