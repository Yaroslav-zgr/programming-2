# Определение функции solve, которая принимает список чисел, целевое значение и текущий путь
def solve(nums, target, path=''):
    # Если список чисел пуст, мы достигли конца списка
    if not nums:
        # Если целевое значение равно нулю, это означает, что мы нашли решение
        if target == 0:
            return path  # Возвращаем текущий путь как решение
        else:
            return None  # Если целевое значение не равно нулю, это означает, что мы не нашли решение
    else:
        # Мы вызываем функцию solve рекурсивно, удаляя первое число из списка и вычитая его из целевого значения
        plus = solve(nums[1:], target - nums[0], path + '+' + str(nums[0]))
        # Если рекурсивный вызов вернул не None, это означает, что мы нашли решение
        if plus is not None:
            return plus  # Возвращаем найденное решение
        # Мы делаем еще один рекурсивный вызов функции solve, но на этот раз добавляем первое число к целевому значению
        minus = solve(nums[1:], target + nums[0], path + '-' + str(nums[0]))
        # Если этот рекурсивный вызов вернул не None, это означает, что мы нашли решение
        if minus is not None:
            return minus  # Возвращаем найденное решение
        return None  # Если ни один из рекурсивных вызовов не вернул решение, возвращаем None

# Определение основной функции, которая будет запускать наш код
def main():
    # Открываем файл input.txt для чтения
    with open('input.txt', 'r') as f:
        # Считываем все данные из файла, разделяем их по пробелам и преобразуем в целые числа
        data = list(map(int, f.read().split()))
    # Извлекаем количество чисел, сами числа и целевое значение из данных
    N, nums, S = data[0], data[1:-1], data[-1]
    # Вызываем функцию solve с числами и целевым значением, чтобы найти решение
    result = solve(nums, S)
    # Открываем файл output.txt для записи
    with open('output.txt', 'w') as f:
        # Если результат равен None, это означает, что решение не найдено
        if result is None:
            f.write('no solution')  # Записываем в файл строку 'no solution'
        else:
            # Если результат не равен None, это означает, что мы нашли решение
            f.write(result[1:] + '=' + str(S))  # Записываем решение в файл

# Это условие проверяет, является ли этот файл основным файлом, который был запущен, а не модулем, который был импортирован
if __name__ == "__main__":
    main()  # Вызываем функцию main, чтобы запустить наш код