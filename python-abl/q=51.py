capacity=int(input())
board=int(input())
passengers=capacity-board
print(passengers)
if passengers<=capacity:
    print("within capacity")
else:
    print("over loaded")
