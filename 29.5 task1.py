import random


# Функция bubble_sort принимает список целых чисел
# data и сортирует его в порядке убывания элементов с
# помощью пузырьковой сортировки. Кроме того, функция
# должна посчитать количество операций (итераций цикла),
# которые выполняет алгоритм, и вернуть это число вызывающей
# стороне.



def bubble_sort(array:list):
    counter = 0

    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] < array[j]:
                array[i], array[j] = array[j], array[i]
            counter += 1
    return counter


def test_sorted():
    data = [random.randint(0, 1000) for i in range(100)]
    data_to_sort = data.copy()
    bubble_sort(data_to_sort)
    if data_to_sort == sorted(data, reverse=True):
        print('OK')
    else:
        print('NOT OK')


def make_observations():
    size = 10
    results = []
    for i in range(100):
        data = [random.randint(0, 1000) for i in range(size)]
        results.append((size, bubble_sort(data)))
        size += 10
    return results


def main():
    test_sorted()
    with open('bubble.csv', 'w') as file:
        file.write(f'iterations,size\n')
        for row in make_observations():
            file.write(f' {row[1]} ,{row[0]}\n')
    print('Done!')

if __name__ == '__main__':
    main()