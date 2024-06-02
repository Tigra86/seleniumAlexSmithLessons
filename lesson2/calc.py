try:
    num_1 = int(input("Введите 1-е число: "))
except ValueError:
    num_1 = "Вы можете ввести только число"
    print(num_1)
    exit()

try:
    num_2 = int(input("Введите 2-е число: "))
except ValueError:
    num_2 = "Вы можете ввести только число"
    print(num_2)
    exit()

operand = input("Введите арифметический знак, один из: +, -, *, /: ")

if operand == "+":
    result = int(num_1 + num_2)
    print(f"Результат сложения {num_1} и {num_2} равен {result}")
elif operand == "-":
    result = int(num_1 - num_2)
    print(f"Результат вычитания {num_1} и {num_2} равен {result}")
elif operand == "*":
    result = int(num_1 * num_2)
    print(f"Результат умножения {num_1} и {num_2} равен {result}")
elif operand == "/":
    try:
        result = int(num_1 / num_2)
        print(f"Результат деления {num_1} и {num_2} равен {result}")
    except ZeroDivisionError:
        result = "На 0 делить нельзя"
        print(result)
else:
    print("Вы можете ввести только арифметический знак, один из: +, -, *, /")
    exit()
