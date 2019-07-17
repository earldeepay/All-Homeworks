# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 07:59:21 2019

@author: DELL PC
"""
#the following code is if statement
def num():
    x,y,z = 2,2,3
    if (x==y):
        st = "true"
    elif(x!=z or y!=z):
        st = "false"
    print(st)
num()    

#if none of the parameters are equa
def num2():
    x,y,z = 1,2,3
    if (x==y):
        st = "true"
    elif(x!=z or y!=z):
        st = "false"
    print(st)
num2()  
        
#the following code will convert string to integer and compare them
def num1():
    x,item,y = 2,2,3
    item_int = int(item)
    if (x==item_int):
        pt = "true"
    else:
        pt =  "false"
    print(pt)    
num1()        
    
    
    
    
    