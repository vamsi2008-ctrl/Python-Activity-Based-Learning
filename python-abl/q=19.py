price=int(input())
quantity=int(input())
budget=int(input())
cost=price*quantity
print(cost)
if cost<=budget:
    print("within budget")
else:
    print("over budget")
