class Dog:
   def __init__(self, name, age):
      self.name = name
      self.age = age

import random

import time

# for i in range(10):
#    print(f"\rProgress: {i * 10}%", end="")
#    time.sleep(0.3)

# 定义一个全局变量
global_var = 10
wecan=120

def change_global_var():
   # 使用global关键字声明我们要修改的是全局变量
   # global global_var
   # global_var = 20
   return global_var+1+wecan


# 调用函数，修改全局变量的值
name_list=["小张","小李","小王"]
for index,name in enumerate(name_list):
   print("第{}号玩家是{}".format(index,name))


