import math

def addition(x, y, func=None):
    return round(x+y, 3)

def subtraction(x,y, func=None):
    return round(x-y, 3)

def multyplication(x, y, func=None):
    return round(x*y, 3)

def division(x, y, func=None):
    return round(x/y, 3)

def raisetopower(x, y, func=None):
    return round(x**y, 3)

def remainder(x, y, func=None):
    return round(x%y, 3)

def sin(x, y, func=None):
    try:    
        res = func(x, y)
    except:
        res = x
    res = math.sin(res)
    
    return round(res, 3)

def cos(x, y, func=None):
    try:    
        res = func(x, y)
    except:
        res = x
    res = math.cos(res)
    return round(res, 3)

def tan(x, y, func=None):
    try:    
        res = func(x, y)
    except:
        res = x
    res = math.tan(res)
    return round(res, 3)

def po(x, y, func=None):
    pass

def permutation(x, y=None, func=None):
    return math.factorial(x)

def arrangement(x, y, func=None):
    res = math.factorial(x)/(math.factorial(x-y))
    return res

def combination(x, y, func=None):
    res = res = math.factorial(x)/(math.factorial(x-y)*math.factorial(y))
    return res

word_to_number_dict = {"один": 1, "два": 2, "три": 3, "четыре": 4, "пять": 5, "шесть": 6, "семь": 7,
                      "восемь": 8, "девять": 9, "десять": 10, "одиннадцать": 11, "двенадцать": 12, "тринадцать": 13,
                      "четырнадцать": 14, "пятнадцать": 15, "шестнадцать": 16, "семьнадцать": 17, "восемнадцать": 18,
                      "девятнадцать": 19, "двадцать": 20, "тридцать": 30, "сорок": 40, "пятьдесят": 50, "шестьдесят": 60,
                      "семьдесят": 70, "восемьдесят": 80, "девяносто": 90, "сто": 100, "двести": 200, "триста": 300, "четыреста": 400,
                        "пятьсот": 500, "шестьсот": 600, "семьсот": 700, "восемьсот": 800, "девятьсот": 900, "тысяча": 1000, "пи": math.pi,
                        "миллион": 1_000_000, "миллиард": 1_000_000_000, "триллион": 1_000_000_000_000,}

word_to_sign_dict = {"плюс": addition, "минус": subtraction, "умножить": multyplication, "разделить": division, "степени": raisetopower, 
                     "синус": sin, "косинус": cos, "тангенс": tan, "остаток": remainder, "по": po, "размещение": arrangement, "перестановка": permutation,
                     "сочетание": combination}

word_to_fraction_dict = {"десятых": 10, "сотых": 100, "тысячных": 1000}

def number_to_int(number=list):
    endnumber = 0
    endnumber_equal = 0
    endnumber_fraction = 0
    count = 0
    flag = 0
    for digit in number:
        if digit == "ноль":
            count += 1
            continue 
        if digit == "и":
            flag = 1
            endnumber_equal = endnumber
            endnumber = 0
            count += 1
            continue
        for word in word_to_number_dict.keys():
            if digit == word:
                endnumber += word_to_number_dict.get(word)
                count+=1
                break
        else:
            if flag == 1:
                for word in word_to_fraction_dict.keys():
                    if digit == word:
                        endnumber_fraction = float (endnumber / word_to_fraction_dict.get(word))
                        count+=1
                        break 
                endnumber = endnumber_equal + endnumber_fraction
            for i in range(count):
                number.pop(0)
            return endnumber, number  

def number_to_str(number):
    resultstr = ''
    flag = 0

    if int(number)!=number:
        number = str(number)
        resultlist = number.split(".")
        result_equal, result_fraction = resultlist
        number = result_equal
        flag = 1


    number = int(number)
    try:
        resultlist = list(map(int,[k for k in str(number)]))
    except:
        return "В ответе отрицательное или неопределённое число, вывод недоступен"
    resultlist.reverse()
    
    count = 0
    countcheck = 0
    for pos in range(len(resultlist)):
        if pos%3 == 0 and pos!=0:
            count += 1
        if count!=countcheck:
            resultlist.insert(pos+countcheck, 1000**count)
            countcheck = count
        resultlist[pos+count] *= (10**(pos%3))
        
    try:
        if resultlist[1]==10:
            resultlist[0]+=resultlist.pop(1)
    except:
        pass
    resultlist.reverse()

    if number == 0:
        resultstr += 'ноль ' 

    for number in resultlist:    
        for key, value in word_to_number_dict.items():
            if value == number:
                resultstr += key + ' '
                break
            else:
                continue
    
    if flag == 1:
        resultstr += 'и '
        fraction_len = 10**len(result_fraction)
        number = int(result_fraction)
        resultlist = list(map(int,[k for k in str(number)]))
        resultlist.reverse()

        for pos in range(len(resultlist)):
            resultlist[pos] *= (10**pos)
        try:
            if resultlist[1]==10:
                resultlist[0]+=resultlist.pop(1)
        except:
            pass
        resultlist.reverse()

        for number in resultlist:    
            for key, value in word_to_number_dict.items():
                if value == number:
                    resultstr += key + ' '
                    break
                else:
                    continue
        
        for key, value in word_to_fraction_dict.items():
            if value == fraction_len:
                resultstr += key
                break

    return resultstr

def find_operation(expr=list):
    for oper in expr:
        for word in word_to_sign_dict.keys():
            if oper == word:
                expr.pop(0)
                return word_to_sign_dict.get(word), expr
        else: 
            raise 'Ошибка'

def gigacalc(expr):
    # Эта часть кода приводит выражение в цифры и считает их
    expr = expr.replace(" на", "").replace(" в","").replace(" от","").replace(" из","")
    expr = (expr.split() + [''])
    checkexpr = list(expr)
    checkvalue, checklist = number_to_int(checkexpr)

    if len(checklist) == len(expr):
        try:
            func1, expr = find_operation(expr)
        except:
            return "Неправильно введено первое число или операция"
        num1, expr = number_to_int(expr)
        try:
            func2, expr = find_operation(expr)
        except: 
            func2 = None
        num2, expr = number_to_int(expr)
        
        if len(expr)>1:
            return "Некорректный ввод второй операции или второго числа"
        try:
            resultint = func1(num1, num2, func2)
        except ZeroDivisionError:
            return 'Делить на ноль нельзя' 
        except:
            return 'Неверный ввод числа или команды'
    else:
        num1, expr = number_to_int(expr)
        try:
            func, expr = find_operation(expr)
        except:
            return "Неправильно введена операция"
        num2, expr = number_to_int(expr)
        if len(expr)>1:
            return "Некорректный ввод операции или второго числа"
        try:
            resultint = func(num1, num2)
        except ZeroDivisionError:
            return 'Делить на ноль нельзя'
    # Эта часть кода переводит значение в буквы
    resultstr = number_to_str(resultint)
    return resultstr

if __name__== '__main__':
    print("""
          
          Моя версия текстового 
          Для остановки программы введите end""")
    while True: 
        expression = input('Введите выражение: ').lower()
        if expression == 'end':
            break
        print(gigacalc(expression))