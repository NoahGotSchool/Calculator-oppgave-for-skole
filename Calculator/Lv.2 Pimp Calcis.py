cal = str(input("Skall vi komme i gang å regne :) ja/nei"))
x = float(input("Gi meg et tall"))
o = str(input("Ka vil du gjør +,-,*,/,**"))
y = float(input("Gi meg et til tall"))
while cal == "ja":
    if o == "+":
        print(x,o,y,"=",x+y)
    elif o == "-":
        print(x,o,y,"=",x-y)
    elif o == "*":
        print(x,o,y,"=",x*y)
    elif o == "/":
        print(x,o,y,"=",x/y)
    else:
        print(x,o,y,"=",x**y)
    cal = str(input("Klar for en til ;) ja/nei"))
