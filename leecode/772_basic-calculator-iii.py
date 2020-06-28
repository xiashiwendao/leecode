# 获取二元运算结果
def caculate(s, startPos, isFirst=False):
    num1, pos, oper = getNextNumAndOper(s, startPos)
    # oper is None，说明已经到尾部，直接返回num1作为运算结果
    if oper is None:
        return num1

    # 如果运算是加法和减法，计算优先级比较低，所以则获取后面数据的计算结果
    if oper in ["+", "-"]:
        num2 = caculate(s, pos)
    # 如果是乘法和除法，优先级别搞，所以先进行计算
    else:
        num2, pos, oper_2 = getNextNumAndOper(s, pos)
        # 高优先级计算
        num1 = caculator[oper](num1, num2)
        # 运算符不为None（后面还有运算符和数字）
        if(oper_2 is not None):
            oper = oper_2
            num2 = caculate(s, pos)
        # 如果是分析到了字符串的尾部，Oper返回为None，此时做一个伪计算，用于最后统一出口就算
        else:
            oper = "+"
            num2 = 0

    return caculator[oper](num1, num2)

# 获取操作数以及操作数后面的运算符
def getNextNumAndOper(s, startPos):
    num_str = ""
    pos = 0
    oper = None
    for pos in range(startPos, len(s)):
        ch = s[pos]
        if ch.isdigit():
            num_str += ch
            continue

        if ch in ["+", "-", "*", "/"]:
            # 操作符不存在，说明是开始解析，继续解析后面的数字
            if oper is None:
                oper = ch
                break
        # 当增加到大小括号的时候，发现有问题，这种数据结构的设置无法很好地满足需要
        if ch == "(":
            for pos_2 in range(pos, len(s)):
                pass

    next_pos = pos + 1
    return int(num_str), next_pos, oper

# 计算q中最高优先级运算的结果计算
def caculate_ver2(q):
    num1, oper = getNextNumAndOper_ver2(q)
    # oper is None，说明已经到尾部，直接返回num1作为运算结果
    if oper is None:
        return num1

    # 如果运算是加法和减法，计算优先级比较低，所以则获取后面数据的计算结果
    if oper in ["+", "-"]:
        num2 = caculate_ver2(q)
    # 如果是乘法和除法，优先级别最高（括号的优先级最高，不过在getNextNumAndOper_ver2
    # 中将会被处理，所以caculated_ver2只考虑乘除法
    else:
        num2, oper_2 = getNextNumAndOper_ver2(q)
        # 高优先级运算计算，结果作为num1
        num1 = caculator[oper](num1, num2)
        # 运算符不为None（后面还有运算符和数字），获取num2
        if(oper_2 is not None):
            oper = oper_2
            num2 = caculate_ver2(q)
        # 如果是分析到了字符串的尾部，Oper返回为None，此时做一个伪计算，用于最后统一出口就算
        else:
            oper = "+"
            num2 = 0

    return caculator[oper](num1, num2)

# 获取操作数以及操作数后面的运算符
def getNextNumAndOper_ver2(q):
    num_str = ""
    pos = 0
    oper = None
    while(len(q) > 0):
        ch = q.pop()
        if ch.isdigit():
            num_str += ch
            continue

        if ch in ["+", "-", "*", "/"]:
            # 操作符不存在，说明是开始解析，继续解析后面的数字
            if oper is None:
                oper = ch
                break
        if ch == "(":
            num_str = caculate_ver2(q)
        elif ch == ")":
            break

    return int(num_str), oper

caculator = {"+": lambda x, y: x+y,
             "-": lambda x, y: x-y,
             "*": lambda x, y: x*y,
             "/": lambda x, y: int(x/y)}

def caculate_ver3(q):
    num1_str = ""
    num1 = None
    oper = None
    num_oper_stack = []
    while(len(q) > 0):
        ch = q.pop()
        if ch.isdigit():
            num1_str += ch
            continue
        if ch in ["+", "-"]:
            oper = ch
            num2 = caculate_ver3(q)
        elif ch in ["*", "/"]:
            oper = ch
            num2 = getNextNum_ver3(q)
            num1 = caculator[oper](int(num1_str), num2)
            num1_str = str(num1)
            oper = None
        if ch == ")":
            q.append(ch) # 跳出的条件要保持到外层继续处理
            break
    if oper is None:
        ret = int(num1_str)
    else:
        ret = caculator[oper](int(num1_str), num2)

    return ret

def getNextNum_ver3(q):
    num_str = ""
    while(len(q) > 0):
        ch = q.pop()
        if ch == "(":
            num_str = str(caculate_ver3(q))  
        if ch.isdigit():
            num_str += ch
            continue
        elif ch == ")":
            break
        # 如果是运算符+-*/需要继续放入到队列中供后续使用
        else:
            q.append(ch)
            break
    
    return int(num_str)


def simpleOperation():
    # print(str(caculate("5+3*2+5+14*2", 0, True)))
    # s = "5+3*2+5+14*2"
    s = "5+3*2+6"
    # s = "5+3*2"
    q = []
    for ch in s:
        q.insert(0, ch)

    print(str(caculate_ver3(q)))
    # print(str(caculate("5+3*2", 0, True)))
def complexOperation():
    s = "5*(3+2)+5"
    q = []
    for ch in s:
        q.insert(0, ch)
    print(str(caculate_ver3(q)))

if __name__ == "__main__":
    simpleOperation()
    # complexOperation()
    

