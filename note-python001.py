# -*- coding: utf-8 -*-
p=print
""" 狭义的函数和变量的属性都是数值传递,复制运算;变量的方法是引用传递,就地运算 """
""" 程序 = 数据结构 + 算法,数据结构分3种:排序,判断(选择),循环 """
""" 递归算法本质是数学归纳法,函数在内部调用自身,即计算第N项与第N-1项的关系,而后一直倒推到第1项,也就是基例
   运用的数据结构其实是栈stack,先堆栈push(放进第一项)后弹出pop(移除最后一项) """
""" 1.基础语法,注释 """
""" 除关键字外,python变量赋值就是声明变量,字典列表集合赋值为空,就是元素不定的变量 """
""" 交叉赋值,同时赋值是python特色,使得本来需要中间过渡变量的交叉赋值,同时完成 """
""" 引用模块时添加别名,简化语句 """
# import keyword as k
""" python的保留字无法重命名,也无法命名其他关键字,特别注意True,False,None是大写开头 """
# print(k.kwlist)
""" python对缩进敏感,冒号表示开始子句,缩进表示子句所处的层次 """
# if True:
#     print("yes")
# else:
#     print('no')
r""" python一条语句换行使用反斜杠\,换行后要缩进 """
r""" 反斜杠\也是文本字符转义符"""
""" 文本引号前加r或R表示raw,反转义,使转义符和文本标点符(如换行符)无效 """
""" 三引号字符串所见即所得 """
""" python空行只是为了区分函数块,无实际意义 """
""" 同一行内多条语句时,python使用;分号表示语句结束(不推荐一行多条语句) """
""" print(字符串1,字符串2,字符串3...[sep=" ",end=" \n"])可以输出任意多个字符串,
   其中sep参数是不同字符串的间隔符,默认为空格,end参数是两个print之间的连接符,默认为换行符\n """
str000="runoob"
# print(str,"\n")
# print(r"\n")
# print("a",end="傻逼")
# print("随便")
# print(""" \n """)

""" 数据类型 """
""" python有6种数据类型:数字number,字符串string,元组tuple,列表list,字典dictionary,集合set;
   其中数字,字符串,元组是不可变数据类型
   例如以下三个变量无法再修改数字,字符串和元组的元素,只能对变量重新赋值 """
""" 字符串string,列表list,元组tuple都属于序列,都可以用索引数字进行截取和索引,索引从0计数
   [头标:尾标[:步长]],步长为可选参数,默认为1,负值为逆向查找,索引区间为左闭右开区间,
   如需索引到最后一位,则尾标留空
   索引可以连续索引,如下例tup001[1][0] """
""" 列表和元组是迭代器,用于循环遍历 """
""" 字符串,列表和数组可以同步成对赋值多个变量,但是变量的数量必须与列表和元组的元素数量相等 """
""" 列表的追加.append,插入.insert,删除.remove,移除.pop(默认最后一项)"""
num001=1234;str001="runoob";tup001=(num001,str001,0)
"""推导式语句: 自变量表达式 for 自变量1 in 范围1 if 条件句1 自变量2 in 范围2 if 条件句2 
   推导式语句中 for...in...if... 相当于定语(状语)从句,因此多个并列子句不能加逗号隔开;
   多个for子句的嵌套遵循相同的for循环运算顺序,即外部大循环在前而内部小循环在后;
   python中多个变量逗号仅用于同步成对元素的同时赋值,详见zip函数和enumerate函数"""
""" range函数的头标是0,左闭右开区间 """
lis001_1=[x+y+z for x,y,z in zip(range(3),range(3),range(3)) ]
# num001[0]=5
# str001[0]="x"
# tup001[0]="a"
# print(tup001[1][0])
# print(lis001_1) 
# print(len(lis_001))
num002_0,num002_1,num002_2,num002_3,num002_4,num002_5="abcdefg"[0:-1]
# print((num002_0)*3)
# print("我是%s,我今年%.3f岁" % (input("请输入姓名"),int(input("请输入年龄"))))
""" 字符串.format方法:大括号{}内,冒号:代替百分号%作为格式化占位符,冒号:前面可以加索引符,其他格式化辅助符不变 """
# print("我是{n},我今年{a:.3f}岁".format(a=float(input("请输入年龄")),n=input("请输入姓名")))
""" type函数可以返回值的类,isinstance函数判断是否属于指定的类,
   而且isinstance认为子类是父类的一种,而type不认为子类是父类的一种,instance第二个参数可以是元组 """
