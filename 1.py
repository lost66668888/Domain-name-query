good_numbers = set()

# 1. 顺子（递增/递减）
for i in range(0, 5):
    good_numbers.add(''.join(str(x) for x in range(i, i+6)))  # 012345, 123456, ...
for i in range(9, 4, -1):
    good_numbers.add(''.join(str(x) for x in range(i, i-6, -1)))  # 987654, 876543, ...

# 2. 豹子（三连）
for d in range(10):
    good_numbers.add(str(d)*6)  # 111111, 222222, ...

# 3. 重复型
for a in range(10):
    for b in range(10):
        if a != b:
            good_numbers.add(f"{a}{a}{b}{b}{a}{a}")  # 112211, 334433, ...
            good_numbers.add(f"{a}{b}{a}{b}{a}{b}")  # 121212, 232323, ...
            good_numbers.add(f"{a}{a}{a}{b}{b}{b}")  # 111222, 333444, ...
            good_numbers.add(f"{a}{b}{b}{a}{a}{b}")  # 122113, 344331, ...

# 4. 镜像型/对称型
for a in range(10):
    for b in range(10):
        for c in range(10):
            good_numbers.add(f"{a}{b}{c}{c}{b}{a}")  # 120021, 450054, 123321, ...

# 5. 年份型（如202023、199991、200002等）
for year in range(1950, 2031):
    y = str(year)
    good_numbers.add(y + y[-2:])  # 202023, 199991, 200002
    good_numbers.add(y[-2:] + y)  # 232023, 991990, 002000

# 6. 其它常见好记型
for a in range(10):
    for b in range(10):
        if a != b:
            good_numbers.add(f"{a}{a}{b}{b}{b}{a}")  # 112221, 334441, ...

# 只保留6位
good_numbers = {num for num in good_numbers if len(num) == 6}

# 写入文件
with open('6位好记.txt', 'w', encoding='utf-8') as f:
    for num in sorted(good_numbers):
        f.write(num + '\n')

print(f"共生成 {len(good_numbers)} 个6位好记号码，已写入 6位好记.txt")