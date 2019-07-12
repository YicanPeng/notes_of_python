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
# str000="runoob"
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
# num001=1234;str001="runoob";tup001=(num001,str001,0)
"""推导式语句: 自变量表达式 for 自变量1 in 范围1 if 条件句1 自变量2 in 范围2 if 条件句2 
   推导式语句中 for...in...if... 相当于定语(状语)从句,因此多个并列子句不能加逗号隔开;
   多个for子句的嵌套遵循相同的for循环运算顺序,即外部大循环在前而内部小循环在后;
   python中多个变量逗号仅用于同步成对元素的同时赋值,详见zip函数和enumerate函数"""
""" range函数的头标是0,左闭右开区间 """
# lis001_1=[x+y+z for x,y,z in zip(range(3),range(3),range(3)) ]
# num001[0]=5
# str001[0]="x"
# tup001[0]="a"
# print(tup001[1][0])
# print(lis001_1) 
# print(len(lis_001))
# num002_0,num002_1,num002_2,num002_3,num002_4,num002_5="abcdefg"[0:-1]
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
# str002="runoob";lis002=["a",1,3+2j];tup002=(str002,lis002,0);tup002_1=("a",);str002_1=("a")
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
# set003=set("123321")
# set003_3=set("1214")
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
""" 字典用大括号{}或dict函数赋值 """
""" 例1空字典添加 """
# dic004_1={}
# dic004_1["one"]=1
# dic004_1[2]="second"
# print(dic004_1)
""" 例2列表推导式 """
# dic004_3={x:x**y for x in range(1,4) for y in range(1,4)}
# print(dic004_3)
""" dict函数的参数接受成对赋值如例3,
   元组组成的序列如例4
   和zip或enumerate函数嵌套如例5 """
""" 例3dict函数成对赋值,这种声明方式,键必须是字符串或元组(因为数字无法被赋值) """
""" 例3中配对变量赋值方式, 罕见"""
# dic004_4 = dict(runoob=1,Google=2,淘宝=3)
# print(dic004_4)
""" 例4dict函数用成对二元元组作为元素的序列赋值,zip和enumerate函数嵌套都是这类赋值 """
# dic004_2=dict((("雅蠛蝶",233),("stupid",1)))
# p(dic004_2)
""" 例5dict函数和zip函数嵌套赋值 """
""" python内置的map,zip,reversed,enumerate,sorted函数都是生成器函数,赋值时实际上没有任何运算
   必须通过序列转换函数或迭代才会实体化展开为序列
   其中zip和enumerate只能使用tuple函数展开或即写即用,不能使用list和iter函数展开
   迭代使用时必须直接写入句子中,不能赋值为变量再代入,必须把函数直接写入语句中才能产生迭代
   特例: sorted自变量就是生成器,返回值也是生成器,可以直接展开 """
# lis004_5_1=[1,2,3]
# lis004_5_2=["谷歌","淘宝","企鹅","alibaba"]
# tup004_5_3=(3,6,9)
# tup004_5_4=(4,8,12)
""" zip函数生成一个zip对象,是多元成对元组组成的特殊对象 """
# zip004_5_1=zip(lis004_5_1,lis004_5_2)
# tup004_5_1=tuple(zip004_5_1)
# lis004_5_1z=list(next(zip004_5_1))
# ite004_5_1=iter(zip004_5_1)
# rev004_5_1=reversed(lis004_5_1)
# lis004_5_1r=list(rev004_5_1)
# zip004_5_2=zip(lis004_5_1,lis004_5_2,tup004_5_3,tup004_5_4) 
# dic004_5_1=dict(zip004_5_1) 
# p(dic004_5_1) #输出为空
# dic004_5_2={}
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

""" zip函数用于把多个列表配对成成对元组作为元素的一维列表,,其解压方式有两种 """
""" 对于zip对象,zip解压会按照外部维度解压 """
# zip004_5_3=zip(list("asd"),(1,2,3),list("qwe"))
# dic004_5_3={k:0 for k in zip(*zip004_5_3)}
# p(dic004_5_3)
""" 对于二维列表或元组,zip会在内部维度垂直解压 """
# zip004_5_4=[list("asd"),(1,2,3),list("qwe")]
# dic004_5_4={k:0 for k in zip(*zip004_5_4)}
# p(dic004_5_4)
""" 以下示例也是垂直解压,*rest表示剩余部分 """
# tup004_a,tup004_b,*rest =zip(*(("a",1,3,7),("b",2,6,14),("c",3,9,21)))
# print(tup004_a,tup004_b,*rest)

""" reversed和sorted函数生成一个新的对象,也就是数值传递 """

""" 判断与循环 """
""" if...elif...else判断语句需要缩进 """
# num005_1=3;num005_2=3
# if num005_1 > num005_2:
#    print("数字A大于数字B")
# elif num005_2 > num005_1:
#    print("数字A小于数字B")
# else:
#    print("数字A等于数字B")
""" while...else...循环是不定循环,因此可以无限循环,通过设定哨兵值参与循环,可以把不定循环修改成有限循环
   其中else语句在while条件false时执行 """
# num005_3 = 1
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
# lis006_1=[0,1,2,3,4]
# ite006_1=iter(lis006_1)
# print(next(ite006_1),next(ite006_1),sep=",")
# for n in ite006_1:
   # print(n)
""" 自定义类中使用__iter__()和__next__()内置函数构造迭代器属性,详见自定义类 """
""" 自定义函数中使用yield关键字,可通过内置循环条件生成可迭代的yield对象,且不占用内存,详见自定义类
   这类自定义函数被称为生成器generator """
""" 推导式可以用于构造生成器推导式,小括号()是生成器标识符: (函数语句 for 变量范围 if 子句) 
   下例使用中括号[],则生成列表,而非生成器"""
# gen006=(x*y for x in range(3) for y in range(3))
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
""" 调用函数时,不带括号则调用的是函数对象;带括号调用,则调用的是函数单次运行的结果(如果有必要参数则必须输入参数) """
# def double_aster(**a):
   # print(a)
# double_aster(b=2,c=5)
# def fibo(l=100,*m,n=100):
   # a,b=0,1
   # list_fibo=[]
   # n = int(n)
   # while b<l+n:
      # list_fibo.append(b)
      # a,b=b,a+b 
   # print(m)
   # return list_fibo
""" 交叉赋值,同时赋值是python特色之一 """
""" 本例中第3参数n必须使用索引名赋值 """
# print(fibo(100,n=1))
""" map函数两个参数,第一个是内嵌函数,后面是内嵌函数所有参数的迭代器,map函数会遍历迭代器,分别代入
   (函数参数不能空,但可以是None,以最短参数序列为准),
   并按第一个原序列的数据类型和返回值生成一个map对象
   map对象不是序列,可以用tuple,list,iter展开 """
""" map函数常与lambda隐函数联用 """
# map008=map(fibo,[100,200,300],(None,1),(None,None))
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
# import sys
""" 引入函数以后,可以通过赋值的方式(函数无需加参数括号),对函数进行重命名,以减小代码量 """
""" sys.path属性返回python引入包和模块的所有路径,第一个路径永远是当前py文件所在的文件夹
可以通过sys.path.append(模块路径)的方式手动添加模块路径 """
# sp = sys.path
# fb = fibo
# print(sp)
""" dir函数返回包或模块或函数所有自定义的关键字 """
# print(dir(fb))
# fb()

""" enumerate函数可以把列表或元组的索引序数和元素成对对应成类似字典键:值的关系的元组,默认从0开始索引
   enumerate函数只能用tuple展开或即写即用,类似zip函数 """
# str008_1="asdfgh"
# enu008_1=enumerate(str008_1)
# tup008_1=tuple(enu008_1)
# lis008_1=list(enu008_1)
# ite008_1=iter(enu008_1)
# dic008_1={i:ele for i,ele in enu008_1}
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
""" lambda函数注意与推导式区分:
   lambda函数自变量参数在前,冒号连接,表达式在后
   推导式表达式在前,for 定义域在后 """
"""列表推导式语句:[表达式 for 自变量1 in 范围1 if 条件句1 自变量2 in 范围2 if 条件句2] """
sm = lambda x,y,z : x+y+z
""" lambda也可以用于柯里化currying一个已有函数,固定其中某个参数,以生成新函数 """
# sm_1=lambda x : sm(1,1,x)
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
# glo008_1=1
# def out008():
#    global glo008_1
#    num = glo008_1
#    def in008():
#       nonlocal num
#       num=num+2
#    print(num*2,in008(),num*2)
#    return
# out008()
""" help函数是内置函数,返回数据类型或函数或模块的详细说明 """
# help(print)
""" yield保留字让自定义函数返回值是可迭代的生成器generator,而且不像list那样占用内存
   return保留字不会保留前次执行后的变量值,因此不可迭代 """
# def feb001(max):
#    n,a,b = 0,0,1
#    while n < max:
#       yield b
#       a,b = b, a+b
#       n = n +1
# feb001_2=feb001(5)
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
# class Vector:
   # """ 自定义类的函数第一个参数是方法的实例自身,惯例命名为self,不推荐随意命名 """
   # """ 自定义类有若干内置的私有方法和属性,即使没有声明也可以内部调用,包括init,class,name,main """
   # """ 私有方法以双下划线开头__私有名称__双下划线结尾 """
   # """ __init__内置属性用于自定义类的初始化,并限定其参数 """
   # def __init__(self, a, b):
   #    self.a = a
   #    self.b = b
   # def __str__(self):
   #    return 'Vector (%d, %d)' % (self.a, self.b)
   # """ 注释只能与代码块主句对齐,不能与子句缩进 """
   # """ 运算符重载也是内置的私有方法,使得类可以按照自定义的方法使用类的基础运算符
   # 本例为使用加号运算符 """
   # def __add__(self,other):
   #    return Vector(self.a + other.a, self.b + other.b)
   # """ self参数代表的是类的实例(也就是变量),而非类本身 """
   # def prt(self):
   #    print(self)
   #    print(self.__class__)
   #    print(self.__str__.__doc__)