# print(isinstance(1.23,(float,int)))
"""使用del 变量1,变量2...  可以删除对象"""
""" 数字包括整数,浮点数,布尔值,复数;复数的虚部关键字j """
""" 数字0,空字符串"",空容器(空列表[]空字典{}空元组()空集合set()),None都是布尔值的False """
""" 列表标识符是中括号[] """
""" 元组标识符是小括号(),空元祖()内无需元素,一个元素的元组需要在元素后加逗号,如tup002_1,否则小括号会被识别为运算符号 """
str002="runoob";lis002=["a",1,3+2j];tup002=(str002,lis002,0);tup002_1=("a",);str002_1=("a")
# print(str002[0::2]);print(lis002[1:-1]);print(tup002[1]),print(tup002_1);print(type(str002_1))
""" 提示音转义符 """
# print("\a",end="")
""" 集合set和字典dictionary的标识符都是大括号{},其中空集合只能用set()函数赋值,而{}赋值的是空字典 """
""" 集合使用set函数赋值,则其参数必须是可迭代的,即必须是字符串或列表或元组,且只能是一个值或空值
   以下set003_1和set003_2就无法赋值 """
""" 集合是没有值的字典,而字典是成对二元元组的集合 """
""" 集合的元素是无序的,因此无法索引 """
""" 集合输出时,重复元素会被自动剔除 """
""" 集合常用于判断元素关系和删除重复元素 """
set003=set("123321")
set003_3=set("1214")
# set003_1=set(123)
# set003_2=set("1","2","3")
# print(set003)
""" 集合可以进行运算 """
""" 集合的差集,003集合存在而003_3不存在的元素 """
# print(set003 - set003_3)
""" 集合的并集 """
# print(set003 | set003_3)
""" 集合的交集 """
# print(set003 & set003_3)
""" 集合中不同时存在的元素 """
# print(set003 ^ set003_3)
# print(set003[0])
""" 字典的.item是由(键:值)成对组成的元组;字典也使用中括号[]索引,但不使用下标索引,使用键索引;
   键必须是唯一的,而且必须是不可变数据类型(数字或字符串或元组);
   字典的元素是键,遍历时,遍历字典的键,且无序排列,返回顺序不一 """
""" 字典元素的标识符是冒号:,因此可以用冒号赋值两个元素构造字典 """
""" 字典常用以下几种方式赋值 """
""" 例1空字典添加 """
dic004_1={}
dic004_1["one"]=1
dic004_1[2]="second"
# print(dic004_1)
""" 例2列表推导式 """
dic004_3={x:x**y for x in range(1,4) for y in range(1,4)}
# print(dic004_3)
""" dict函数的参数可以是成对赋值如例3,或者是元组组成的列表如例4,或者和zip函数嵌套如例5 """
""" 例3dict函数成对赋值,这种声明方式,键必须是字符串或元组(因为数字无法被赋值) """
""" 例3中使用变量赋值方式配对,因此不能是 '文本'=数字,这种方式是特殊方式,不常用 """
dic004_4 = dict(runoob=1,Google =2,淘宝=3)
# print(dic004_4)
""" 例4dict函数用成对二元元组作为元素的序列赋值,zip和enumerate函数嵌套都是这类赋值 """
dic004_2=dict([("雅蠛蝶",233),("stupid",1)])
# print(dic004_2["雅蠛蝶"])
""" 例5dict函数和zip函数嵌套赋值 """
""" python内置的map,zip,reversed,enumerate,sorted函数都是生成器函数,赋值时实际上没有任何运算
   当返回对象时通过序列转换函数或迭代才会实体化为序列,展开运算
   其中zip和enumerate只能使用tuple函数展开或即写即用,不能使用list和iter函数展开
   迭代使用时必须直接写入句子中,不能赋值为变量再代入,必须把函数直接写入语句中才能产生迭代
   特例: sorted自变量就是生成器,返回值也是生成器,可以直接展开 """
