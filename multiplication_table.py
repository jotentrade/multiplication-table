#!/usr/bin/env python3

print("9 x 9 乘法表\n")

for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} x {j} = {i*j:2d}", end="\t")
    print()  # 換行

# 也可以印成表格形式
print("\n\n漂亮的表格格式:")
print("   ", end="")
for i in range(1, 10):
    print(f"{i:3d}", end="")
print()
print("  " + "---"*9)

for i in range(1, 10):
    print(f"{i} |", end="")
    for j in range(1, 10):
        print(f"{i*j:3d}", end="")
    print()