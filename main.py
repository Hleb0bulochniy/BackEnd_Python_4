'''
Файл содержит вызов конструкций для Лабораторной работы 4
'''
from exceptions import (
    divide, check_number_negativity, safe_divide, safe_check_number_negativity,
    divide_numbers, key_word_guess, access_dict, square_root, name_input,
    calculate_area, glue_strings, buy_goods
)

# п.9 Функция, которая последовательно вызывает ВСЕ вышесозданные функции.
# Функция ДОЛЖНА завершаться корректно и НЕ ДОЛЖНА иметь необработанных исключений
def def_check():
    '''Функция вызывает все функции из других пунктов и обрабатывает исключения'''
    #п.1
    try:
        divide(12,0)
    except ZeroDivisionError as e:
        print(f"Ошибка: {e}")
    try:
        check_number_negativity(-3)
    except ValueError as e:
        print(f"Ошибка: {e}")
    print("")

    #п.2
    safe_divide(12,0)
    print("")

    #п.3
    safe_check_number_negativity(-3)
    print("")

    #п.4
    divide_numbers(3,-1)
    key_word_guess("nezachet")
    test_dictionary = {
    "key1": "a",
    "key2": "b",
    "key3": "c"}
    access_dict(test_dictionary, "key4")
    print("")

    #п.5
    square_root(-25)
    print("")

    #п.6 не содержит функций

    #п.7
    name_input("Admin")
    print("")

    #п.8
    try:
        calculate_area(-3)
    except ValueError as e:
        print(f"Ошибка: {e}")
    finally:
        print("Завершение операции подсчета радиуса")
    try:
        glue_strings("24124",24213)
    except TypeError as e:
        print(f"Ошибка: {e}")
    finally:
        print("Завершение операции соединения строк")
    try:
        buy_goods(300,339)
    except ValueError as e:
        print(f"Ошибка: {e}")
    finally:
        print("Завершение операции вычета денег")



if __name__ == '__main__':
    def_check()
