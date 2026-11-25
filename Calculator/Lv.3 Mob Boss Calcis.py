cal = str(input("Skall vi komme i gang å regne :) ja/nei"))

while cal == "ja":
    x = float(input("Gi meg et tall"))
    o = str(input("Ka vil du gjør +,-,*,/,**,%"))
    y = float(input("Gi meg et til tall"))

    if o == "+":
        print(x,o,y,"=",x+y)
    elif o == "-":
        print(x,o,y,"=",x-y)
    elif o == "*":
        print(x,o,y,"=",x*y)
    elif o == "/":
        print(x,o,y,"=",x/y)
    elif o == "%":
        print(x,o,y,"=",x/y*100,"%")
    else:
        print(x,o,y,"=",x**y)

    cal = str(input("Klar for en til :) ja/nei"))

print("...")
print(":(")
