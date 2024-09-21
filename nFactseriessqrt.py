num=int(input("Enter the last number of series: "))
count=0
def factorial(num):
    fact=1
    while num!=0:
        fact=fact*num
        num=num-1
    return fact
for i in range(1,num+1):
    if i % 2 == 0:
        sign= " - "
    else:
        sign=' + '
    if i == 1:
        print(i, sign,end="")
        continue
    if i == num:
        print(f"{i*i}/{factorial(i)}",end="")
        continue
    print(f"{i*i}/{factorial(i)}{sign}",end="")
