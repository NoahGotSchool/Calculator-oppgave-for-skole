cal = str(input("Skall vi komme i gang å regne :) ja/nei"))
hist = []

while cal == "ja":
    x = float(input("Gi meg et tall"))
    o = str(input("Ka vil du gjør +,-,*,/,**,%"))
    y = float(input("Gi meg et til tall"))
    svar = 0
    
    if o == "+":
        print(x,o,y,"=",x+y)
        svar = x+y
    elif o == "-":
        print(x,o,y,"=",x-y)
        svar = x-y
    elif o == "*":
        print(x,o,y,"=",x*y)
        svar = x*y
    elif o == "/":
        print(x,o,y,"=",x/y)
        svar = x/y
    elif o == "%":
        print(x,o,y,"=",x/y*100,"%")
        svar = x/y*100 
    else:
        print(x,o,y,"=",x**y)
        svar = x**y
    hist.append(svar)
    print(hist)
    cal = str(input("Klar for en til :) ja/nei"))

print("...")
print(":(")