""" 自定义类的第一个参数必须是实例本身,即使是无参方法,也必须声明实例本身作为参数 """
""" 自定义类从第二个参数开始,才是真正的参数 """
# v1 = Vector(2,10)
# v2 = Vector(5,-2)
# v3 = Vector(1,2)
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
# class iteration001:
   # """ 自定义类中,参数必须赋值为self.属性才能参与其他函数运算,无论该参数是否是私有参数 """
   # def __init__(self,y=1,x=5):
      # self.y = y
      # self.x = x
      # self.a = 0
   # """ 即使无返回值,函数最好以return语句结尾;自定义类中,如果无返回值,只是定义私有属性,则return self """  
   # def __iter__(self):
      # return self
   # """ 本例中使用条件语句触发raise stopiteration终止迭代 """
   # """ python3中,迭代器不再有.next属性,只有next函数,所以只能使用__next__私有属性,而非可以被外部调用的.next公有属性 """
   # """ 本例中迭代返回值是self.a计数器 """
   # def __next__(self):
      # if self.a <self.x * self.y:
         # x = self.a
         # self.a += self.y
         # return x
      # else:
         # raise StopIteration

# cls001=iteration001(1,5)
# ite008_1=iter(cls001)
# print(next(ite008_1),next(ite008_1),sep=",")
# for x in ite008_1:
#    print(x,end=",")
""" 自定义子类可以同时继承多个父类的函数,如果子类的自定义函数与父类相同,则子类的函数覆盖父类,
   多继承的父类函数重名时,默认继承括号内排前的父类函数
   super函数可以调用子类的父类同名函数 """
""" 以下示例中展示了format函数的和字典参数的联用,format函数和列表参数的联用 """
# class people:
    #定义基本属性
   #  name = ''
   #  age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
   #  __weight = 0
    #定义构造方法
   #  def __init__(self,n,a,w):
      #   self.name = n
      #   self.age = a
      #   self.__weight = w
   #  def speak(self):
   #      print("%s 说: 我 %d 岁。" %(self.name,self.age))
# class student(people):
   #  grade = ''
   #  def __init__(self,n,a,w,g):
        #调用父类的构函
      #   people.__init__(self,n,a,w)
      #   self.grade = g
    #覆写父类的speak方法
   #  def speak(self):
        #本例中大括号{}内第一个0不可省略,表示format的参数索引序数
      #   print("{0[0]} 说: 我 {0[1]} 岁了，我在读 {0[2]} 年级".format([self.name,self.age,self.grade]))
# class speaker():
#     topic = ''
#     name = ''
#     def __init__(self,n,t,a):
#         self.name = n
#         self.topic = t
#         self.age=a
      #   self.properties008={"q":self.name,"w":self.topic,"e":self.age}
   #  def speak(self):
      #   print("我叫 {q}，我今年{e}岁,是一个演说家，我演讲的主题是 {w}".format(**self.properties008))
""" 文本.format函数,文本内大括号{}如果是数字索引,则仅是format参数的位置索引,不能作为参数标识符 """
""" 此处使用双**号使参数以字典的形式引入函数中 """
# class sample(student,speaker):
# 切换不同顺序则父类不同
# class sample(speaker,student):
   #  a =''
   #  def __init__(self,n,a,w,g,t):
      #   student.__init__(self,n,a,w,g)
      #   speaker.__init__(self,n,t,a)
# test = sample("Tim",25,80,4,"Python")
""" 方法名同，默认调用的是在括号中排前的父类的方法 """
# test.speak()
""" super函数第一个参数是变量的子类,第二个参数是变量,使用后返回一个以子类参数为参数的父类对象 """
# super(sample,test).speak()

""" 输入与输出 """
""" print输出用户易读的字符串(不带引号),repr输出程序易读的字符串(带引号) """
# str009_1="asd"
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
# div = lambda y:1/y
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
import matplotlib.pyplot as plt 
plt_font = {'family' : 'SimHei',
        'weight' : 'bold',
        'size'   : '12'}
plt.rc('font', **plt_font)               # 步骤一（设置字体的更多属性）
plt.rc('axes', unicode_minus=False)  # 步骤二（解决坐标轴负数的负号显示问题）
import pandas as pd
from pandas import Series as sr,DataFrame as df
import seaborn as sns
import statsmodels as sm
""" 自定义isiterable函数以后使用 """
def isiterable(ele):
   try:
      iter(ele)
      return True
   except TypeError:
      return False

""" 番外篇:装饰器 """
""" 装饰器用于在不改变已有函数内部结构的前提下,把原函数作为参数嵌套进装饰器函数中,函数原地重命名 """
""" 装饰器函数必须闭包,所以1.装饰器必须内嵌函数,2.return内嵌函数3.return内嵌函数不加括号 """
""" 本例中通过添加*和**,使得装饰器可以装饰在有任意类型参数的函数上 """
# def greet001(b="王凤"):   
#    def middle(f):
#       def inner(*x,**y):
#          p("Hello",b,sep=",",end="!\n")
#          f(*x,**y)
#       return inner
#    return middle
# """  """
# def self_introduce001(a="彭义灿"):
#    p("My name is {}!".format(a))

""" 不使用语法糖,则相当于外套函数原地赋值 """
""" 第二个括号内是函数名作为参数,不是运行self_introduce001函数;
   向自定义函数内嵌函数传递参数,通过第二个括号完成 """
# self_introduce001=greet001("Orris")(self_introduce001)
# self_introduce001("Ethan")
""" 使用语法糖只是简化代码书写的技巧,不是装饰器的实质 """
# @greet001("Ethan")
# def self_introduce002(a="彭义灿"):6
#    print("My name is {}!".format(a))
# # self_introduce002("Orris")

# print(isiterable(55))
# print(isiterable(str(55)))

""" pandas学习 """
""" numpy入门 """
""" np.array函数参数可以是列表或元组或range(包括np.arange) """
# arr101_0=np.array(np.arange(32).reshape(8,4))
# print(arr101_0)
""" ndarray是自定义数据类型,不是列表,也不是元组,不继承列表和元组方法
   ndarray的形状遵循由外到内的表示,数轴的顺序0开始,0轴表示最外层维度,(8,4)表示0轴8行,1轴4列的数组 """
# print(arr101_0.dtype)
# print(arr101_0.shape)
""" 使用ndarray.astype方法可以更改ndarray对象的dtype数据类型 """
# arr101_1=arr101_0.astype(np.float64)
# print(arr101_1.dtype)
# arr101_1=arr101_1.astype(np.int16)
""" ndarray对象切片截取时,是引用传递,所有更改会反映到数据源
   多维数组的索引以逗号作为分割维度的标识符(也可以类似普通序列多个[][]常规索引),冒号作为头标:尾标:步长的标识符 """
# arr101_1[0:3:2,2:]=0
# print(arr101_1[0:3:2])
""" ndarray对象可以使用其他等长ndarray的布尔值进行索引,只有True值会被索引出来 """
# arr101_a = np.array(list("asdf"))
# print(arr101_a=="a")
""" 索引长度为4的arr101_0的第二个维度 """
# print(arr101_0[:,arr101_a=="a"])
""" 波浪符~用于反义操作,两次反义操作得到相同结果 """
# arr101_a_1= arr101_a != "a"
# print(arr101_0[~arr101_a_1])
""" 布尔型ndarray中and和or保留字无效,只能使用&和|字符,且条件用小括号间隔开 """
# print(arr101_0[(arr101_a=="a") | (arr101_a == "f")])
""" 花式索引是列表索引,是逐个索引,因此无法用冒号进行切片范围索引 """
# print(arr101_0[[1,2,3],[1,2,3]])
# print(arr101_0[[1,2,3]][:,1:3])
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
""" np.unique函数可以清除重复值(pd.unique同理) """
# print(np.unique(np.array(list("asdasdf"))))
""" 统计函数又称聚合函数,约简函数 """
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
""" series和dataframe的索引都是不可变数据类型,只能reindex数值传递(复制运算) """
""" series和dataframe的对齐功能,类似数据库的join,根据键进行匹配 """
""" pandas.Series函数类似zip函数构造的有序字典,缺省则为数字索引,可以接受序列或字典,其中字典的键会成为索引 """
""" 当键多于值时,series会复制填充 """
# sr102_1=sr(list("qwer"),index=list("asdf"))
# sr102_2=sr(dict(zip(list("qwer"),list("asdfgh"))))
# print(sr102_1)
# print(sr102_2)
""" series是值参与运算,键只作为索引 """
# print(sr102_1.values)
# print(sr102_1.index)
""" series和df的中括号索引都是前闭后闭的索引,容易与python内置索引产生歧义,且索引不唯一,因此尽量用.loc属性索引 """
# print(sr102_1["a":"f"])
""" series和df运算时都是元素级运算,会根据索引对齐,无法对齐部分,填充为NAN值,即无效值 not a number """
# sr102_3=sr(np.arange(5))
# sr102_4=sr(np.arange(3))
# print(sr102_3+sr102_4)
""" df只能构造二维数组 """
""" ndarray,列表作为df参数,不转置 """
# df102_8=df(np.arange(3).reshape(3,1),index=list("qwe"))
# p(df102_8)
# df102_9=df(np.arange(3).reshape(1,3),columns=list("asd"))
# p(df102_9)
# df102_5=df(np.arange(20).reshape(5,4),index=list("qwert"),columns=list("asdf"))
# p(df102_5)
# df102_10=df([[1,2,3],[4,5,6]],index=list("qw"),columns=list("asd"))
# p(df102_10)
# df102_12=df(sr102_3,sr102_4)
# p(df102_12)
""" 只有字典作为df函数参数才会转置为列 """
# df102_11=df({"a":range(3),"s":range(3),"d":range(3)})
# p(df102_11)
""" df添加列就是直接赋值新的df列索引,无法对齐的空值会被填充nan """
# df102_5["g"]=sr(range(3),index=list("qwe"))
# p(df102_5)
# del df102_5["g"]
# p(df102_5)
""" 双层嵌套字典构造df,外层字典的键作为列索引,内层字典是行索引 """
# df102_6=df({0:{1:"a",2:"s",3:"f"},4:{1:"q",2:"w",3:"e"}})
""" df也可以使用.T属性转置 """
# p(df102_6);p(df102_6.T)
""" pd的columns和index都是不可变的,一旦初始确定即不再改变,后续只能reindex,所以以下语句错误 """
# df102_5.columns[0]="z"
# df102_5.index[0]="x"
# df102_7=df(np.arange(3),index=list("aaa"))
# p(df102_7[0])
""" df的中括号[]普通索引只能索引列,不能索引行,索引行和添加行或者定点索引只能使用.loc属性,.loc是索引,
   所以参数用中括号[],.loc和.iloc截取是左闭右开区间,与python普通索引方法一致 """
