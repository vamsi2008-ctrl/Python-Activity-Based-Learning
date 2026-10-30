usage=int(input())
rate=2
budget=int(input())
cost=usage*rate
print(cost)
if cost<=budget:
    print("within budget")
else:
    print("over budget")
