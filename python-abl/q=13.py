balance=int(input())
deposit=int(input())
balance=balance+deposit
withdrow=int(input())
if withdrow<=balance:
    print(balance-withdrow)
else:
    print("insufficient balance")
print(balance)    
