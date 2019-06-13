# -*- coding: utf-8 -*-
""" 注释只能在句尾使用关键字和关键符 """
""" 除关键字外,python变量赋值就是声明,变量赋值为空,就是内容不定的变量 """
""" 引用模块时添加别名,简化语句 """
# import keyword as k
# print(k.kwlist)
""" python对缩进敏感,冒号表示开始子句,缩进表示子句所处的层次 """
# if True:
#     print("yes")
# else:
#     print('no')
""" python语句换行使用反斜杠 """
""" 反斜杠也是文本字符转义符"""
""" 文本引号前加r表示raw,反转义,使转义符和文本标点符(如换行符)无效 """
""" 三引号字符串所见即所得 """
""" python空行只是为了区分函数块,无实际意义 """
""" 同一行内多条语句时,python使用;分号表示语句结束(不推荐一行多条语句) """
""" print输出默认换行,可以在结尾加上end=连接符,连接不同print字符串 """
# print("\n")
# print(r"\n")
# print("a",end="傻逼")
# print("随便")
# print(""" \n """)
""" 注释不要打断缩进关系树,即本例中从class下穿和def连接def的纵线 """
class Vector:
   """ 自定义类的方法第一个参数是方法的实例自身,例命名为self,也可以随意命名,但不推荐 """
   """ 自定义类有若干内置的私有方法和属性,即使没有声明也可以内部调用,包括init,class,name,main """
   def __init__(self, a, b):
      self.a = a
      self.b = b

   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)
      """ 运算符重载也是内置的私有方法,使得类可以按照自定义的方法使用各类基础运算符,
      本例为使用加号运算符 """
   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)
      """ self参数代表的是类的实例(也即是变量),而非类本身 """
   def prt(self):
      print(self)
      print(self.__class__)
""" 自定义类的第一个参数必须是实例本身,即使是无参方法,也必须声明实例本身作为参数 """
""" 自定义类从第二个参数开始,才是真正的参数 """

v1 = Vector(2,10)
v2 = Vector(5,-2)
v3 = Vector(1,2)
print(v1+v2+v3)
print(v1)
""" 类的私有属性和方法以双下划线开头,私有属性无法被实例从外部调用,但是类的私有属性可以被外部调用 """
print(v1.__class__.__name__)
v1.prt()