# df102_5.loc["q"]=0
""" 添加行 """
# df102_5.loc["y","d"]=0
# df102_5.loc["e":"t","a":"s"]=np.nan
""" .iloc只能是序数索引,与索引标签无关(即使标签是2,序数是0,.iloc[0]索引到0行) """
""" 花式索引是数组索引,中括号[]是花式索引标识符,
所以不能使用冒号:划出头标尾标进行范围索引,范围索引只能是普通索引 """
# df102_5.loc[["e","r","t"],["a","s"]]=0
# p(df102_5)
""" pd也可以使用布尔型索引,pd可以作为pd函数的参数生成新pd """
# p(df(df102_5[df102_5["a"]<10]))
""" reindex可以重设行索引和列索引排序,以新索引新增df,且复制新旧索引能对齐的部分
   可以通过fill_value参数指定填充值 """
""" df和df的代数函数,都可以设置fill_value参数 """
# p(df102_5.reindex(index=list("ytrewq"),fill_value=233))
# p(df102_5.reindex(columns=list("aytrewq"),fill_value=233))
""" series和df运算时都会自动对齐,
   df.apply应用聚合函数,累积函数和一般函数时,代入函数的参数是df的series
   默认按列代入,默认参数为axis=0(axis="index")扩散,可以设置为按axis=1/axis="columns"传播
      df只能创建二维数组,而numpy无维数限制
      axis的理解类似物理学上的横波:波的行进方向和波的能量方向垂直,
      中选定的axis是迭代方向(外循环),而其他axis则成为一个整体,是运算方向(内循环)
      series与pd运算时,series与选定的axis平行 """
# pd和numpy采用了不同的axis思路
""" 聚合函数,.apply方法和与series的广播运算,.fillna中,axis表示运算方向(按axis作为一个整体执行运算),在.drop和.dropna中,axis表示查找方向 """
""" pd中sr永远输出为纵向,但是对齐只看下标,不看维度,;每次运算,axis=0列索引先取参数或构成外循环,行索引构成内循环,外循环输出为结果
   以pd.sum为例,外循环0列:0行1行sum输出为一个值;1列,2列依次外循环,最终输出结果为外循环每列的sum
   以pd.sub(sr)为例,外循环0列:0行1行与sr的0,1依次对齐运算,sr的2无法对齐输出nan,三个数值输出为一个sr,外循环成列
   以pd.apply为例,外循环0列:列作为sr代入函数求得max,输出为一个值,最终输出为各列的max
   以pd.drop([0])为例,外循环0列:内循环删除行索引为0的元素;依次循环1列,2列,得到最终删除(0,0),(0,1),(0,2)的结果
   由以上推断得出,axis指定外循环的方向,而内循环根据指定参数进行对齐运算 """
# df_max=lambda x :x.max()
# df102_13=df([[1,2,3],[2,4,6]])
# df102_14=df([[1,2],[3,4]])
# sr102_13=sr([7,8,9])
# p(df102_13)
# p(df102_13.sum(axis=0))
# p(df102_13.sum(axis=1))
# p(df102_13+df102_14)
# p(df102_13.sub(sr102_13,axis=0))
# p(df102_13.sub(sr102_13,axis=1))
# p(df102_13.apply(df_max,axis=0))
# p(df102_13.apply(df_max,axis=1))
# p(df102_13.drop([0],axis=0))
# p(df102_13.drop([0],axis=1))
""" df函数只能创建二维数组,np可以创建多维数组,所以以下第2个函数无效 """
# arr102_15=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# df102_15=df(arr102_15)
# p(df102_5)
# p(df102_5.apply(df_max,axis="index"))
# p(df102_5.apply(df_max,axis=1))
# p(df102_5.apply(df_max))
# p(df102_5.cumsum())
# p(df102_5.cumsum(axis=1))
""" 元素级函数使用.applymap方法,常用的numpy元素函数ufunc也可以用于df对象 """
# p(np.sqrt(df102_5))
# df_fmt=lambda x : "{:f}".format(x)
# p(df102_5.applymap(df_fmt))

""" df和series运算时,默认axis=1 """
# sr102_5=sr(np.arange(4),index=list("asfg"))
# sr102_5=sr(np.arange(4),index=list("qwey"))
# p(df102_5.sub(sr102_5))
# p(df102_5.sub(sr102_5,axis=0))
# p(df102_5.sub(sr102_5,axis=1))
# p(df102_5+sr102_5)
""" 按行index方向对齐索引"q",所以axis=0
   df的属性,默认inplace=False数值传递,复制运算,改为True之后,就地运算 """
# df102_5.drop("q",axis=0,inplace=False)
""" 由于索引本身是不可变数据类型,所以多个索引作为drop参数,必须是中括号[],小括号会被认为是一个元组作为索引 """
# df102_5.drop(["a","f"],axis=1,inplace=True)
# p(df102_5)
""" 排序和排名 """
# sr102_333=sr(range(4),index=list('qwer'))
""" 根据索引排序和根据值排序,默认升序排序,可以指定为降序 """
# p(sr102_333.sort_index())
# p(sr102_333.sort_values(ascending=False))
""" df排序可以指定排序轴或排序列 """
# df102_333=df(np.arange(8).reshape((2,4)),index=list('qw'),columns=list('asdf'))
""" 指定多个排序列时,按照指定顺序,先指定的列先排序,不打乱先列排序的前提下后排序的列内部再重新排序 """
# p(df102_333.sort_values(by=['w','q'],ascending=False,axis=1))
# p(df102_333.sort_values(by=['q'],ascending=False,axis=1))
# p(df102_333.sort_index(axis=1,ascending=False))
""" 排名是返回数值的排名数字,默认method='average',表示同级数值的排名表达方式 """
# sr102_334=sr([7, -5, 7, 4, 2, 0, 4])
""" 同级的排名取排名平均数 """
# p(sr102_334.rank())
""" 同级的排名先出现排前面 """
# p(sr102_334.rank(method='first'))
""" 同级的排名取最大排名数 """
# p(sr102_334.rank(method='max'))
""" 同级的排名取最小排名数 """
# p(sr102_334.rank(method='min'))
""" 类似min,但是忽略同排名对后续排名的影响(并列第1的后一名是第2名,而非第3名) """
# p(sr102_334.rank(method='dense'))

""" pandas读取文件 """
""" 读写CSV格式 """
""" d:/notes-python """
# import os
# import sys
# path = os.path.abspath(os.path.dirname(sys.argv[0]))
# p(path)
# df102_16=pd.read_csv("d:/notes-python/examples/ex1.csv")
r""" “/”：表示根目录，在windows系统下表示某个盘的根目录，如“E:\” 
   “./”：一个点表示当前目录；（表示当前目录时，也可以去掉“./”，直接写文件名或者下级目录）
   “../”：两个点表示上级目录。"""
""" 本例需要把pwd转移至本py文件所在文件夹才能使用相对路径
   先在终端中输入:d,切换盘符
   再cd notes-python转至目标文件夹 """
""" nrow参数设置读取行 """
# df102_16=pd.read_csv("examples/ex1.csv",nrows=2)
# p(df102_16)
# import csv
""" csv.reader是成行读取csv文件 """
""" zip(*values)是把values垂直解压 """
# with open("examples/ex7.csv") as f102_17:
   # csv102_17=csv.reader(f102_17)
   # lines=list(csv102_17)
   # header,values = lines[0],lines[1:]
   # p(header)
   # p(values)
   # data_dict={k:v for k,v in zip(header,values)}
   # data_dict={k:v for k,v in zip(header,zip(*values))}
   # p(repr(zip(*values)))
   # df102_17=df(data_dict)
   # p(df102_17)
