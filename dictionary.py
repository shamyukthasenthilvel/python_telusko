data={1:'shamy',2:'malli'}
a=data[1]
print(a)
data.get(2)
#data[3]
data.get(3)#dont give any error
print(data.get(4,'not found'))
#making list in dictionary
key=['shamy','malli','deepi']
values=['python','java','js']
my_dict=dict(zip(key,values))
print(my_dict)
my_dict['abi']='rubi'
print(my_dict)
del my_dict['deepi']
print(my_dict)
prog={'js':'atom','cs':'vs','python':['pycharm','sublime'],'java':{'jse':'netbeans','jee':'eclipse'}}
print(prog['python'])
print(prog['python'][1])
