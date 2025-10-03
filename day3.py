#sets={}...
set={1,2,3,1,2,1,2}                     #set(any variable which you want..)
print(set)                              #set is avoid repeated element.



#list=[]...
list=[1,2,3,3,4,5,6,6,7,7,8]            #list(any variable which you want..)
list.append(11)                         #this is add element syntax 
print(list)                             #Mutable -> list




#dict={}...
dict={                                  #dict(any variable which you want..)
    "model":"1st model",                #before colon(:) is "key" element and after colon(:) is "value" element.
    "year":2021,
    "age":25
}
print(type(dict))
print(dict['model'])                   #this syntax is print single value of key 
dict['city']='Hydrabad'                #this is add element syntax 
print(dict)





#tuple=()..
tuple=(1,2,3)                           #tuble(any variable which you want..)
print(tuple)                            #Immutable -> tuple



#functions..                            # "def" is a function
def mom(a,b):                           # mom(a,b):   -> is called parameter
    print(a+b)                          # mom is like a variable
a=10
b=20
c=mom(a,b)
print(c)                                # mom(a,b)    -> is called arguments
d=mom(5,6)
print(d)
e=mom(a,b)
print(e)
f=mom(5,6)
print(f)