""" 版本警告:read_table即将删除 """
""" 利用read_table读写文件 """
# df106_22=pd.read_table("d:/notes-python/examples/ex2.csv",sep=',',header=None,names=['a','b','c','d','message'],index_col='message')
# p(df106_22)
""" 读写Excel """
""" 先利用pd.ExcelFile创建Excel实例,再通过read_excel读取 """
# exc102_18=pd.ExcelFile('examples/ex1.xlsx')
""" 读取多个sheet时,sheet名称用中括号包围(不能用小括号) """
# df102_18=pd.read_excel(exc102_18,['example1','example2'])
# p(df102_18)
""" python简单读写MySQL """
# import mysql.connector
# myconn=mysql.connector.connect(host='localhost',user='root',password='1234',database='runoob')
# mycursor=myconn.cursor()
# rows=mycursor.execute('select * from tb1')
# for x in mycursor:
#    p(x)
# mycursor.close
# myconn.close
""" pandas读写MySQL """
# import pymysql
# import sqlalchemy
# from sqlalchemy import create_engine 
# info_conn_to_mysql='mysql+pymysql://{0}:{1}@{2}:{3}/{4}?charset=utf8'.format('root','1234','localhost','3306','runoob')
# engine_mysql=create_engine(info_conn_to_mysql)
# cmd_sql='select * from tb1'
# df10999=pd.read_sql(sql=cmd_sql,con=engine_mysql)
# p(df10999)
""" 使用df.to_sql可以把df写入MySQL中 """

""" 数据清洗与转换 """
""" 处理缺失值 """
""" df.isnull和df.notnull检测缺失值 """
""" 滤除缺失值dropna方法 """
# df102_19=df([[1., 6.5, np.nan], [1., np.nan, np.nan],[np.nan, np.nan, np.nan], [np.nan, 6.5, np.nan]],index=[0,1,3,2])
""" df.dropna默认how='any',默认删除任何有无效值的行,可以通过设置how='all'指定 """
# p(df102_19)
# p(df102_19.isnull())
# p(arr102_19)
# p(df102_19.dropna(how="all"))
# df102_19[3]=np.nan
""" 指定删除列 """
# p(df102_19)
# p(df102_19.dropna(axis=1,how="all"))
""" 填充缺失值fillna方法 
    fillna可以接受series参数 """
""" 可以设置inplace参数=True就地运算 """
# p(df102_19.fillna("a"))
""" fillna可以接受字典参数,对指定列填充不同值 """
# p(df102_19.fillna({0:"x",1:"y",2:"z"}))
# """ fillna接受series参数 """
# sr102_19=df102_19.sum(axis=1)
# p(sr102_19)
""" 现阶段fillna只能逐列填充,默认axis=0,不能调整 """
# p(df102_19.fillna(sr102_19))
""" method参数设置向前填充,limit参数设置填充个数 """
# p(df102_19.fillna(method="ffill",limit=1))
""" 数据转换 """
""" 移除重复数据duplicated属性,drop_duplicates方法 """
# df102_20=df({'k1': ['one', 'two'] * 3 + ['two'], 'k2': [1, 1, 2, 3, 3, 4, 4]})
# p(df102_20)
# p(df102_20.duplicated())
""" drop_duplicates,缺省是全列比对重复,可以设置比对列,keep参数默认保存第一个重复项或指定最后一个重复项 """
# p(df102_20.drop_duplicates())
# p(df102_20.drop_duplicates('k2',keep='last'))
""" 利用函数或映射转换数据series.map方法 """
# dic102_20={1:'q',2:'w',3:"e",4:'r'}
# df102_20["k3"]=df102_20['k2'].map(dic102_20)
""" map函数与lambda联用 """
# df102_20['k2']=df102_20['k2'].map(lambda x: dic102_20[x])
# p(df102_20)
""" 替换值replace方法,接受单一值,列表参数,字典参数 """
# p(df102_20.replace([1,2],'q'))
# p(df102_20.replace([1,2],list('qw')))
# p(df102_20.replace({1:'q',2:'w',3:'e'}))
""" df.rename方法重置指定索引,接受字典参数 """
# p(df102_20.rename(columns={'k1':8}))
""" 特定文本函数,待解 """
# p(df102_20.rename(columns=str.upper))
""" df数据的索引无法单个索引修改,只能整体替换 """
# df102_20.index=df102_20.index.map(lambda x : x**3)
# p(df102_20)
""" 离散化和面元划分 """
""" pd.cut和pd.qcut函数,默认左开右闭,可以设置right=false改为左闭右开 """
# lis102_21 = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
# bin102_21=[0,25,30,35,50,100]
""" pd.cut返回值是一个categorical对象,可以视作由分类标签labels构成的字符串 """
# ct102_21_1=pd.cut(lis102_21,bin102_21,labels=list('qwert'))
# p(ct102_21_1)
# p(ct102_21_1.codes)
""" pd.value_counts函数返回各个取值的数据数量 """
# p(pd.value_counts(ct102_21_1))
""" 如果输入的是分割段数,则会按最值均分所有数据,precision=2小数点后保留两位,right=false左闭右开 """
# ct102_21_2=pd.cut(lis102_21,4,precision=2,right=False)
# p(ct102_21_2)
""" pd.qcut按最大最小值进行分位数分割,保证每段元素个数相同 """
# qct102_21_1=pd.qcut(lis102_21,3,precision=1)
# p(qct102_21_1)
""" 分段参数设为0-1的小数,即可控制分位点 """
""" 分段参数可以设置成整数,则按此比例均分 """
# qct102_21_2=pd.qcut(lis102_21,[0,0.3,0.7,0.9,1],precision=1)
# p(qct102_21_2)
""" 检测和转换异常值.any方法 """
# df102_22=df(np.random.randn(1000,4))
# p(df102_22.describe())
# df102_22_1=df102_22[(np.abs(df102_22)>3).any(1)]
# p(df102_22_1)
""" np.sign函数把负数转为-1,正数转为1,0转为0,nan转为nan,可以用此函数转换超出正常值的数值 """
# p(np.sign(df102_22))
""" 随机抽样np.random.permuting函数和df.take方法;随机采样.sample方法(不重复replace=False) """
# df102_23=df(np.arange(5*4).reshape(5,4))
# slt102_23_1=np.random.permutation(3)
# p(df102_23)
# p(df102_23.take(slt102_23_1,axis=1))
# p(df102_23.loc[:,slt102_23_1])
# p(df102_23.reindex(columns=slt102_23_1))
""" df.sample和series.sample方法抽样,默认不重复抽取相同样;超出总体数量本,可以开启重复抽样 """
# p(df102_23.sample(n=2))
# p(df102_23.sample(n=7,replace=True))
""" 哑变量pd.get_dummies函数,把定性的一维数据转化为布尔型矩阵的方便计数 """
# df102_24=df({'k':['q','w','e','q','w','q'],'v':[1,2,3,1,2,3]})
""" prefix参数用于给哑变量添加前缀 """
# dummies=pd.get_dummies(df102_24['v'],prefix='value')
""" 此处双中括号不用单括号原因待解,可能与索引类型有关,普通索引截取的是series,花式索引截取的是df,只有df才能使用join方法 """
# df_join_dummies=df102_24[['k']].join(dummies)
# p(df102_24)
# p(df_join_dummies)
""" 哑变量常与pd.cut和pd.qcut等离散化函数联用,完成统计 """
# np.random.seed(10225)
# arr102_25=np.random.rand(10)
# bin102_25=[0,0.2,0.4,0.6,0.8,1]
# df_ct_dum=pd.get_dummies(pd.cut(arr102_25,bins=bin102_25,labels=list('qwert')))
# p(df_ct_dum)
""" 字符串操作split,strip,字符串.join,find,index,字符串.replace """
# str102_26='q,we,  git  '
# lis102_26_1=str102_26.split(',')
# p(lis102_26_1)
# lis102_26_2=[s.strip() for s in lis102_26_1]
# p(lis102_26_2)
# str102_26_1=":".join(lis102_26_2)
# p(str102_26_1)
""" 判断字符存在常用函数,其中字符串.index查找不存在的字符时,会返回error,而字符串.find会返回-1 """
# p("git" in lis102_26_2)
# p(str102_26_1.index('git'))
# p(str102_26_1.find(','))
""" 替换字符 """
# p(str102_26.replace(',','::'))
""" 正则表达式 """
""" re模块可以指定compile生成regexp对象用于大批量字符串处理,本笔记只举一例 """
# import re
# text102_27 = "foo    bar\t baz  \tqux"
# text102_27_1=re.split('\s+',text102_27)
# p(text102_27_1)
r""" 以下语句与上述语句结果相同,其中'\s+'表示一个或多个空白符(空白符包括空格,换行符,制表符等)
   regexp.findall方法返回所有匹配正则表达式的字符串,与此类似的search方法只返回第一个,而match方法只匹配字符串首部 """
# regexp102_27=re.compile('\s+')
# text102_27_2=regexp102_27.split(text102_27)
# text102_27_3=regexp102_27.findall(text102_27)
# text102_27_4=regexp102_27.sub('///',text102_27)
# p(text102_27_2)2
# p(text102_27_3)
# p(text102_27_4)
""" 矢量化字符串函数,即判断以series为整体进行文本运算 """
""" 由于.map和.applymap方法应用于nan值时会报错,因此有一系列针对series跳过nan的方法,通过series.str属性访问 """
# sr102_28 =sr({'Dave': 'dave@google.com', 'Steve': 'steve@gmail.com','Rob': 'rob@gmail.com', 'Wes': np.nan})
""" .str.contains查找字符 """
# p(sr102_28.str.contains('google'))
""" .str.get或.str[]索引指定字符 """
# p(sr102_28.str.get(3))
# p(sr102_28.str[3])

