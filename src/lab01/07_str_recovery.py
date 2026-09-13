string = input()
for i in range(len(string)):
    if string[i].isupper():
        start=i
        break
for i in range(start+1, len(string)):
    if string[i].isdigit():
        second=i+1
        break
step = second - start
res = ''
for i in range(start, len(string), step):
    res += string[i]
    if string[i] == '.':
        break
print(res)