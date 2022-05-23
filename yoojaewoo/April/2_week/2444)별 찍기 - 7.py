# 문제
# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

# 출력
# 첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.

# 예제 입력 1
# 5

# 예제 출력 1
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

# 첫번째 시도
# num = int(input())
# for j in range(num):
#     print(" " * (num - j -1) + "*" * (2 * j + 1))
# for n in range(num):
#     print((" " * n) + ("*" * (2 * num - 2 * n - 1)))

# 두번째 시도
num = int(input())
for j in range(num):
    print(" " * (num - j - 1) + "*" * (2 * j + 1))
for n in range(num):
    print((" " * (n + 1)) + ("*" * (2 * num - 2 * n - 3)))