lis004_5_1=[1,2,3]
lis004_5_2=["谷歌","淘宝","企鹅","alibaba"]
tup004_5_3=(3,6,9)
tup004_5_4=(4,8,12)
""" zip函数生成一个zip对象,是多元成对元组作为元素的特殊序列 """
zip004_5_1=zip(lis004_5_1,lis004_5_2)
tup004_5_1=tuple(zip004_5_1)
# lis004_5_1z=list(next(zip004_5_1))
ite004_5_1=iter(zip004_5_1)
rev004_5_1=reversed(lis004_5_1)
lis004_5_1r=list(rev004_5_1)
zip004_5_2=zip(lis004_5_1,lis004_5_2,tup004_5_3,tup004_5_4) 
dic004_5_1=dict(zip004_5_1)
dic004_5_2={}
""" 以下示例中第1句,第2句有效,而第3句,第4句运算无效,zip和enu函数只能以tuple展开或即写即用(enumerate,map,reversed同理) """
# for k,v in zip(lis004_5_1,lis004_5_2):
# for k,v in tup004_5_1:
# for k,v in lis004_5_1z:
# for k,v in zip004_5_1:
   # dic004_5_2[k]=v
# print(dic004_5_2)+
# print(rev004_5_1)
# print(lis004_5_1r)
""" zip函数必须即写即用,所以以下第1句可行,而第2句无效 """
# print(next(zip(lis004_5_1,lis004_5_2)))
# print(next(zip004_5_1))
# print(dic004_5_1)
# print(dic004_5_2)
""" zip对象可以通过迭代或字典展开,无法直接展开 """
""" *rest关键字用于指代成对序列的剩余全部元素 """
# for x,y,*rest in zip004_5_2:
#    print(x,y,sep="@",end="\n")

""" zip函数用于把多个列表配对成成对元组作为元素的一维列表,其解压如下 """
tup004_a,tup004_b,*rest =zip(*(("a",1,3,7),("b",2,6,14),("c",3,9,21)))
# print(tup004_a,tup004_b,*rest)
""" reversed和sorted函数生成一个新的对象,也就是数值传递 """

""" 判断与循环 """
""" if...elif...else判断语句需要缩进 """
num005_1=3;num005_2=3
# if num005_1 > num005_2:
#    print("数字A大于数字B")
# elif num005_2 > num005_1:
#    print("数字A小于数字B")
# else:
#    print("数字A等于数字B")
""" while...else...循环是不定循环,因此可以无限循环,通过设定哨兵值参与循环,可以把不定循环修改成有限循环
   其中else语句在while条件false时执行 """
num005_3 = 1
# while num005_3 <10:
#    print(num005_3,end=" ")
#    num005_3 += 2
# else:
#    print("\n",num005_3,"大于或等于10")
""" for...in...else...循环是有限循环,用于遍历序列(iter)
   for循环中,else只在全部遍历之后才执行;循环异常中断break则不会执行 """
""" break终止循环;当有多层嵌套时,break只终止内层小循环 """
# for str005_1 in "asdfgh":
#    if str005_1 == "f":
#       break
#    print("发现文本",str005_1)
# else:
#    print("查找完毕")
""" continue不执行本轮循环剩余语句 """    
# for str005_2 in "asdfgh":
#    if str005_2 == "f":
#       continue
#    print("发现文本",str005_2,end=",")
# else:
#    print("查找完毕")

""" 迭代器与生成器 """
""" 使用iter函数可以把字符串,列表,元组,集合,字典生成迭代器,迭代器使用next函数只进不退
   可以使用iter函数的对象,称为可迭代对象
   各类序列必须要使用iter函数后才可以使用next函数迭代 """
lis006_1=[0,1,2,3,4]
ite006_1=iter(lis006_1)
# print(next(ite006_1),next(ite006_1),sep=",")
# for n in ite006_1:
   # print(n)
