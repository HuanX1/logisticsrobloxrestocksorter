import sys
p = {}
numbers = [str(x) for x in sys.stdin.read().split()]
for n in range(1,len(numbers),2): #assuming one line has [NAME] [RESTOCK AMOUNT]
    p.update({numbers[n-1] : int(numbers[n])})
sort_orders = sorted(p.items(), key=lambda x: x[1], reverse=True)
for i in sort_orders:
    print(i[0], i[1])
