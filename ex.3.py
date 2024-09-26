number = int(input("輸⼊數字 : "))
result = "是奇數" * (number % 2 == 1) + "是偶數" * (number % 2 == 0)
print("結果 :", number, result)