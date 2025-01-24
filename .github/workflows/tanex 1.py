# tanex 1

# 导入正则表达式库
import re
# 导入数学库
import math
# 导入随机库
import random

'''
数据类型:
character_string:"*"
integer:'*'
decimal:`*`
list:{*,*,*...}
address:<*,*,*...>
'''

'''
运算符:
*+*
*-*
*/*
*%*
*>*
*<*
*=*
*==*
*!=*
*>=*
*<=*
*&&*
*||*
*=*
*;*
'''

'''
函数:
input:输入
output:输出
end:结束
power:幂
square_root:平方根
abs:绝对值
round:四舍五入
random:随机数
random_int:随机整数
random_float:随机浮点数
random_char:随机字符
random_string:随机字符串
ceil:向上取整
floor:向下取整
sin:正弦
cos:余弦
tan:正切
asin:反正弦
acos:反余弦
atan:反正切
atan2:反正切2
pi:圆周率
e:自然常数
log:对数
log10:以10为底的对数
exp:指数
pow:幂
sqrt:平方根
factorial:阶乘
gcd:最大公约数
lcm:最小公倍数
split:分割
replace:替换
find:查找
max:最大值
min:最小值
definition_character_string:定义字符串
definition_integer:定义整数
definition_decimal:定义小数
definition_list:定义列表
definition_address:定义地址
definition_dictionary:定义字典
character_string:转字符串
integer:转整数
decimal:转小数
item:取列表元素
finally:取字典元素
key:取字典键
value:取字典值
length:取列表长度
if:条件语句
in:包含
not_in:不包含
not:非
'''
x=0
end_=False#结束标志(如果运算end函数,则结束)

# 变量库，key:变量名，value:[变量值,变量类型]
bian_liang_list={}

# 函数库，key:函数名，value:[函数内容，函数参数的个数，[函数类型]]
han_shu_list = {
    "input": [input, 0, ["character_string"]],#input
    "output": [print, 1, ["character_string"]],#output 内容
    "end": [lambda: globals().update({"end_": True}), 0, []],#end
    "power": [pow,2, ["decimal", "decimal"]],#power 底数 指数
    "square_root": [math.sqrt,1, ["decimal"]],#square_root 被开方数
    "abs": [abs,1, ["decimal"]],#abs 数
    "round": [round,2, ["decimal", "integer"]],#round 数 精度
    "random": [random,2, ["decimal", "decimal"]],#random 数 数
    "ceil": [math.ceil,1, ["decimal"]],#ceil 数
    "floor": [math.floor,1, ["decimal"]],#floor 数
    "sin": [math.sin,1, ["decimal"]],#sin 数
    "cos": [math.cos,1, ["decimal"]],#cos 数
    "tan": [math.tan,1, ["decimal"]],#tan 数
    "asin": [math.asin,1, ["decimal"]],#asin 数
    "acos": [math.acos,1, ["decimal"]],#acos 数
    "atan": [math.atan,1, ["decimal"]],#atan 数
    "atan2": [math.atan2,2, ["decimal", "decimal"]],#atan2 数 数
    "pi": [math.pi,0, ["decimal"]],#pi
    "e": [math.e,0, ["decimal"]],#e
    "log": [math.log,1, ["decimal"]],#log 数
    "log10": [math.log10,1, ["decimal"]],#log10 数
    "exp": [math.exp,1, ["decimal"]],#exp 数
    "pow": [pow,2, ["decimal", "decimal"]],#pow 底数 指数
    "sqrt": [math.sqrt,1, ["decimal"]],#sqrt 被开方数
    "factorial": [math.factorial,1, ["integer"]],#factorial 数
    "gcd": [math.gcd,2, ["integer", "integer"]],#gcd 数 数
    "lcm": [math.lcm,2, ["integer", "integer"]],#lcm 数 数
    "split": [str.split,2, ["character_string", "character_string"]],#split 字符串 分隔符
    "replace": [str.replace,3, ["character_string", "character_string", "character_string"]],#replace 字符串 旧字符 新字符
    "find": [str.find,2, ["character_string", "character_string"]],#find 字符串 字符
    "max": [max,2, ["integer", "integer"]],#max 数 数
    "min": [min,2, ["integer", "integer"]],#min 数 数
    "definition_character_string": [lambda x: globals().update({x: [x, "character_string"]}), 1, ["character_string"]],#definition 变量 字符串
    "definition_integer": [lambda x: globals().update({x: [x, "integer"]}), 1, ["integer"]],#definition 变量 整数
    "definition_decimal": [lambda x: globals().update({x: [x, "decimal"]}), 1, ["decimal"]],#definition 变量 小数
    "definition_list": [lambda x: globals().update({x: [x, "list"]}), 1, ["list"]],#definition 变量 列表
    "definition_address": [lambda x: globals().update({x: [x, "address"]}), 1, ["address"]],#definition 变量 地址
    "definition_dictionary": [lambda x: globals().update({x: [x, "dictionary"]}), 1, ["dictionary"]],#definition 变量 字典
    "character_string":[str,1, ["character_string"]],#character_string 值
    "integer":[int,1, ["integer"]],#integer 值
    "decimal":[float,1, ["decimal"]],#decimal 值
    "item":[lambda x,y: x[y], 2, ["list", "integer"]],#item 列表 索引
    "finally":[lambda x,y: x[y], 2, ["dictionary", "character_string"]],#finally 列表 索引
    "key":[lambda x: x, 2, ["dictionary", "character_string"]],#key 字典
    "value":[lambda x: x, 2, ["dictionary", "character_string"]],#value 字典
    "length":[lambda x: len(x), 1, ["list"]],#length 列表
    "if":[lambda x,y,z: x if y else z, 3, ["character_string", "character_string", "character_string"]],#if 条件
    "in":[lambda x,y: str(int(x in y)), 2, ["character_string", "character_string"]],#in 变量 变量
    "not_in":[lambda x,y: str(int(x not in y)), 2, ["character_string", "character_string"]],#not_in 变量 变量
    "not":[lambda x:x=="1" if x=="0" else "1", 1, ["character_string"]],#not 条件
}

