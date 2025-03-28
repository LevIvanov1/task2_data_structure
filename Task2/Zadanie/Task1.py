def is_number(s):
    if not s:
        return False

    has_decimal = False
    digit_has = False
    for i, char in enumerate(s):
        if char.isdigit():
            digit_has = True
        elif char == '.' and not has_decimal and digit_has:
            has_decimal = True
        elif char == '-' and i == 0:
            continue
        else:
            return False
    return digit_has

def main():
    num_input = input("Число с пробелом: ")
    numbers = num_input.split()
    stepen = int(input("Введите степень: "))
    result = []
    for num in numbers:
        if is_number(num):
            num_float = float(num)
            result.append(str(num_float ** stepen))
        else:
            result.append(num * stepen)

    print("Ответ:", ' '.join(result)) # можно ввести как по заданию, ответ будет выводить с типом плавающей точкой
main()