""" 自定义类中使用__iter__()和__next__()内置函数构造迭代器属性,详见自定义类 """
""" 自定义函数中使用yield关键字,可通过内置循环条件生成可迭代的yield对象,且不占用内存,详见自定义类
   这类自定义函数被称为生成器generator """
""" 推导式可以用于构造生成器,小括号()是标识符: (函数语句 for 变量范围 if 子句) 
   下例使用中括号[],则生成列表,而非表达式"""
gen006=(x*y for x in range(3) for y in range(3))
# print(next(gen006))
""" for...in 可迭代对象: 循环语句中使用有迭代属性的变量,会自动调用next函数,类似for... in... iter(序列) """

""" 内置函数和自定义函数 """
""" 不可变对象(数字,字符串,元组)的运算和赋值相当于VBA的值传递,原有变量不会被函数运算重新赋值;
   可变对象赋值和运算都是引用传递,与函数共享同一内存指针,对象会在函数运算后被重新赋值 """
""" 函数没有return,返回值是None """
""" 自定义函数时,可以声明缺省参数,如本例中的l参数和n参数,如有非默认参数,则默认参数必须放在函数定义语句的最后
   加*的参数是不定长参数,类似VBA的可选参数,加一个*,参数以元组类型代入,如本例m参数;
      加两个*,参数必须以键=值的方式输入,且返回值也是字典形式
   在引用函数时,不定长参数之后的参数必须使用索引名赋值,如本例n参数 """
""" 自定义函数最好以return结尾,而且python中return可以返回多个值 """
def double_aster(**a):
   print(a)
# double_aster(b=2,c=5)
def fibo(l=100,*m,n=100):
   a,b=0,1
   list_fibo=[]
   n = int(n)
   while b<l+n:
      list_fibo.append(b)
      a,b=b,a+b 
   # print(m)
   return list_fibo
""" 交叉赋值,同时赋值是python特色之一 """
""" 本例中第3参数n必须使用索引名赋值 """
# print(fibo(100,n=1))
""" map函数两个参数,第一个是内嵌函数,后面是内嵌函数所有参数的迭代器,map函数会遍历迭代器,分别代入
   (函数参数不能空,但可以是None,以最短参数序列为准),
   并按第一个原序列的数据类型和返回值生成一个map对象
   map对象不是序列,可以用tuple,list,iter展开 """
map008=map(fibo,[100,200,300],(None,1),(None,None))
# lis008=list(map008)
# tup008=tuple(map008)
# ite008=iter(map008)
# print(next(ite008),next(ite008))
# print(tup008[0][0:-3:-1])
# print(lis008)
""" 模块 """
""" 只有包含__init__.py模块的文件夹才会被python认定为包,以免识别其他文件 """
""" 包和模块有两种引入方式,即:import 模块 和 from 模块 import 函数 ;
其中import 函数名 from 模块 可以直接调用函数名,无需 包名.模块.函数 的方式调用函数
但是后引入的函数会覆盖之前引入的同名函数,因此不推荐此方法引入函数"""
import sys
""" 引入函数以后,可以通过赋值的方式(函数无需加参数括号),对函数进行重命名,以减小代码量 """
""" sys.path属性返回python引入包和模块的所有路径,第一个路径永远是当前py文件所在的文件夹
可以通过sys.path.append(模块路径)的方式手动添加模块路径 """
sp = sys.path
fb = fibo
# print(sp)
""" dir函数返回包或模块或函数所有自定义的关键字 """
# print(dir(fb))
# fb()

""" enumerate函数可以把列表或元组的索引序数和元素成对对应成类似字典键:值的关系的元组,默认从0开始索引
   enumerate函数只能用tuple展开或即写即用,类似zip函数 """
str008_1="asdfgh"
enu008_1=enumerate(str008_1)
tup008_1=tuple(enu008_1)
lis008_1=list(enu008_1)
ite008_1=iter(enu008_1)
dic008_1={i:ele for i,ele in enu008_1}
""" 无法遍历提前生成的enumerate对象,只能即写即用函数结果 """
# for k,v in enumerate("asdf"):
#    print(k)
# for k in enumerate("asdf"):
#    print(k)

