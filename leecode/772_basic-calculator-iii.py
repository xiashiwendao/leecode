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

    next_pos = pos + 1
    return int(num_str), next_pos, oper

caculator = {"+": lambda x, y: x+y,
             "-": lambda x, y: x-y,
             "*": lambda x, y: x*y,
             "/": lambda x, y: int(x/y)}

if __name__ == "__main__":
    print(str(caculate("5+3*2+5+14*2", 0, True)))
    # print(str(caculate("5+3*2", 0, True)))
