# 대소문자 바꾸기

''' 문제
영어 소문자와 대문자로 이루어진 단어를 입력받은 뒤, 대문자는 소문자로, 소문자는 대문자로 바꾸어 출력하는 프로그램을 작성하시오.
'''

''' 입력
첫째 줄에 영어 소문자와 대문자로만 이루어진 단어가 주어진다. 단어의 길이는 최대 100이다.
'''

''' 출력
첫째 줄에 입력으로 주어진 단어에서 대문자는 소문자로, 소문자는 대문자로 바꾼 단어를 출력한다.
'''

# 풀이
a = input()

# 1. lower(), upper() 사용
for aa in a:
    print(aa.lower() if aa.isupper() else aa.upper(), end='')

# 2. 아스키 코드 사용
for aa in a:
    if ord(aa) > 96:
        print(chr(ord(aa) - 32), end='')
    else:
        print(chr(ord(aa) + 32), end='')

# 3. swapcase() 사용
print(input().swapcase())
