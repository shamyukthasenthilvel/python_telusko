import array as arr
mine = arr.array('i',[22,5,4,22,74,69])
n=len(mine)
for i in range(n//2):
    mine[i],mine[n-i-1]=mine[n-i-1],mine[i]
print(mine)