""" 数据规整:聚合,合并与重塑 """
""" 层次化索引 """
""" 以series开始为例 """
# sr108_1=sr(np.random.randn(9),index=[list("qqqwweerr"),[1,2,3,1,3,1,2,2,3]])
# p(sr108_1)
# p(sr108_1.index)
""" 层次化索引更简单,常规索引需要排序后才能切片,且索引排序需要指定level """
# sr108_1_1=sr108_1.sort_index(level=0)
""" 层次化索引的不同层级用小括号()作为一个整体代入中括号索引 """
# p(sr108_1_1[('e',2):'r'])
# p(sr108_1.loc[:,2])
# p(sr108_1.loc[['q','w']])
""" unstack把一维series逆透视为二维df,二级索引作为行标题 """
# df108_1=sr108_1.unstack()
# p(df108_1)
# sr108_1_2=df108_1.stack()
# p(sr108_1_2)
""" df的index和columns都可以建立分层索引 """
""" df的排序需要指定axis和level """
# df108_2=df(np.arange(12).reshape(4,3),index=[list("qqww"),[1,2,1,2]],columns=[list('aas'),[0,1,0]])
# p(df108_2)
# p(df108_2.index)
# p(df108_2.columns)
# p(df108_2.loc['q':"w",'a':"s"])
# p(df108_2.swaplevel())
""" multiindex函数创建多级索引反复使用 """
# mi108_2=pd.MultiIndex.from_arrays([list("qqww"),[1,2,1,2]])
# df108_2_1=df(np.arange(12).reshape(4,3),index=mi108_2)
# p(df108_2_1)
""" 重排与分级排序 """
""" 排序详见上文 """
""" 根据级别汇总聚合 """
# p(df108_2.sum(level=0))
# p(df108_2.sum(level=1))
""" 把列转换为索引 """
# df108_3 = df({'a': range(7), 'b': range(7, 0, -1),'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two'], 'd': [0, 1, 2, 0, 1, 2, 3]})
""" df.set_index方法可以把df内的列转为索引,可以设置drop=false,使得成为索引的列不删除 """
# df108_3_1 = df108_3.set_index(['c','d'])
# df108_3_2 = df108_3.set_index(['c','d'],drop=False)
# df108_3_3 = df108_3_1.reset_index()
# p(df108_3)
# p(df108_3_1)
# p(df108_3_2)
# p(df108_3_3)
""" 合并数据集 """
""" 数据库风格的df合并pd.merge """
""" pd.merge类似数据库的join ... on查询,需要指定连接字段;
   默认是inner join,可以通过how参数指定left,right,outer """
""" 多个外键,用列表代入;左右外键名称不同,则分别指定left_on,right_on;如果没有指定外键on,默认指定同名列为外键(推荐指定外键) """
""" 进行pd.merge时,两df原有的索引会被删除 """
# df108_4 = df({'k1':list('qqw'),'k2':list('asa'),'lv':[1,2,3]})
# df108_5 = df({'k1':list('qqww'),'k3':list('aaas'),'rv':[4,5,6,7]})
# df108_6 = pd.merge(df108_4,df108_5,left_on=['k1','k2'],right_on=['k1','k3'],how='outer')
# p(df108_6)

""" 索引上的合并pd.merge和df.join """
""" pd.merge可以指定按索引对齐合并或者索引与列混合对齐(right_index和left_on混用) """
# df108_7=pd.merge(df108_4,df108_5,left_index=True,right_index=True,how='inner')
# p(df108_7)
# df108_8=df108_4.set_index(['k1','k2'])
# df108_9=df108_5.set_index(['k1','k3'])
# df108_10=pd.merge(df108_8,df108_5,right_on=['k1','k3'],left_index=True,how='inner')
# df108_11=pd.merge(df108_8,df108_9,right_index=True,left_index=True)
# p(df108_8)
# p(df108_5)
# p(df108_10)
# p(df108_9)
# p(df108_11)
""" 使用df.join方法实现索引合并,可以同时合并多个df """
# df108_12=df(np.arange(12).reshape((4,3)),index=list('qwer'))
# df108_13=df(np.arange(12).reshape((3,4)),index=list('qwt'))
""" 重名的列需要添加suffix参数重命名 """
# df108_14=df108_12.join(df108_13,how='outer',lsuffix='_left',rsuffix='_right')
# p(df108_14)
""" 轴向连接np.concatenate和pd.concat """
# arr108_15=np.arange(12).reshape(4,3)
# p(np.concatenate([arr108_15,arr108_15]))
# p(np.concatenate([arr108_15,arr108_15],axis=1))
# sr108_16_1=sr([0,1],index=list('qw'))
# sr108_16_2=sr([2,3,4],index=list('qrt'))
# sr108_16_3=sr([5,6],index=list('er'))
""" axis=1表示合并轴,由于sr是纵向轴,所以一维sr在横向合并时,通过对齐成为二维pd;此处join_axes参数必须使用双中括号[[]] """
""" sr的二维合并时,keys参数自动成为列索引 """
# p(pd.concat([sr108_16_1,sr108_16_2,sr108_16_3],axis=1,join_axes=[list('qwrt')],join='inner',keys=['k1','k2','k3']))
""" axis=0,可以设置keys参数,添加层次化索引 """
# p(pd.concat([sr108_16_1,sr108_16_2,sr108_16_3],keys=['k1','k2','k3']))
""" pd的合并可以设置ignore_index参数丢弃合并轴方向的索引 """
# df108_17_1=df(np.arange(12).reshape((4,3)),index=list('qwer'),columns=list('asd'))
# p(pd.concat([df108_17_1,df108_17_1],axis=0,ignore_index=False,keys=['lev1','lev2']))
# p(pd.concat([df108_17_1,df108_17_1],axis=1,ignore_index=True))
""" 合并重叠数据sr.combine_first和df.combine_first """
""" .combine_first方法用于合并存在相同值的两个sr或pd,参数有义值填充nan;重叠元素,对象覆盖参数 """
# df108_18_1 = df({'a': [1., np.nan, 5., np.nan],'b': [np.nan, 2., np.nan, 6.],'c': range(2, 18, 4)})
# df108_18_2 = df({'a': [5., 4., np.nan, 3., 7.],'b': [np.nan, 3., 4., 6., 8.]})
# p(df108_18_1)
# p(df108_18_2)
# p(df108_18_1.combine_first(df108_18_2))
""" 重塑和轴向旋转 """
""" df.stack和df.unstack是根据索引进行维度变换 """
""" 重塑层次化索引 df.stack和df.unstack"""
""" .stack用于把pd二维表降维成一维表sr,所有的列都会变成索引 """
# df108_19=df(np.arange(6).reshape((2,3)),index=pd.Index(list('qw'),name='row_index'),columns=pd.Index(list('asd'),name='col_index'))
# sr108_19=df108_19.stack()
# p(df108_19)
# p(sr108_19)
""" .unstack就是对pd和sr根据行索引index进行升维,指定的行索引会成为最低级的列索引 """
# df108_20=df({'z':sr108_19,'x':sr108_19+5},columns=pd.Index(list('zx'),name='k'))
# p(df108_20)
# p(df108_20.unstack('row_index'))
# p(df108_20.unstack(1))
""" df.pivot和pd.melt是根据列进行维度变换 """
""" 长格式转为宽格式(一维表透视为二维表)df.pivot """
""" 宽格式转为长格式(二维表逆透视为一维表)pd.melt """
# df108_25=df({'z':[0,1,2],'x':[3,4,5],'c':[6,7,8],'k':list('qwe')})
""" pd.melt中id_vars指定转为次级行索引的列(可以通过reset_index方法转为列),value_vars指定数值列,variable是自动生成的索引辅助列,value是自动生成的一维值列 """
# df108_25_m=pd.melt(df108_25,id_vars=['x'],value_vars=['z','k'])
""" df.pivot中index指定转为行索引的列(可以通过reset_index方法转为列),columns指定转为列索引的列,values指定数值列 """
# df108_25_m_p=df108_25_m.pivot(index='variable',columns='x',values=['value']).reset_index(0)
# p(df108_25)
# p(df108_25_m)
# p(df108_25_m_p)

""" 数据聚合与分组运算 """
""" groupby机制 """
""" df.groupby生成的是可迭代的group对象是由索引和值构成的二元成对迭代器,需要用函数(常用list)才能实例化,实例化后可以以此生成字典 """
""" df.groupby指定的分组依据会成为新df的索引 """
# df110_1=df({'k1':list('qqwwq'),'k2':list('asasa'),'v1':np.arange(5),'v2':np.arange(5)+5})
# p(df110_1.sort_values(by='k1'))
""" 也可以指定df外能与df索引对齐的series成为分组依据,在df的切片进行分组group时,如果by参数接受df的列作为参数,则必须是df[],不能省略df """
# sr110_1=sr(list('zzxxxx'))
# gp110_1=df110_1[['v1','v2']].groupby([df110_1['k1'],sr110_1])
""" 多元分组构成的字典:键是元组格式,值是df格式 """
""" 选取一列或列的子集 """
# p(dict(list(gp110_1))[('q','z')])
# p(gp110_1.size())
# gp110_2=df110_1[['v1','v2']].groupby([df110_1['k1'],df110_1['k2']])
# for [i,v] in gp110_2:
   # p(i)
   # p(v)