# for k,v in tup008_1:
# for k,v in lis008_1:
# for k,v in ite008_1:
#    print(k)
   # print(next(k))
# for k,v in dic008_1.items():
#    print(k,v)
""" lambda 变量1,变量2,变量3... : 表达式 语句用于创建简单的匿名函数,仅可以使用自身参数变量 """
sm = lambda x,y,z : x+y+z
""" lambda也可以用于柯里化currying一个已有函数,固定其中某个参数,以生成新函数 """
sm_1=lambda x : sm(1,1,x)
# print(sm(1,2,3))
# print(sm_1(1))
""" Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，
   其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，
   也就是说这些语句内定义的变量是全局变量，外部也可以访问 """
""" python按照LEGB的顺序查找变量,Local局域作用域,Enclosing内嵌函数的外包函数的作用域,Global全局作用域,Builtin内置作用域(内置函数所在模块) """
# if True:
#    msg008="welcome"
# print(msg008)
""" nonlocal关键字可以使内嵌引用外包函数的变量,而且是引用传递,会改变该变量的值 """
""" global关键字可以使函数直接引用外部的全局变量 """
glo008_1=1
def out008():
   global glo008_1
   num = glo008_1
   def in008():
      nonlocal num
      num=num+2
   print(num*2,in008(),num*2)
   return
# out008()
""" help函数是内置函数,返回数据类型或函数或模块的详细说明 """
# help(print)
""" yield保留字让自定义函数返回值是可迭代的生成器generator,而且不像list那样占用内存
   return保留字不会保留前次执行后的变量值,因此不可迭代 """
def feb001(max):
   n,a,b = 0,0,1
   while n < max:
      yield b
      a,b = b, a+b
      n = n +1
feb001_2=feb001(5)
# print(next(feb001_2),next(feb001_2),sep=",")
""" 一个迭代器只能使用一次,已经输出的迭代元素,无法再次输出 """
# for n in feb001_2:
#    print(n)

""" 数据结构 """
""" 列表可以使用.append方法和.pop方法使其成为堆栈stack(后进先出) """
""" 列表可以使用.append方法和.popleft方法使其成为队列queue(先进先出) """
""" 列表可以使用.clear方法清空,也可以使用del 列表[:] 删除全索引的方式清空 """
""" reversed函数倒转序列 """
""" sorted函数生成排序的序列 """

