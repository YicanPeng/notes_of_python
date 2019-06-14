# -*- coding: utf-8 -*-
""" 程序 = 数据结构 + 算法,数据结构分3种:排序,判断(选择),循环 """
""" 1.基础语法,注释 """
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

""" 自定义函数 """
""" 不可变对象相当于VBA的值传递,原有变量不会被函数运算重新赋值;
   可变对象类似引用传递,与函数共享同一内存指针,会在函数运算后被重新赋值 """

""" 自定义函数时,可以声明缺省参数,如本例中的l参数和n参数
   加*的参数是不定长参数,类似VBA的可选参数,加一个*,返回值是元组类型,如本例m参数;加两个*,返回值是字典类型
   在引用函数时,不定长参数之后的参数必须使用索引名赋值,如本例n参数 """
def fibo(l=100,*m,n=0):
   a,b=0,1
   n = int(n)
   while b<n+l:
      print(b,end=" ")
      a,b=b,a+b
   print(m)
""" 交叉赋值,同时赋值是python特色 """
""" 本例中第3参数必须使用索引名赋值 """
fibo(100,n=1)

""" 模块 """
""" 包和模块有两种引入方式,即:import 模块 和 from 模块 import 函数 ;
其中import 函数名 from 模块 可以直接调用函数名,无需 模块.函数 的方式调用
但是后引入的函数会覆盖之前引入的同名函数,因此不推荐此方法引入函数"""
import sys
""" 引入函数以后,可以通过赋值的方式,对函数进行重命名,以减小代码量 """
""" sys.path属性返回python引入包和模块的所有路径,第一个路径永远是当前py文件所在的文件夹
可以通过sys.path.append(模块路径)的方式手动添加模块路径 """
aaa = sys.path
bbb = fibo
# print(aaa)
""" dir函数返回包或模块或函数自定义的字符 """
# print(dir(bbb))
# bbb()
""" 文件引用自身内置属性和方法,无需前缀,__name__属性永远是__main__ """
# print(__name__)





























""" 注释不要打断缩进关系树,如本例中从class下穿和def连接def的纵线 """
class Vector:
   """ 自定义类的方法第一个参数是方法的实例自身,例命名为self,也可以随意命名,但不推荐 """
   """ 自定义类有若干内置的私有方法和属性,即使没有声明也可以内部调用,包括init,class,name,main """
   def __init__(self, a, b):
      self.a = a
      self.b = b
   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)
   """ 注释只能与代码块主句对齐,不能与子句缩进 """
   """ 运算符重载也是内置的私有方法,使得类可以按照自定义的方法使用各类基础运算符
   本例为使用加号运算符 """
   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)
   """ self参数代表的是类的实例(也即是变量),而非类本身 """
   def prt(self):
      print(self)
      print(self.__class__)
      print(self.__str__.__doc__)
""" 自定义类的第一个参数必须是实例本身,即使是无参方法,也必须声明实例本身作为参数 """
""" 自定义类从第二个参数开始,才是真正的参数 """
v1 = Vector(2,10)
v2 = Vector(5,-2)
v3 = Vector(1,2)
# print(v1+v2+v3)
# print(v1)
""" 类的私有属性和方法以双下划线开头,私有属性无法被实例从外部调用,但是类的私有属性可以被外部调用 """
# print(v1.__class__.__name__)
# v1.prt()

""" print可以输出两个文本,其中sep参数是两个文本的间隔符,默认为空格,end参数是两个print之间的连接符,默认为回车 """
# print(1,2,sep=",",end=".")
# print("a")
""" help函数是内置函数,返回数据类型或函数或模块的详细说明 """
# help(print)