def han_shu(name, args):
    if name in han_shu_list:
        if type(han_shu_list[name][0]) != str:
            if len(args) == han_shu_list[name][1]:
                return han_shu_list[name][0](*args)
            else:
                bao_cuo("参数数量错误", 1)
                return ''
        else:
            return han_shu_list[name][0]
    else:
        bao_cuo("函数不存在", 1)
        return ''

def bao_cuo(nr,y):#这是报错函数
    global end_
    print(nr,end=",")
    print("在第"+str(x)+"行,"+"第"+str(y)+"列")
    end_=True#结束标志

def lei_xing(zhi):
    if zhi[0]=="\"":
        return "character_string"
    elif zhi[0]=="'":
        return "integer"
    elif zhi[0]=="`":
        return "decimal"
    elif zhi[0]=="{":
        return "list"
    elif zhi[0]=="<":
        return "address"
    elif zhi[0]=="[":
        return "variable"
    else:
        return "function"
#运算函数
def yun_suan(dm):
    if dm[1]=="+":#加法
        if lei_xing(dm[0])==lei_xing(dm[2]):
            if lei_xing(dm[0])=="character_string":
                return "\""+str(dm[0][1:-1])+str(dm[2][1:-1])+"\""
            elif lei_xing(dm[0])=="integer":
                return "'"+str(int(dm[0][1:-1]))+str(int(dm[2][1:-1]))+"'"
            elif lei_xing(dm[0])=="decimal":
                return "`"+str(float(dm[0][1:-1]))+str(float(dm[2][1:-1]))+"`"
            elif lei_xing(dm[0])=="list":
                return str(dm[0][:-1])+str(dm[2][0:])
            elif lei_xing(dm[0])=="address":
                return str(dm[0][:-1])+str(dm[2][0:])
            elif lei_xing(dm[0])=="variable":
                return bian_liang_list[dm[0]]+"+"+bian_liang_list[dm[2]]
            elif lei_xing(dm[0])=="function":
                return han_shu(dm[0])+"+"+han_shu(dm[2])
        else:
            bao_cuo("类型错误", 1)
            return ''
    elif dm[1]=="-":#减法
        if lei_xing(dm[0])==lei_xing(dm[2]):
            if lei_xing(dm[0])=="character_string":
                return "\""+str(str(dm[0][1:-1])-str(dm[2][1:-1]))+"\""
            elif lei_xing(dm[0])=="integer":
                return "'"+str(int(dm[0][1:-1]))-str(int(dm[2][1:-1]))+"'"
            elif lei_xing(dm[0])=="decimal":
                return "`"+str(float(dm[0][1:-1]))-str(float(dm[2][1:-1]))+"`"
            elif lei_xing(dm[0])=="list":
                bao_cuo("列表不能进行减法运算", 1)
                return ""
            elif lei_xing(dm[0])=="address":
                bao_cuo("地址不能进行减法运算", 1)
                return ""
            elif lei_xing(dm[0])=="variable":
                return bian_liang_list[dm[0]]+"-"+bian_liang_list[dm[2]]
            elif lei_xing(dm[0])=="function":
                return han_shu(dm[0])+"-"+han_shu(dm[2])
        else:
            bao_cuo("类型错误", 1)
            return ''
    elif dm[1]=="*":#乘法
        if lei_xing(dm[0])==lei_xing(dm[2]):
            if lei_xing(dm[0])=="character_string":
                bao_cuo("字符串不能进行乘法运算", 1)
                return ""
            elif lei_xing(dm[0])=="integer":
                return "'"+str(int(dm[0][1:-1]))*str(int(dm[2][1:-1]))+"'"
            elif lei_xing(dm[0])=="decimal":
                return "`"+str(float(dm[0][1:-1]))*str(float(dm[2][1:-1]))+"`"
            elif lei_xing(dm[0])=="list":
                bao_cuo("列表不能进行乘法运算", 1)
                return ""
            elif lei_xing(dm[0])=="address":
                bao_cuo("地址不能进行乘法运算", 1)
                return ""
            elif lei_xing(dm[0])=="variable":
                return bian_liang_list[dm[0]]+"*"+bian_liang_list[dm[2]]
            elif lei_xing(dm[0])=="function":
                return han_shu(dm[0])+"*"+han_shu(dm[2])
        else:
            bao_cuo("类型错误", 1)
            return ''
    elif dm[1]=="/":#除法
        if lei_xing(dm[0])==lei_xing(dm[2]):
            if lei_xing(dm[0])=="character_string":
                bao_cuo("字符串不能进行除法运算", 1)
                return ""
            elif lei_xing(dm[0])=="integer":
                return "'"+str(int(dm[0][1:-1])/int(dm[2][1:-1]))+"'"
            elif lei_xing(dm[0])=="decimal":
                return "`"+str(float(dm[0][1:-1])/float(dm[2][1:-1]))+"`"
            elif lei_xing(dm[0])=="list":
                bao_cuo("列表不能进行除法运算", 1)
                return ""
            elif lei_xing(dm[0])=="address":
                bao_cuo("地址不能进行除法运算", 1)
                return ""
            elif lei_xing(dm[0])=="variable":
                return bian_liang_list[dm[0]]+"/"+bian_liang_list[dm[2]]
            elif lei_xing(dm[0])=="function":
                return han_shu(dm[0])+"/"+han_shu(dm[2])
        else:
            bao_cuo("类型错误", 1)
            return ''
    elif dm[1]=="%":#取余
        if lei_xing(dm[0])==lei_xing(dm[2]):
            if lei_xing(dm[0])=="character_string":
                bao_cuo("字符串不能进行取余运算", 1)
                return ""
            elif lei_xing(dm[0])=="integer":
                return "'"+str(int(dm[0][1:-1])%int(dm[2][1:-1]))+"'"
            elif lei_xing(dm[0])=="decimal":
                return "`"+str(float(dm[0][1:-1])%float(dm[2][1:-1]))+"`"
            elif lei_xing(dm[0])=="list":
                bao_cuo("列表不能进行取余运算", 1)
                return ""
            elif lei_xing(dm[0])=="address":
                bao_cuo("地址不能进行取余运算", 1)
                return ""
            elif lei_xing(dm[0])=="variable":
                return bian_liang_list[dm[0]]+"%"+bian_liang_list[dm[2]]
            elif lei_xing(dm[0])=="function":
                return han_shu(dm[0])+"%"+han_shu(dm[2])
        else:
            bao_cuo("类型错误", 1)
            return ''
    elif dm[1]==">":#大于
        if lei_xing(dm[0])==lei_xing(dm[2]):
            if lei_xing(dm[0])=="character_string":
                bao_cuo("字符串不能进行大于运算", 1)
                return ""
            elif lei_xing(dm[0])=="integer":
                return "'"+str(int(int(dm[0][1:-1])>int(dm[2][1:-1])))+"'"
            elif lei_xing(dm[0])=="decimal":
                return "`"+str(int(float(dm[0][1:-1])>float(dm[2][1:-1])))+"`"
            elif lei_xing(dm[0])=="list":
                bao_cuo("列表不能进行大于运算", 1)
                return ""
            elif lei_xing(dm[0])=="address":
                bao_cuo("地址不能进行大于运算", 1)
                return ""
            elif lei_xing(dm[0])=="variable":
                return bian_liang_list[dm[0]]+">"+bian_liang_list[dm[2]]
            elif lei_xing(dm[0])=="function":
                return han_shu(dm[0])+">"+han_shu(dm[2])
        else:
            bao_cuo("类型错误", 1)
            return ''
    elif dm[1]=="<":#小于
        if lei_xing(dm[0])==lei_xing(dm[2]):
            if lei_xing(dm[0])=="character_string":
                bao_cuo("字符串不能进行小于运算", 1)
                return ""
            elif lei_xing(dm[0])=="integer":
                return "'"+str(int(int(dm[0][1:-1])<int(dm[2][1:-1])))+"'"
            elif lei_xing(dm[0])=="decimal":
                return "`"+str(int(float(dm[0][1:-1])<float(dm[2][1:-1])))+"`"
            elif lei_xing(dm[0])=="list":
                bao_cuo("列表不能进行小于运算", 1)
                return ""
            elif lei_xing(dm[0])=="address":
                bao_cuo("地址不能进行小于运算", 1)
                return ""
            elif lei_xing(dm[0])=="variable":
                return bian_liang_list[dm[0]]+"<"+bian_liang_list[dm[2]]
            elif lei_xing(dm[0])=="function":
                return han_shu(dm[0])+"<"+han_shu(dm[2])
        else:
            bao_cuo("类型错误", 1)
            return ''
    elif dm[1]=="==":#等于
        if lei_xing(dm[0])==lei_xing(dm[2]):
            if lei_xing(dm[0])=="character_string":
                return str(int((dm[0][1:-1]==(dm[2][1:-1]))))
            elif lei_xing(dm[0])=="integer":
                return "'"+str(int(int(dm[0][1:-1])))==str(int(int(dm[2][1:-1])))+"'"
            elif lei_xing(dm[0])=="decimal":
                return "`"+str(int((float(dm[0][1:-1]))==(float(dm[2][1:-1]))))+"`"
            elif lei_xing(dm[0])=="list":
                return str(int(dm[0]==dm[2]))
            elif lei_xing(dm[0])=="address":
                return str(int(dm[0]==dm[2]))
            elif lei_xing(dm[0])=="variable":
                return bian_liang_list[dm[0]]+"=="+bian_liang_list[dm[2]]
            elif lei_xing(dm[0])=="function":
                return han_shu(dm[0])+"=="+han_shu(dm[2])
        else:
            bao_cuo("类型错误", 1)
            return ''
    elif dm[1]=="!=":#不等于
        if lei_xing(dm[0])==lei_xing(dm[2]):
            if lei_xing(dm[0])=="character_string":
                return str(int(dm[0][1:-1]!=dm[2][1:-1]))
            elif lei_xing(dm[0])=="integer":
                return "'"+str(int(int(dm[0][1:-1])!=int(dm[2][1:-1])))+"'"
            elif lei_xing(dm[0])=="decimal":
                return "`"+str(int(float(dm[0][1:-1])!=float(dm[2][1:-1])))+"`"
            elif lei_xing(dm[0])=="list":
                return str(int(dm[0]!=dm[2]))
            elif lei_xing(dm[0])=="address":
                return str(int(dm[0]!=dm[2]))
            elif lei_xing(dm[0])=="variable":
                return bian_liang_list[dm[0]]+"!="+bian_liang_list[dm[2]]
            elif lei_xing(dm[0])=="function":
                return han_shu(dm[0])+"!="+han_shu(dm[2])
        else:
            bao_cuo("类型错误", 1)
            return ''
    elif dm[1]==">=":#大于等于
        if lei_xing(dm[0])==lei_xing(dm[2]):
            if lei_xing(dm[0])=="character_string":
                bao_cuo("字符串不能进行大于等于运算", 1)
                return ""
            elif lei_xing(dm[0])=="integer":
                return "'"+str(int(int(dm[0][1:-1])>=int(dm[2][1:-1])))+"'"
            elif lei_xing(dm[0])=="decimal":
                return "`"+str(int(float(dm[0][1:-1])>=float(dm[2][1:-1])))+"`"
            elif lei_xing(dm[0])=="list":
                bao_cuo("列表不能进行大于等于运算", 1)
                return ""
            elif lei_xing(dm[0])=="address":
                bao_cuo("地址不能进行大于等于运算", 1)
                return ""
            elif lei_xing(dm[0])=="variable":
                return bian_liang_list[dm[0]]+">="+bian_liang_list[dm[2]]
            elif lei_xing(dm[0])=="function":
                return han_shu(dm[0])+">="+han_shu(dm[2])
        else:
            bao_cuo("类型错误", 1)
            return ''
    elif dm[1]=="<=":#小于等于
        if lei_xing(dm[0])==lei_xing(dm[2]):
            if lei_xing(dm[0])=="character_string":
                bao_cuo("字符串不能进行小于等于运算", 1)
                return ""
            elif lei_xing(dm[0])=="integer":
                return "'"+str(int(int(dm[0][1:-1])<=int(dm[2][1:-1])))+"'"
            elif lei_xing(dm[0])=="decimal":
                return "`"+str(int(float(dm[0][1:-1])<=float(dm[2][1:-1])))+"`"
            elif lei_xing(dm[0])=="list":
                bao_cuo("列表不能进行小于等于运算", 1)
                return ""
            elif lei_xing(dm[0])=="address":
                bao_cuo("地址不能进行小于等于运算", 1)
                return ""
            elif lei_xing(dm[0])=="variable":
                return bian_liang_list[dm[0]]+"<="+bian_liang_list[dm[2]]
            elif lei_xing(dm[0])=="function":
                return han_shu(dm[0])+"<="+han_shu(dm[2])
        else:
            bao_cuo("类型错误", 1)
            return ''
    elif dm[1]=="&&":#与运算
        if lei_xing(dm[0])==lei_xing(dm[2]):
            if lei_xing(dm[0])=="character_string":
                bao_cuo("字符串不能进行与运算", 1)
                return ""
            elif lei_xing(dm[0])=="integer":
                if dm[0][1:-1]=='\'0\'' or dm[0][1:-1]=='\'1\'':
                    if dm[2][1:-1]=='\'0\'' or dm[2][1:-1]=='\'1\'':
                        return "'1'"
                    else:
                        return "'0'"
                else:
                    bao_cuo("整数只能为0或1才能进行与运算", 1)
                    return ""
            elif lei_xing(dm[0])=="decimal":
                bao_cuo("小数不能进行与运算", 1)
                return ""
            elif lei_xing(dm[0])=="list":
                bao_cuo("列表不能进行与运算", 1)
                return ""
            elif lei_xing(dm[0])=="address":
                bao_cuo("地址不能进行与运算", 1)
                return ""
            elif lei_xing(dm[0])=="variable":
                return bian_liang_list[dm[0]]+"&&"+bian_liang_list[dm[2]]
            elif lei_xing(dm[0])=="function":
                return han_shu(dm[0])+"&&"+han_shu(dm[2])
        else:
            bao_cuo("类型错误", 1)
            return ''
    elif dm[1]=="||":#或运算
        if lei_xing(dm[0])==lei_xing(dm[2]):
            if lei_xing(dm[0])=="character_string":
                bao_cuo("字符串不能进行或运算", 1)
                return ""
            elif lei_xing(dm[0])=="integer":
                if dm[0][1:-1]=='\'0\'' or dm[0][1:-1]=='\'1\'':
                    if dm[2][1:-1]=='\'0\'' or dm[2][1:-1]=='\'1\'':
                        return "'1'"
                    else:
                        return "'0'"
                else:
                    bao_cuo("整数只能为0或1才能进行或运算", 1)
                    return ""
            elif lei_xing(dm[0])=="decimal":
                bao_cuo("小数不能进行或运算", 1)
                return ""
            elif lei_xing(dm[0])=="list":
                bao_cuo("列表不能进行或运算", 1)
                return ""
            elif lei_xing(dm[0])=="address":
                bao_cuo("地址不能进行或运算", 1)
                return ""
            elif lei_xing(dm[0])=="variable":
                return bian_liang_list[dm[0]]+"||"+bian_liang_list[dm[2]]
            elif lei_xing(dm[0])=="function":
                return han_shu(dm[0])+"||"+han_shu(dm[2])
        else:
            bao_cuo("类型错误", 1)
            return ''

