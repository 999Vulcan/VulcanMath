import fractions
import random
import sympy
# -*- coding: utf-8 -*-


""" Build Vulcan Math exercises """

def FracToStr(x):
    s = ""
    if x - int(x): s= "<sup> " + (str(x - int(x))).replace("/", "</sup>&frasl;<sub>") + "</sub>"
    if int(x) or s == "": s = (str(int(x))).rjust(2) + s
    return s

def GetFrac(l):
    while True:
        f = random.randint(l[0],l[1]) + fractions.Fraction(random.randint(l[2],l[3]), random.randint(l[2],l[3]))
        if f != int(f): return f

def BuildFractions(*args):
    for _ in range(args[0]):
        a, b = GetFrac(args[1:]), GetFrac(args[1:])
        sign = random.choice([-1, 1])
        if sign == -1: b, a = sorted((a, b))
        yield (FracToStr(a) + {1: ' + ', -1: ' - '}[sign] + FracToStr(b) + ' = ' + '_' * 28 +
              ' ' + FracToStr(a + sign * b) + '\n')

def Multiplication(*args):
    for _ in range(args[0]):
        a, c, b = random.randint(args[1],args[2]), random.randint(args[1],args[2]), random.randint(args[3],args[4])
        sign = random.choice([-1, 1])
        if sign == -1: c, a = sorted((a, c))
        yield str(a) + " &times; " + str(b) + {1: ' + ', -1: ' - '}[sign] + str(c) + ' = ' + '_' * 33 + " " + str(a * b + sign * c) + '\n'

def KGMath1(*args):
    for _ in range(args[0]):
        a, b = random.randint(args[1],args[2]), random.randint(args[1],args[2])
        yield str(a) + " + " + str(b) + ' = ' + '_' * 30 + " " + str(a + b) + '\n'

def KGMath2(*args):
    for _ in range(args[0]):
        a, b = random.randint(args[1],args[2]), random.randint(args[1],args[2])
        sign = 1
        if a + b > args[3]: sign, a , b = -1, max(a, b), min(a,b)
        yield str(a) + {1: ' + ', -1: ' - '}[sign] + str(b) + ' = ' + '_' * 30 + " " + str(a + sign * b) + '\n'

def Mult1(*args):
    numbers = [x for x in range(2, args[1]+1)]
    if 10 in numbers: numbers.remove(10)
    for _ in range(args[0]):
        a, b = random.choice(numbers), random.choice(numbers)
        yield (' ' + str(a))[-2:] + " &times; " + (str(b)+' ')[:2] + ' = ' + '_' * 30 + " " + str(a * b) + '\n'

def Equations1(*args):
    for _ in range(args[0]):
        filler = "_" * 33 + " " 
        a, b = random.randint(args[1],args[2]), random.randint(args[1],args[2])
        a, b = max(a, b), min(a,b)
        yield {1:str(b) + " + x = " + str(a) + "  x = " + filler + str(a - b) + "\n",
               2:str(a*2) + " - x = " + str(b) + "  x = " + filler + str(a*2 - b) + "\n",
               3:"x - " + str(a) + " = " + str(b) + "  x = " + filler + str(a + b) + "\n",
               4:"x + " + str(b) + " = " + str(a) + "  x = " + filler + str(a - b) + "\n"}[random.choice(range(1,5))]

def FormatBinomial(s):
    s1 = str(s).replace("**", "^").replace("*", "").replace(" ", "")
    while "^" in s1:
        n = s1.find("^")
        s1 = s1[:n] + "<sup>" + s1[n+1] + "</sup>" + s1[n+2:]
    return s1

def Binomials(*args):
    x = sympy.symbols('x')
    for _ in range(args[0]):
        n = random.randint(args[1],args[2])* x + random.choice([-1, 1]) * random.randint(args[1],args[3])
        m = random.randint(args[1],args[2])* x + random.choice([-1, 1]) * random.randint(args[1],args[3])
        yield ("(" + FormatBinomial(n)).rjust(7) + ")&times;(" + (FormatBinomial(m) + ")").ljust(7) + " = " + "_" * 17 + " " + FormatBinomial(sympy.expand(n*m))+"\n"