""" get_group()用于读取指定索引的gp对象内的元素 """
# p(gp110_2.get_group(('q','a')))
# p(gp110_2['v1'].mean())
""" 对分组进行迭代 """
""" 分组依据的值以多元元组格式构成索引,如下例中的(q,w) """
# for (q,w),e in gp110_2:
#    p(q,w)
#    p(e)
""" 分组默认是axis=0,如有需要可以改为axis=1 """
# sr110_3=df110_1.dtypes
# p(sr110_3)
# gp110_3=df110_1.groupby(by=sr110_3,axis=1)
# for a,s in gp110_3:
#    p(a)
#    p(s)
""" 通过字典或series分组 """
""" groupby接受能与索引对齐的字典或sr作为by参数,多余映射会被忽略 """
# dic110_4={'k1':'k','k2':'k','k3':'k','v1':'v','v2':'v','v3':'v'}
# gp110_4=df110_1.groupby(by=dic110_4,axis=1)
# for a,s in gp110_4:
#    p(a)
#    p(s)
# sr110_5=sr(dic110_4)
# gp110_5=df110_1.groupby(by=sr110_5,axis=1)
# p(sr110_5)
# for a,s in gp110_5:
#    p(a)
#    p(s)
""" 通过索引分组 """
""" 通过索引的进行函数运算分组 """
""" by参数输入的函数会把索引作为参数自动代入函数进行计算,并以返回值进行分类,函数不能加括号,类似apply """
# df110_6 = df(np.arange(25).reshape((5, 5)), columns=['a', 'b', 'c', 'd', 'e'],index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis'])
# lis110_6 = list('qqqww')
""" groupby的by参数接受函数分组,字典分组,列表索引,series分组,pd.cut和pd.qcut生成的categorical对象混用 """
# gp110_6 = df110_6.groupby(by=[len,lis110_6])
# p(df110_6)
# p(gp110_6.count())
""" 根据索引级别分组 """
""" 层次化索引可以通过指定level和axis进行分组 """
# col_index110_7=pd.MultiIndex.from_arrays([list('qqqww'),list('asdas')],names=['c1','c2'])
# df110_7=df(np.arange(20).reshape((4,5)),columns=col_index110_7)
# gp110_7_0=df110_7.groupby(level='c1',axis=1)
# gp110_7_1=df110_7.groupby(level=1,axis=1)
# p(df110_7)
# p(gp110_7_0.count())
# p(gp110_7_1.count())
""" 数据聚合 """
""" group对象可以直接应用聚合函数或通过group.agg或group.aggregate方法自定义聚合运算 """
# df110_8=df({'k1':list('qqwwq'),'k2':list('asasa'),'v1':np.arange(5),'v2':np.arange(5)+5})
# p(df110_8)
# gp110_8=df110_8.groupby(by=[df110_8['k1'],df110_8['k2']])
""" quantile是series方法,但是因为group对象的元素是series,所以也适用 """
# p(gp110_8.quantile(0.8))
# def gp_max(x):
   # return x.max()
# p(gp110_8.aggregate(gp_max))
# p(gp110_8.describe())
""" 面向列的多函数应用 """
# df110_9=pd.read_csv('D:/notes-python/examples/tips.csv')
# df110_9['tips_percent']=df110_9['tip']/df110_9['total_bill']
# gp110_9=df110_9.groupby(by=['day','smoker'])
# gp110_9_1=df110_9.groupby(by=['day','smoker'],as_index=False)
""" df.head属性显示df靠前的项 """
# p(df110_9.head(10))
""" 可以通过字典指定group对象运算,中括号[]标识符和二元成对元组对聚合函数运算结果重命名 """
# p(gp110_9['tips_percent','total_bill'].agg({'tips_percent':[('平均值','mean'),('标准差','std')],'total_bill':[('最大值',gp_max)]}))
""" 以下字典参数方法会被版本更新删除,因此不推荐 """
# p(gp110_9['tips_percent'].agg({'平均值':'mean','标准差':'std'}))
""" 以没有行索引的形式返回聚合数据 """
""" groupby不应用聚合函数时,默认会把分组依据设置为索引,设置as_index参数关闭 """
# p(gp110_9.mean())
# p(gp110_9_1.mean())
""" apply:一般性的拆分,应用,合并 """
""" 左闭右开索引,待解? """
# def gp_top(frm,n=5,column='tips_percent'):
   # return frm.sort_values(by=column,ascending=False)[:n]
# p(gp_top(df110_9,n=6))
""" apply应用函数时,被应用函数参数与函数名应当并列赋值 """
""" groupby.apply应用聚合函数时,默认把分组依据和原始索引合并为层次化索引,设置group_keys参数可以关闭 """
# p(df110_9.groupby(by=['smoker','day'],group_keys=False).apply(gp_top,n=1,column='total_bill'))
""" 分位数和桶分析 """
""" groupby中by参数可以接受pd.cut和pd.qcut生成的对象 """
# df110_11=df({'v1':np.random.rand(20),'v2':np.random.rand(20)})
# ctg110_11_c=pd.cut(df110_11['v1'],5)
# ctg110_11_q=pd.qcut(df110_11['v1'],5)
# p(df110_11)
""" agg方法接受中括号[]和二元元组对函数输出列重命名 """
# p(df110_11.groupby(ctg110_11_c).agg([('平均值','mean')]))
# p(df110_11.groupby(ctg110_11_q).agg(['mean']))
""" 示例:用特定于分组的值填充缺失值 """
""" 示例:随机采样和排列 """
""" 示例:分组加权相关系数 """
""" 示例:组级别的线性回归 """
""" 透视表和交叉表 """
""" 透视表df.pivot_table是用于对数据进行分组和聚合的方法,且不同于groupby方法,df.pivot_table可以把分组依据转置为列索引 """
""" 透视表的aggfunc默认为'mean',可以指定为自定义函数或任意对series成立的聚合函数,margins参数用于开关进行分组汇总小计,fill_value参数用于设置填充值 """
""" 透视表不支持对aggfunc输出值重命名,待解 """
# p(df110_9.pivot_table(index=['time','day'],columns=['smoker'],values=['tips_percent','size'],margins=True,fill_value='NX',aggfunc={'size':len,'tips_percent':'std'}))
""" 生成交叉表:pd.crosstab """
""" 交叉表是专用于计算分组频率的特殊透视表 """
# p(pd.crosstab(index=[df110_9['time'],df110_9['day']],columns=df110_9['smoker'],margins=True))

""" 时间序列 """
""" 日期和时间数据类型及工具 """
from datetime import datetime as dt,timedelta as td
""" datetime数据格式以毫秒储存时间,以timedelta格式表示两个datetime数据的时间差 """
# p(dt.now())
# p(dt.now().year)
""" .tzinfo用于储存时区信息 """
# p(dt.now().tzinfo)
""" dt数据可以被dt.strftime方法格式化为字符串,全部dt时间格式参见Excel表格 """
# p(dt.now().strftime('%F'))
""" 字符串和datetime相互转换 """
""" dt.strptime函数可以把字符串转为dt数据 """
# p(dt.strptime('2019-7-8','%Y-%m-%d'))
from dateutil.parser import parse as ps 
""" parse是比dt.strptime函数更简易的日期字符串解析包,但parse包更容易出错;设置dayfirst参数,可以声明字符串是'日月年'日期格式 """
# p(ps('8-7-2019',dayfirst=True))
""" 数据戳的null值是nat not a number """
""" pandas处理时间字符串series常用pd.to_datetime函数 """
# p(pd.to_datetime(['2019-7-8 21:10:36',None]))
""" 时间序列基础 """
""" pandas基本时间序列是以时间戳为索引的series,pandas时间戳通常由字符串或datetime对象生成
   pandas用numpy的datetime64数据类型以纳秒形式存储时间戳
   pandas的时间序列索引是专用的DatetimeIndex,DatetimeIndex的值是Timestamp对象 """
