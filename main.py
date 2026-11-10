arr = list(map(int, input("Введіть числа через пробіл: ").split()))

current_sum = arr[0]
max_sum = arr[0]

start = 0
end = 0
temp_start = 0

for i in range(1, len(arr)):
    if arr[i] > current_sum + arr[i]:
        current_sum = arr[i]
        temp_start = i
    else:
        current_sum += arr[i]

    if current_sum > max_sum:
        max_sum = current_sum
        start = temp_start
        end = i

subarray = arr[start:end + 1]

print(f"Максимальна сума підмасиву {subarray}: {max_sum}")