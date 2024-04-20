def main(input_string) -> str:
    try:

        if len(input_string.split()) != 3:
            raise Exception("throws Exception //т.к. строка не является математической операцией")
        a, operator, b = input_string.split()


        if not (1 <= a <= 10) or not (1 <= b <= 10):
            raise ValueError("Числа должны быть от 1 до 10")


        if operator == '+':
            result = a + b
        elif operator == '-':
            result = a - b
        elif operator == '*':
            result = a * b
        elif operator == '/':
            result = a // b
        else:
            raise ValueError("throws Exception //т.к Неподдерживаемая операция")

        return str(result)

    except (IndexError, ValueError) as e:
        raise Exception("Ошибка: " + str(e))


if __name__ == '__main__':
    while True:
        try:
            print(main(input("Введите математическую операцию(2 Числа и 1 оператор): ")))
        except Exception as e:
            print(e)