""" 自定义类 """
""" 注释不要打断缩进关系树,如本例中从class下穿和def连接def的纵线 """
""" 自定义类的外部参数在init函数中赋值,并参与类的方法参与运算 """
class Vector:
   """ 自定义类的方法第一个参数是方法的实例自身,惯例命名为self,不推荐随意命名 """
   """ 自定义类有若干内置的私有方法和属性,即使没有声明也可以内部调用,包括init,class,name,main """
   """ __init__内置属性用于自定义类的初始化,并限定其参数 """
   def __init__(self, a, b):
      self.a = a
      self.b = b
   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)
   """ 注释只能与代码块主句对齐,不能与子句缩进 """
   """ 运算符重载也是内置的私有方法,使得类可以按照自定义的方法使用类的基础运算符
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
""" 文件引用自身内置属性和方法,无需前缀,__name__属性永远是__main__ 
   由于模块第一次被引入时模块的主程序main必定会被执行
   在自定义类时,可以通过判断name属性是否为main,限定类只能在模块被整体引入时才能执行 """
# print(__name__)
""" 类的私有属性和方法以双下划线开头,实例的私有属性无法被实例从外部调用,但是类的私有属性可以被外部调用 """
# print(v1.__class__.__name__)
# v1.prt()
""" 自定义类使用__iter__,__next__内置函数,使自定义类具备迭代属性 """
class iteration001:
   """ 自定义类中,参数必须赋值为self.属性才能参与其他函数运算,无论该参数是否是私有参数 """
   def __init__(self,y=1,x=5):
      self.y = y
      self.x = x
      self.a = 0
   """ 即使无返回值,函数最好以return语句结尾;自定义类中,如果无返回值,只是定义私有属性,则return self """  
   def __iter__(self):
      return self
   """ 本例中使用条件语句触发raise stopiteration终止迭代 """
   """ python3中,迭代器不再有.next属性,只有next函数,所以只能使用__next__私有属性,而非可以被外部调用的.next公有属性 """
   """ 本例中迭代返回值是self.a计数器 """
   def __next__(self):
      if self.a <self.x * self.y:
         x = self.a
         self.a += self.y
         return x
      else:
         raise StopIteration

cls001=iteration001(1,5)
ite008_1=iter(cls001)
# print(next(ite008_1),next(ite008_1),sep=",")
# for x in ite008_1:
#    print(x,end=",")
""" 自定义子类可以同时继承多个父类的函数,如果子类的自定义函数与父类相同,则子类的函数覆盖父类,
   多继承的父类函数重名时,默认继承括号内排前的父类函数
   super函数可以调用子类的父类同名函数 """
""" 以下示例中展示了format函数的和字典对象的联用,format函数和序列对象的联用 """
class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))
class student(people):
    grade = ''
    def __init__(self,n,a,w,g):
        #调用父类的构函
        people.__init__(self,n,a,w)
        self.grade = g
    #覆写父类的speak方法
    def speak(self):
        #本例中大括号{}内第一个0不可省略,表示format的参数索引序数
        print("{0[0]} 说: 我 {0[1]} 岁了，我在读 {0[2]} 年级".format([self.name,self.age,self.grade]))
class speaker():
    topic = ''
    name = ''
    def __init__(self,n,t,a):
        self.name = n
        self.topic = t
        self.age=a
        self.properties008={"q":self.name,"w":self.topic,"e":self.age}
    def speak(self):
        print("我叫 {q}，我今年{e}岁,是一个演说家，我演讲的主题是 {w}".format(**self.properties008))
""" 由于大括号{}内的索引返回的是带括号的文本,所以上例中字典无法以数字作为键来进行索引 """
class sample(student,speaker):
# 切换不同顺序则父类不同
# class sample(speaker,student):
   #  a =''
    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t,a)
test = sample("Tim",25,80,4,"Python")
""" 方法名同，默认调用的是在括号中排前地父类的方法 """
# test.speak()
""" super函数第一个参数是变量的子类,第二个参数是变量,使用后返回一个以子类参数为参数的父类对象 """
# super(sample,test).speak()

""" 输入与输出 """
""" print输出用户易读的字符串(不带引号),repr输出程序易读的字符串(带引号) """
str009_1="asd"
# print(str009_1)
# repr(str009_1)
""" 按指定格式输出 """
""" 字符串.rjust方法右对齐,字符串.ljust方法左对齐,字符串.center方法居中对齐 """
# for x in range(1,11,1):
#    print(repr(x).rjust(2),repr(x*x).rjust(3),end=" ")
#    print(repr(x**3).rjust(4))
# for x in range(1,11,1):
#    print("{:2d} {:3d} {:4d}".format(x,x**2,x**3))

""" 代码改进与优化 """
""" 代码由于经常出现bug,需要设置某些错误处理语句 """
div = lambda y:1/y
""" except从句仅在try子句出错时,根据错误类型执行except子句 """
""" as从句用于别名 """
""" 不带错误类型的except子句必须放在所有except子句最后,对未声明的错误类型进行兜底 """
""" 仅当try子句无异常执行完毕时,执行else子句 """
""" 无论try从句是否异常,finally从句都会执行,所以必须放在最后 """
# try:
#    print(div(int(input())))
# except ZeroDivisionError as err:
#    print("请不要输入0",err)
# except:
#    print("请勿输入字符串")
# else:
#    print("一切正常")
# finally:
#    print("over")
""" 当使用某个打开后必须要关闭的对象(主要是file对象)时,使用with语句可以简化代码 """

""" 数据分析入门 """
import numpy as np 
# import matplotlib.pyplot as plt 
import pandas as pd
from pandas import Series as sr,DataFrame as df
# import seaborn as sns
# import statsmodels as sm
""" 自定义isiterable函数以后使用 """
def isiterable(ele):
   try:
      iter(ele)
      return True
   except TypeError:
      return False

# print(isiterable(55))
# print(isiterable(str(55)))

""" pandas学习 """
""" numpy入门 """
arr101_0=np.arange(32).reshape(8,4)
# print(arr101_0)
""" ndarray是自定义数据类型容器,不是列表,也不是元组,不继承列表和元组方法
   ndarray的形状遵循由外到内的表示,数轴的顺序0开始,0轴表示最外层维度,(8,4)表示0轴8行,1轴4列的数组 """
# print(arr101_0.dtype)
# print(arr101_0.shape)
""" 使用ndarray.astype方法可以更改ndarray对象的dtype数据类型 """
arr101_1=arr101_0.astype(np.float64)
# print(arr101_1.dtype)
""" ndarray对象切片截取时,是引用传递,所有更改会反映到数据源
   多维数组的索引以逗号作为标识符区分维度(也可以类似普通序列多个[]多步常规索引),冒号作为头标:尾标:步长的标识符 """
arr101_1[0:3:2,2:]=0.0000
# print(arr101_1[0:3:2])
""" ndarray对象可以使用布尔值进行索引,只有True值会被索引出来 """
arr101_a = np.array(list("asdf"*2))
# print(arr101_a)
# print(arr101_0[arr101_a=="a"])
""" 波浪符~用于反义操作,两次反义操作得到相同结果 """
arr101_a_1= arr101_a != "a"
# print(arr101_0[~arr101_a_1])
""" 布尔型ndarray中and和or保留字无效,只能使用&和|字符,且条件用小括号间隔开 """
# print(arr101_0[(arr101_a=="a") | (arr101_a == "f")])
""" ndarray有T属性和transpose属性两种方式转置 """
# print(arr101_1.T)
# print(arr101_1)
""" 多维函数一般用transpose属性,指定转置轴的位置 """
# print(arr101_1.transpose(1,0))
# print(arr101_1)
""" ndarray的专用np函数称为ufunc,会把计算方式传播给数组内每一个值,ufunc可以设置参数,使其变为引用传递,就地运算 """
# print(np.sqrt(arr101_1))
""" np.where(判断式,真值运算,假值运算)函数就是数组的if函数 """
# print(np.where(arr101_1==0,arr101_0,arr101_1))
# print(arr101_1)
""" np.unique函数可以清除重复值 """
# print(np.unique(np.array(list("asdasdf"))))
""" 整行或整列作为从参数进行统计分析的函数称为聚合函数(约简函数),以及以特定轴为方向的累积函数 """
""" np.save函数保存单个ndarray为npy文件,np.load可以加载该文件 """
""" np.savez保存多个ndarray为一个npy文件,且以类似字典的对象保存 """
""" np.savez_compressed压缩保存多个ndarray """
""" 随机漫步示例 """
# nwalks = 5000
# nsteps = 1000
# draws = np.random.randint(0, 2, size=(nwalks, nsteps)) # 0 or 1
# steps = np.where(draws > 0, 1, -1)
# walks = steps.cumsum(1)
# plt.plot(walks[:50])

""" pandas入门 """
""" series是dataframe的基本组成单元,即使是dataframe的横向行series,输出时也是纵向显示 """
""" series和dataframe的索引都是不可变数据类型,只能reindex数值传递(复制运算),不能引用传递(就地运算) """
""" pandas.Series类似zip函数构造的有序字典,缺省为数字索引,可以由序列或字典构造,其中字典的键会成为索引 """
""" 当键多于值时,series会复制填充 """
sr102_1=sr(list("qwer"),index=list("asdf"))
sr102_2=sr(dict(zip(list("qwer"),list("asdfgh"))))
# print(sr102_1)
# print(sr102_2)
""" series是值参与运算,键只作为索引 """
# print(sr102_1.values)
# print(sr102_1.index)
""" series和pandas的中括号索引都是前闭后闭的索引,容易与python内置索引产生歧义,且索引不唯一,因此尽量用.loc属性索引 """
# print(sr102_1["a":"f"])
""" series和pandas运算时都是元素级运算,会根据索引对齐,无法对齐部分,填充为NAN值,即无效值 not a number """
sr102_3=sr(np.arange(5))
sr102_4=sr(np.arange(3))
# print(sr102_3+sr102_4)
""" ndarray,列表作为df参数,不转置 """
df102_8=df(np.arange(3).reshape(3,1),index=list("qwe"))
# p(df102_8)
df102_9=df(np.arange(3).reshape(1,3),columns=list("asd"))
# p(df102_9)
df102_5=df(np.arange(20).reshape(5,4),index=list("qwert"),columns=list("asdf"))
# p(df102_5)
df102_10=df([[1,2,3],[4,5,6]],index=list("qw"),columns=list("asd"))
# p(df102_10)
df102_12=df(sr102_3,sr102_4)
# p(df102_12)
""" 只有字典才会转置为列 """
df102_11=df({"a":range(3),"s":range(3),"d":range(3)})
# p(df102_11)
""" df添加列就是直接赋值新的df列索引,无法对齐的空值会被填充nan """
df102_5["g"]=sr(range(3),index=list("qwe"))
# p(df102_5)
del df102_5["g"]
# p(df102_5)
""" 双层嵌套字典构造df,外层字典的键作为列索引,内层字典是行索引 """
df102_6=df({0:{1:"a",2:"s",3:"f"},4:{1:"q",2:"w",3:"e"}})
""" df也可以使用.T属性转置 """
# p(df102_6);p(df102_6.T)
""" pd的columns和index都是不可变的,一旦初始确定即不再改变,后续只能reindex,所以以下语句错误 """
# df102_5.columns[0]="z"
# df102_5.index[0]="x"
df102_7=df(np.arange(3),index=list("aaa"))
# p(df102_7[0])
""" df的中括号[]普通索引只能索引列,不能索引行,索引行和添加行或者定点索引只能使用.loc属性,参数用中括号 """
# df102_5.loc["q"]=0
""" 添加行 """
# df102_5.loc["y","d"]=0
# df102_5.loc["e":"t","a":"s"]=np.nan
""" 花式索引是数组索引,中括号[]是花式索引标识符,
所以不能使用冒号:划出头标尾标进行范围索引,范围索引只能是普通索引 """
# df102_5.loc[["e","r","t"],["a","s"]]=0
# p(df102_5)
""" series和df运算时都会自动对齐,
   df.apply应用聚合函数,累积函数和一般函数时,代入函数的参数是df的series
   默认按列代入,默认参数为axis=0(axis="index")传播,可以设置为按axis=1/axis="columns"传播 """
""" 如果是仅有df自身series作为参数的函数,则axis参数表示迭代的轴方向
   如果是df和series,或者索引作为参数的方法函数,则axis参数表示series对齐的方向,或是索引查找的方向 """
df_max=lambda x :x.max()
df102_5.columns.name="列"
df102_5.index.name="行"
# p(df102_5)
p(df102_5.apply(df_max,axis="index"))
p(df102_5.apply(df_max,axis=1))
# p(df102_5.cumsum())
# p(df102_5.cumsum(axis=1))
""" 元素级函数使用.applymap方法,常用的numpy元素函数ufunc也可以用于df对象 """
# p(np.sqrt(df102_5))
df_fmt=lambda x : "{:f}".format(x)
# p(df102_5.applymap(df_fmt))
""" reindex可以重设行索引和列索引排序,会自动创建新旧索引无法对齐的部分
   且可以通过fill_value参数指定填充值 """
""" df和df的计算函数,都可以设置fill_value参数 """
# p(df102_5.reindex(index=list("ytrewq"),fill_value=233))
""" df和series运算时,默认axis=1 """
# sr102_5=sr(np.arange(4),index=list("asfg"))
sr102_5=sr(np.arange(4),index=list("qwey"))
# p(df102_5.sub(sr102_5))
p(df102_5.sub(sr102_5,axis=0))
# p(df102_5.sub(sr102_5,axis=1))
# p(df102_5+sr102_5)
""" 按行index方向对齐索引"q",所以axis=0
   df的属性,默认inplace=False数值传递,复制运算,改为True之后,就地运算 """
# df102_5.drop("q",axis=0,inplace=True)
# df102_5.drop("a",axis=1,inplace=False)
# p(df102_5)