# 1.Хакер Василий получил доступ к классному журналу и хочет заменить
# все свои минимальные оценки на максимальные. Напишите программу,
#  которая заменяет оценки Василия, но наоборот: все максимальные –
# на минимальные.
# Input: 5 -> 1 3 3 3 4

# Output: 1 3 3 3 1


n = int(input())
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)

print(arr)

a = max(arr)
for i in range(len(arr)):
    if arr[i] == a:
        arr[i] = min(arr)
    
print(arr)
