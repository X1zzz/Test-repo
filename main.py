

import time
# print(dir(a))
#
# print(type(a.__doc__))           # 如果是属性，打印结果是str
# print(type(a.bit_length()))           # 如果是方法，打印结果是
# print(type(a.bit_length))           # 如果是方法，打印结果是 builtin_function_or_method

import Test1
class Person:
   def __init__(self, name, age):
      self.name = name
      self.age = age

   def greet(self):
      print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# 创建Person类的实例
person1 = Person("Alice", 30)
dog1 = Test1.Dog("Bob",12)

print(type(Person))
print(type(person1))
print(type(Test1.Dog))
print(type(dog1))
print(type(person1.greet))
print(type(person1.name))

# a=list(range(10))
# for i in range(10):
#     print(i)

print(dir(11))




