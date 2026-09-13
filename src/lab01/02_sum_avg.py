a,b=float(input('a: ').replace(',','.')), float(input('b: ').replace(',','.'))
sum, avg = a+b, (a+b)/2
print(f'{sum=:.2f}; {avg=:.2f}')