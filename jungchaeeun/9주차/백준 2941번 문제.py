croa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croa:
    word = word.replace(i, '*')

print(len(word))
