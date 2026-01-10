import random
import time


def bubbleSort(arr: list[int]) -> list[int]:
    # arr = [1, 2, 3, 4, 6]
    # index = 4, inner_i = 0, range_end = 0
    # Jumlah element
    # i.e length of element = 5
    length_of_element = len(arr)

    # range(start, end, [step])
    for index in range(0, length_of_element):
        for inner_index in range(0, length_of_element - index - 1):
            if arr[inner_index] > arr[inner_index + 1]:
                # Ini proses swapping (tukar) element
                arr[inner_index], arr[inner_index + 1] = (
                    arr[inner_index + 1],
                    arr[inner_index],
                )
    return arr


n = 100

data = []

for i in range(n):
    data.append(random.randint(1, 1000))

print(data)

now = time.time()
print(bubbleSort(data))
then = time.time()

total_time = then - now

print(f"Time taken: {total_time} second")