#优先级运算
shun_xu=("(",")","*","/","%","+","-","==","!=",">","<","<=",">=","&&","||","=",";")#顺序
you_xian=""
zong_dai_ma=""
lin_shi=[]
#优先级运算函数
def you_xian_suan(dm):
    you_xian=dm
    zong_dai_ma=dm#全局变量
    if dm:
        for i in shun_xu:
            if i in dm:
                if i=="(" or i==")":
                    you_xian=you_xian[you_xian.index(i[0]):you_xian.index(i[1])+1]
                    lin_shi=[you_xian.index(i[0]),you_xian.index(i[1])]
                elif i==";":
                    return zong_dai_ma
                else:
                    lin_shi=[you_xian.index(i),you_xian.index(i)]
                    while 1:
                        lin_shi[0]-=1
                        if zong_dai_ma[lin_shi[0]]in shun_xu:
                            break
                    while 1:
                        lin_shi[1]+=1
                        if zong_dai_ma[lin_shi[1]]in shun_xu:
                            break
                    you_xian=you_xian[lin_shi[0]+1:lin_shi[1]-1]
            if lei_xing(you_xian[0]) != '' and lei_xing(you_xian[2]) != '':
                zong_dai_ma=zong_dai_ma[0:lin_shi[0]]+yun_suan(you_xian)+zong_dai_ma[lin_shi[1]:]
                you_xian_suan(zong_dai_ma)
            else:
                bao_cuo("类型错误", 1)
                return ''

fen_ge=("+","-","*","/","%",">","<","=","==","!=",">=","<=","&&","||",";","(",")","[","]","{","}")
def split_string(dm):
    while True:
        for i in range(len(fen_ge)):
            if fen_ge[i] in dm:
                dm=dm.split(fen_ge[i])
                you_xian_suan(dm)

if __name__ == "__main__":
    print('tanex 1 中文版')
    x = 0  # 重置行号
    while True:
        if(end_):
            print("运行结束")  # 这是结束的标志
            break
        x += 1  # 先增加行号
        dai_ma = input()
        dai_ma = split_string(dai_ma)
        if(dai_ma):  # 如果输入的代码不为空，则运行
            result = yun_suan(dai_ma)