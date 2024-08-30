"""
Для решения данной задачи применим метод префиксных сумм.
Основная идея заключается в следующем: если некоторая подпоследовательность не делится на 89
без остатка, нужно найти префикс этой последовательности, имеющий такой же остаток, что и наша
подпоследовательность. Исключив этот префикс из последовательности, мы получим новую
подпоследовательность, которая будет кратна 89.
"""

# открываем файл и читаем данные
with open('27_B.txt') as f:
    n = int(f.readline())
    data = list(map(int, f.readlines()))

# список для хранения минимальных префиксных сумм
prefix_sums = [float("inf")] * 89
# список для хранения длины префиксных сумм
prefix_lens = [0] * 89

# Сумма текущей последовательности
s = 0
# Максимальная найденная сумма подпоследовательности, кратная 89
max_s = 0
# Минимальная длина подпоследовательности при найденной максимальной сумме
min_len = float('inf')

# Проходим по всем элементам последовательности
for i, num in enumerate(data, start=1):
    s += num
    # Если текущая сумма кратна 89
    if s % 89 == 0:
        max_s = s
        min_len = i
    # Если текущая сумма не кратна 89
    else:
        prefix = prefix_sums[s % 89]  # Находим префиксную сумму с таким же остатком
        len_prefix = prefix_lens[s % 89]
        if s - prefix > max_s:
            max_s = s - prefix
            min_len = i - len_prefix
        elif s - prefix == max_s:
            min_len = min(min_len, i - len_prefix)
    # Обновляем минимальную префиксную сумму и ее длину
    if s < prefix_sums[s % 89]:
        prefix_sums[s % 89] = s
        prefix_lens[s % 89] = i

print(min_len)