""" 索引,选取和子集构造 """
""" DatetimeIndex索引方式接受dt时间,Timestamp型时间,字符串型时间 """
""" 常用dt函数构造dt时间 """
# p(dt(2019,7,10))
""" 也经常使用pd.DatetimeIndex函数构造时间序列索引 """
# di111_1=pd.DatetimeIndex(['2019/7/1','2019/7/2','2019/7/2','2019/7/1','2019/7/3'])
# df111_1=df(np.arange(20).reshape((5,4)),index=di111_1)
# p(df111_1['2019/7/1'])
# p(df111_1.groupby(level=0).count())
""" 时间序列的索引也是就地运算 """
""" 带有重复索引的时间序列 """
""" 相同时间段的时间序列索引时构成切片 """
""" 日期的范围,频率和移动 """
""" 生成日期范围 """
""" pd.date_range生成指定长度的DatetimeIndex,periods参数设定freq的循环次数,freq参数设定频率 """
""" pd.date_range默认保留时分秒,可以通过normalize参数关闭 """
# p(pd.date_range(start='2018/1/1 15:24:17',end='2019/7/10',freq='BQS-AUG',normalize=True))
""" 频率和日期偏移量 """
from pandas.tseries.offsets import Hour,Minute,Day,MonthEnd
""" 时间序列的基础频率是类似以上引入的Hour和Minute,但日常使用时只需要设立整数倍的基础频率即可 """
# p(pd.date_range(start='2019/7/10 15:43:13',periods=3,freq='1h30t'))
""" wom日期 """
""" 对于非固定时间间隔而是指定日期的pandas基础频率,称为锚定偏移(anchored offset),如wom-1mon,表示每个月第一个周一 """
# p(pd.date_range(start='2019/7/10 15:43:13',periods=3,freq='WOM-1fri'))
""" 移动(超前和滞后)数据 """
""" sr.shift和pd.shift在没有freq参数时,默认时间索引不变,只移动数值;而设置freq参数后,数值不动,而移动时间索引 """
# sr111_2=sr(np.arange(4),index=pd.date_range(start='2019/7/10',periods=4,freq='m'))
# p(sr111_2)
# p(sr111_2.shift(2))
# p(sr111_2.shift(2,freq='90t'))
""" 通过偏移量对日期进行位移 """
""" dt时间也可以通过直接计算偏移量而移动 """
""" 由2019/7/10加22天得到8月1号,由8月1号的第二个月末得出930 """
# p(dt(2019,7,10)+22*Day()+MonthEnd(2))
""" 对于锚定时点,有.rollforward和.rollback方法,移动时间 """
# p(MonthEnd().rollback('20190711'))
# p(MonthEnd().rollforward('20190711'))
""" 利用锚定时点的rollforward可以实现类似resample的时间序列索引的分组,但是此方法仅供参考,不推荐学习 """
# sr111_3=sr(np.arange(10),index=pd.date_range(start='20190711',periods=10,freq='7d'))
# p(sr111_3)
# p(sr111_3.groupby(MonthEnd().rollforward).mean())
""" 时区处理 """
""" 时区本地化和转换 """
""" 操作时区意识型timestamp对象 """
""" 不同时区之间的运算 """
""" 时期及其算术运算 """
""" 时期period表示的是时间段,用pd.period函数构造,由指定时间点(时间点也可以只精确到月份或年) """
# pr111_3=pd.Period('2019/7/10',freq='a-jun')
# pr111_4=pd.Period('2019/3/22',freq='a-jun')
""" 时期可以用整数进行加减运算 """
# p(pr111_3+1)
""" 相同freq的时期可以用减法计算时间差,不能用加法 """
# p(pr111_3-pr111_4)
""" pd.period_range用于生成一组时期索引PeriodIndex """
# p(pd.period_range('2019/7/10',periods=4,freq='m'))
""" 如果有有字符串数组,可以使用pd.periodindex函数生成periodindex对象 """
# p(pd.PeriodIndex(['2019Q1','2019Q2','2019Q3'],freq='q-dec'))
""" 时期的频率转换 """
""" period对象,带periodindex索引的series对象和df对象都可以通过.asfreq方法转为其他频率,how指代转化时间戳 """
# pr111_5=pd.Period('2019-jul',freq='a-jun')
# pr111_6=pr111_5.asfreq(freq='m',how='start')
# p(repr(pr111_5))
# p(repr(pr111_6))
""" 按季度计算的时期频率 """
# pri111_7=pd.period_range(start='2018q1',end='2019q2',freq='q-dec')
# df111_7=df(np.arange(len(pri111_7)*2).reshape((len(pri111_7),2)),index=pri111_7)
# p(df111_7)
""" period对象的频率转换,m对应月(不是锚定偏移),d对应每月最后一个日历日,bm对应月(不是锚定偏移),b对应最后一个工作日 """
# p(df111_7.asfreq(freq='b',how='e'))
""" timestamp和period相互转换 """
""" 含有period和timestamp作为索引的sr和pd,可以使用.to_timestamp和.to_period方法进行相互转换,其中时间戳转为时期,时期会重复 """
# tsi111_8=pd.date_range('2019/6/29',periods=6,freq='d')
# sr111_8=sr(np.random.randn(6),index=tsi111_8)
""" 设置freq参数,可以指定period """
# sr111_8_1=sr111_8.to_period()
# sr111_8_2=sr111_8_1.to_timestamp(how='e')
# p(sr111_8)
# p(sr111_8_1)
# p(sr111_8_2)
""" 通过数组创建periodindex """
""" 对于时期存在于df对象内部的df,可以通过pd.periodindex函数设置对应的时间参数生成periodindex索引 """
# df111_9=pd.read_csv("D:/notes-python/examples/macrodata.csv")
# p(df111_9.head(10))
# pri111_9=pd.PeriodIndex(year=df111_9['year'],quarter=df111_9['quarter'],freq='q-dec')
# df111_9.index=pri111_9
# p(df111_9['infl'].head(10))
""" 重采样及频率转换 """
""" 重采样是用df.resample方法类似根据时间索引进行分组group,生成的是resample对象 """
""" 降采样 """
""" 把高频数据转为低频数据,称为降采样;反之称为升采样 """
# tsi111_10=pd.date_range('2019/7/10 20:33:05',periods=50,freq='t')
# sr111_10=sr(np.arange(len(tsi111_10)),index=tsi111_10)
# p(sr111_10.head(10))
""" rule参数表示重采样的时间间隔;level参数表示重采样的索引级别;axis参数表示重采样轴,默认axis=0;
   fill_method表示升采样时的插值方式,默认不插值;closed默认区间左开右闭;loffset(如'+1s')表示时间校正(类似.shift方法)
   limit表示升采样填充时允许的最大时期数;kind表示聚合的时间索引类型('timestamp'或者是'period'),默认与原时间序列相同(timestamp是锚定整点聚合,而非固定时间间隔)
   label参数表示降采样时,显示整数面元的边界'left'或者'right',默认left;convention参数表示时期索引升采样父时期转换为子时期的转换方法,默认是'start',即由父时期的起始子时期继承父时期的值 """
# p(sr111_10.resample(level=0,rule='10t',label='right',kind='period').sum())
# p(sr111_10.resample(level=0,rule='10t',label='right',kind='timestamp').sum())
""" ohlc重采样 """
""" ohlc指的是股票常用的开盘价open,最高价high,最低价low,收盘价close,用于求取一维series的特定二维df """
# p(sr111_10.resample(rule='10min',kind='period').ohlc())
""" 升采样和插值 """
""" resample.asfreq方法可以实例化resample对象 """
# df111_11=df(np.arange(2*4).reshape((2,4)),index=pd.date_range('2019/7/10',periods=2,freq='w-wed'))
# p(df111_11)
# p(df111_11.resample('d',fill_method='ffill').asfreq('d'))
# p(df111_11.resample('d').bfill(limit=3))
""" 重采样索引不必完全与旧索引重叠,但是不对齐的部分需要填充 """
# p(df111_11.resample('w-thu').asfreq())
# p(df111_11.resample('w-thu').ffill())
""" 通过时期重采样 """
""" 时期的重采样要求频率必须有包含关系或平行关系,如Q-MAR只能升采样为A-MAR,A-JUN,A-SEP,A-DEC """
# pri111_12=pd.period_range('2019-7',periods=10,freq='m')
# df111_12=df(np.arange(10*4).reshape((10,4)),index=pri111_12)
# p(df111_12)
# p(df111_12.resample('a-dec').sum())
# p(df111_12.resample('a-dec').sum().resample('q-dec',convention='start').ffill())
# p(df111_12.resample('a-dec').sum().resample('q-dec',convention='end').ffill())
""" 移动窗口函数 """
# df111_13=pd.read_csv('d:/notes-python/examples/stock_px_2.csv',parse_dates=True,index_col=0)
# slt111_13=df111_13[['AAPL','MSFT','XOM']]
# slt111_13_rsp=slt111_13.resample('b').ffill()
# slt111_13_rsp['AAPL'].plot()
""" df.rolling方法根据索引,截取等长的移动窗口的数据并计算 """
""" df.rolling方法默认需要窗口所有值为非null值,即最少需要与window参数等量的有效数据才会聚合;修改min_periods参数,则可以接受低于window个数的数据进行计算,在有offset参数时,默认min_period=1 """
# mean_appl=slt111_13_rsp['AAPL'].rolling(window='50d',min_periods=1).mean()
# mean_appl.plot()
""" df.expanding方法与rolling方法类似,只不过是从最小时期开始,窗口长度不断扩大,属于累计窗口,而非等长窗口 """
# mean_appl.expanding(min_periods=200).mean().plot()
""" window参数接受整数和时长文本如上例的'50d' """
#slt111_13_rsp.rolling(60).mean().plot(logy=True)
""" 指数加权函数 """
""" 指数加权函数df.ewm方法用于对时间值附加权重,使得不同时间的数据重要性不等
   df.ewm方法中,span参数指的是根据时间跨度衰减权重;com参数指的是根据质心衰减,halflife指的是根据半衰期衰减 """
# ma60=slt111_13_rsp.loc['2006':'2007','AAPL'].rolling(30,min_periods=20).mean()
# ewma60=slt111_13_rsp.loc['2006':'2007','AAPL'].ewm(span=30).mean()
# ma60.plot(style='k--',label='simple ma')
# ewma60.plot(style='k-',label='ewma')
# plt.legend()
""" 二元移动窗口函数 """
""" 例如相关系数,协方差等统计运算需要在两个时间序列执行 """
# spx_rets=df111_13['SPX'].pct_change()
# slt111_13_rsp_pct_change=slt111_13_rsp.pct_change()
# slt111_13_rsp_pct_change_corr=slt111_13_rsp_pct_change.rolling(125,min_periods=100).corr(spx_rets)
# slt111_13_rsp_pct_change_corr.plot()
""" 用户定义的移动窗口函数 """
""" rolling.apply方法可以使窗口值应用自定义函数 """
# from scipy.stats import percentileofscore
# s_at_2pct=lambda x:percentileofscore(x,0.02)
# slt111_13_rsp_pct_change_apply=slt111_13_rsp_pct_change['AAPL'].rolling(250).apply(s_at_2pct)
# slt111_13_rsp_pct_change_apply.plot()
""" plt.legend用于给图像添加图例 """
# plt.legend()
""" 绘图和可视化 """
""" pandas自带的绘图方法如df.plot和seaborn包都是基于matplotlib包设计的 """
""" matplotlib入门 """
""" matplotlib的图像都具体在figure对象的subplot中生成 """
""" figure和subplot """
# fig109_1=plt.figure()
# """ figure的subplot从1开始索引计数 """
# ax109_1=fig109_1.add_subplot(2,2,1)
# ax109_2=fig109_1.add_subplot(2,2,2)
# ax109_3=fig109_1.add_subplot(2,2,3)
# ax109_1.hist(np.random.randn(100),bins=20,color='k',alpha=0.3)
# ax109_2.scatter(np.arange(30),np.arange(30)+3*np.random.randn(30))
# ax109_3.plot(np.random.randn(50).cumsum(),'k--')
""" 利用plt.subplots函数同步赋值,生成一个figure对象和一个由其中subplot对象组成的ndarray数组,数组索引从0开始计数 """
""" 调整subplot间距 """
# fig109_2,axes109_2=plt.subplots(2,3,sharex=True,sharey=True)
# p(fig109_2,axes109_2)
""" subplots_adjust既是figure的方法,也是一个独立函数 """
# for i in range(2):
   # for j in range(3):
      # axes109_2[i,j].hist(np.random.randn(500),bins=50,color='k',alpha=0.5)
