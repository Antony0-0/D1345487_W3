a = int(input("輸⼊係數 a : "))
b = int(input("輸⼊係數 b : "))
c = int(input("輸⼊係數 c : "))
x1 = (-b + (b**2 - 4*a*c)**0.5) / (a*2)
x2 = (-b - (b**2 - 4*a*c)**0.5) / (a*2)
print("⽅程式的根為：" + "x1 = " + str(x1) + ", x2 = "+ str(x2))