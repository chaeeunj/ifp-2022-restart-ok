#12926_시저 암호
import string
def solution(s, n):
    answer = ''
    lo, up= list(string.ascii_lowercase), list(string.ascii_uppercase)

    for i, c in enumerate(s):
        if c == ' ':
            answer += ' '
        elif c.isupper():
            answer += (up[(up.index(c) + n)%26])
        else:
            answer += (lo[(lo.index(c) + n)%26])
    return answer