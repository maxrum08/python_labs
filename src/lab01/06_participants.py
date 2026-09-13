N = int(input())
true=false=0
for n in range(N):
    person = input()
    type = person.split()[-1]
    if type == 'True':
        true += 1
    else:
        false += 1
print(true, false)