i=1
N = int(input(f'in_{i}: '))
true=false=0
for n in range(N):
    i+=1
    person = input(f'in_{i}: ')
    type = person.split()[-1]
    if type == 'True':
        true += 1
    else:
        false += 1
print('out:', true, false)