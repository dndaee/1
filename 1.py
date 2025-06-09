def calculate_x(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Числа a та b повинні бути додатними.")

    if a < b:
        return a / b + 1
    elif a == b:
        return -1
    else:  # a > b
        return (a * b - 5) / a

try:
    a = float(input("Введіть число a (додатнє): "))
    b = float(input("Введіть число b (додатнє): "))
    
    x = calculate_x(a, b)
    print(f"Результат: X = {x:.2f}")
except ValueError as e:
    print("Помилка:", e)
except ZeroDivisionError:
    print("Помилка: ділення на нуль.")
