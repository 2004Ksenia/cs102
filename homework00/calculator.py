import math
import typing as tp


def calc(num_1: float, num_2: float, command: str) -> tp.Union[float, str]:
    if command == "+":
        return num_1 + num_2
    if command == "-":
        return num_1 - num_2
    if command == "*":
        return num_1 * num_2
    if command == "/":
        return num_1 / num_2
    if command == "**":
        return num_1**num_2
    else:
        return f"Неизвестный оператор: {command!r}."


def calc_1(num_1: float, command: str) -> tp.Union[float, str]:
    if command == "**2":
        return num_1**2
    if command == "**2":
        return num_1**2
    if command == "sin":
        return math.sin(num_1)
    if command == "cos":
        return math.cos(num_1)
    if command == "ln":
        return math.log(num_1)
    if command == "log10":
        return math.log10(num_1)
    if command == "tan":
        return math.tan(num_1)
    else:
        return f"Неизвестный оператор: {command!r}."


if __name__ == "__main__":
    while True:  # программа выполняется до ввода 0 вместо команды
        COMMAND = input("Введите оперцию > ")
        if COMMAND.isdigit() and int(COMMAND) == 0:
            break
        if COMMAND in ("+", "-", "*", "/", "**"):
            NUM_1 = float(input("Первое число > "))
            NUM_2 = float(input("Второе число > "))
            print(calc(NUM_1, NUM_2, COMMAND))
        if COMMAND in ("**2", "sin", "cos", "ln", "log10", "tan"):
            NUM_1 = float(input("Число > "))
            print(calc_1(NUM_1, COMMAND))
        else:
            print("Неизвестный оператор", COMMAND)
