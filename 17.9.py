while True:
    try:
        a = list(map(int, input('Введите числа через пробел: ').split(' ')))
    except Exception:
        print("Некорректный ввод!")
    else:
        break

while True:
    try:
        b = list(map(int, input(f'Введите число от {min(list(a))} до {max(list(a))}: ').split(',')))
        if min(list(b)) < min(list(a)) or min(list(b)) > max(list(a)):
            raise ValueError
    except ValueError:
        print(f"Нужно ввести число от {min(list(a))} до {max(list(a))}!")
    else:
        break

array, num = list(map(int, a)), list(map(int, b))
array.extend(num)

for i in range(len(array)):
    for j in range(len(array) - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]

print(array)

def binary_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)

element = min(b)
idx = binary_search(array, element, 0, len(array))

if element == max(array):
    Pidx = idx
elif element == min(array):
    Pidx = "- не определён"
else:
    Pidx = idx - 1

print(f"Последний индекс в списке: {len(array)-1}")
print(f"Предшествующий числу {element} индекс:", Pidx)