x = int(input("Gi meg et tall"))
o = str(input("Ka vil du gjør +,-,*,/,**"))
y = int(input("Gi meg et til tall"))


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