""" wspace和hspace用于控制subplot之间空白占整个figure的百分比 """
# fig109_2.subplots_adjust(wspace=0, hspace=0)
# plt.subplots_adjust(left=None,bottom=None, right=None, top=None,wspace=0.05, hspace=0.05)
""" 颜色,标记和线型 """
""" 刻度,标签和图例 """
""" 生成单幅图表,可以直接使用plt.plot函数,图表颜色,标记和线型的参数分别如下,其中颜色参数接受常用颜色首字母和指定颜色码 """
""" 线形图中非实际数据默认是线性插值,marker参数用于标记真实值,drawstyle参数修改插值方式 """
# arr109_3=np.random.randn(30).cumsum()
# plt.plot(arr109_3,linestyle='dashed',marker='.',color='k',label='default')
# plt.plot(arr109_3,linestyle='--',marker='o',color='#DEABCF',drawstyle='steps-post',label='steps-post')
""" plt.legend放置图例时,绝大多数情况下可以直接使用loc='best' """
# plt.legend(loc='best')
""" 设置标题,轴标签,刻度以及刻度标签 """
# arr109_4=np.random.randn(1000).cumsum()
# fig109_4,ax109_4=plt.subplots()
# ax109_4.plot(arr109_4)
# """ set_xticks设置标签所在位置 """
# ax109_4.set_xticks([0,200,300,500,800,1000])
# """ set_xticklabels设置标签名称 """
# ax109_4.set_xticklabels(['base','first','second','third','fourth','final'],rotation=30,fontsize='medium')
# prpty109_4={
#            'title':"我的第一个图表标题 ",
#            'xlabel':'steps'
# }
# ax109_4.set(**prpty109_4)
""" 添加图例 """
""" subplot.legend和plt.legend都可以设置图例,如果不设置label或label='nolegend'则不会生成图例 """
""" 注解以及在subplot上绘图 """
""" annotate待解 """
# fig109_5 = plt.figure()
# ax109_5 = fig109_5.add_subplot(1, 1, 1)

# df109_5 = pd.read_csv('d:/notes-python/examples/spx.csv', index_col=0, parse_dates=True)
# df109_5_spx = df109_5['SPX']

""" 用pandas的df.plot方法生成图像 """
# tb109_5=df109_5_spx.plot(ax=ax109_5,style='b-')
""" ax.plot方法后续更新需要强制声明时间转换方法,因此不再适用 """
# ax109_5.plot(df109_5_spx,'r-')

# crisis_df109_5 = [
#                   (dt(2007, 10, 11), '牛市巅峰'),
#                   (dt(2008, 3, 12), 'Bear Stearns Fails'),
#                   (dt(2008, 9, 15), '雷曼破产')
#                   ]
""" df.asof方法索引:如果索引存在且值非null,则返回目标值;如果索引不存在或值为null,则返回目标值前面最近的非null值;subset参数用于指定判断null值的列,默认为none,即全判断 """
# for (date, label) in crisis_df109_5:
#     ax109_5.annotate(
#                label, 
#                xytext=(
#                         date, 
#                         df109_5_spx.asof(date) + 225
#                      ),
#                xy=(
#                      date,
#                      df109_5_spx.asof(date) + 75
#                   ),
#                arrowprops=dict(
#                                  facecolor='purple', 
#                                  headwidth=4, 
#                                  width=2,
#                                  headlength=4
#                               ),
#                 horizontalalignment='left', 
#                 verticalalignment='top'
#                 )

# Zoom in on 2007-2010
""" set_xlim和set_ylim设置x轴和y轴起止值 """
# ax109_5.set_xlim(['1/1/2007', '1/1/2011'])
# ax109_5.set_ylim([600, 1800])

# ax109_5.set_title('Important dates in the 2008-2009 financial crisis')
# ax109_5.set(ylabel='标普指数',xlabel='时间点')
""" 将图表保存到文件 """
""" 保存全部图表至1个文件中 """
# plt.savefig('d:/notes-python/examples/dates-in-financial-crisis-1.pdf',dpi=800,bbox_inches='tight')
""" 保存指定图表 """
# fig109_5.savefig('d:/notes-python/examples/dates-in-financial-crisis-2.pdf',dpi=800,bbox_inches='tight')
# tb109_5.get_figure().savefig('d:/notes-python/examples/dates-in-financial-crisis-3.pdf',dpi=800,bbox_inches='tight')
""" matplotlib配置 """
""" plt.rc用于配置matplotlib的参数,详见import matplotlib段 """
""" 使用pandas和seaborn绘图 """
# sr109_6=sr(np.random.randn(10).cumsum(),index=np.arange(0,100,10))
# fig109_6,axes109_6=plt.subplots(4,1)
""" ax参数用于指定绘图subplot,没有指定时默认为当前subplot """
# sr109_6.plot(ax=axes109_6[0],kind='line',figsize=(6,6))
# sr109_6.plot(ax=axes109_6[1],kind='bar',figsize=(6,6))
# sr109_6.plot(ax=axes109_6[2],kind='barh',figsize=(6,20))
# sr109_6.plot(ax=axes109_6[3],kind='kde',figsize=(6,6))
# fig109_6.subplots_adjust(left=None,bottom=None, right=None, top=None,wspace=0.1, hspace=0.3)
""" 线形图 """
""" df的绘图会自动在图表上创建图例,df.plot和sr.plot默认就是df.plot.line和sr.plot.line """
""" df.plot中subplots=True则不同列分别绘制于不同subplot """
""" 柱状图 """
""" plot.bar用于绘制垂直条形图,plot.barh用于绘制水平条形图(此时横轴显示值,纵轴显示索引) """
""" 柱状图中stacked=True则设置为堆积柱状图 """
# df109_7=pd.read_csv('D:/notes-python/examples/tips.csv')
# df109_7['tip_pct']=df109_7['tip']/(df109_7['total_bill']-df109_7['tip'])
# p(df109_7.head())
""" 使用seaborn绘图时,可以减少工作量,图片中柱状图显示的是平均数,而黑线表示默认的95%置信区间的取值范围(可以设置) """
# sns.barplot(x=df109_7['tip_pct'],y=df109_7['day'],hue='smoker',data=df109_7,orient='h')
# sns.set(style='whitegrid')
""" 直方图和密度图 """
""" 直方图histogram用于对散点值进行面元分析,密度图Kernel Density Estimate用于生成核密度估计 """
# fig109_7,axes109_7=plt.subplots(3,1)
# df109_7['tip_pct'].plot.hist(bins=50,ax=axes109_7[0])
# df109_7['tip_pct'].plot.density(ax=axes109_7[1])
""" sns绘制直方图和密度图 """
# arr109_8_1=np.random.normal(0,1,200)
# arr109_8_2=np.random.normal(10,2,200)
# sr109_8=sr(np.concatenate([arr109_8_1,arr109_8_2]))
# sns.distplot(sr109_8,100,color='k',ax=axes109_7[2])
""" 散布图或点图 """
# df109_9=pd.read_csv('D:/notes-python/examples/macrodata.csv')
# df109_9_slt=df109_9[['cpi','m1','tbilrate','unemp']]
# df109_9_slt_trans=np.log(df109_9_slt).diff().dropna()
# p(df109_9_slt_trans[-5:])
""" 使用sns的regplot方法制作散布图和线性回归线 """
# sns.regplot('m1','unemp',data=df109_9_slt_trans)
""" sns.pairplot用于在对角线上展示对应列的kde,在其他位置展现任意两两列的散点图 """
# sns.pairplot(df109_9_slt_trans, diag_kind='kde', plot_kws={'alpha': 0.2})
""" 分面网格和类型数据 """
""" 分面网格用于比较展示分组数据 """
# sns.factorplot(x='day', y='tip_pct', row='time',col='smoker',kind='bar', data=df109_7[df109_7['tip_pct'] < 1])
""" 箱型图用于展示中位数,四分位数和异常值 """
# sns.factorplot(x='tip_pct',y='day',kind='box',data=df109_7[df109_7['tip_pct']< 0.5])
""" pandas高级应用 """
""" 分类数据 """
""" pandas的分类类型 """
""" 用分类进行计算 """
""" 用分类提高性能 """
""" 分类方法 """
""" 为建模创建虚拟变量 """
""" groupby高级应用 """
""" 分组转换和解封groupby """
""" 分组的时间重采样 """
""" 链式编程技术 """
""" 管道方法 """

""" 数据分析案例 """
""" 解析json数据 """
""" 用movielens数据 """
""" 全美婴儿姓名 """
""" usda食品数据库 """
""" 联邦选举委员会数据库 """

