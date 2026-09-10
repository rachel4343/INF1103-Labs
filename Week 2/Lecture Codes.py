# Control Flow Structures
# 1. Sequential Control Flow
# 2. Selection (Conditional) Control Flow
# 3. Iteration (Looping) Control Flow




# 1. Sequential Control Flow
first = 15
second = 50
print(first,second)
first,second = second, first
print(first,second)




# 2. Selection (Conditional) Control Flow
# if statement
food = "Burger"
price = 0.0
if food == "Burger":
    print("You chose Burger")
    print("Please pay 8.00 SGD")
    price = 8.0

# elif statement
food = "Sandwich"
price = 0.0
if food == "Fries":
    print("You chose Fries")
    print("Please pay 4.00 SGD")
    price = 4.0
elif food == "Burger":
    print("You chose Burger")
    print("Please pay 8.00 SGD")
    price = 8.0
else:
    print("Sorry your choice is not available")




# 3. Iteration (Looping) Control Flow
# while loop
walk_circle = 0
while walk_circle < 10:
    walk_circle = walk_circle + 1
print("Walking complete")
print(walk_circle)
# the while loop will always execute as long as the stated condition is true
# thus walk_circle is 10

# for loop
walk_circle = 0
for walk_circle in range(10):
    print(walk_circle)
print("Walking complete")
print(walk_circle)

# break statements; Stop the loop when some condition is satisfied
walk_circle = 0
for walk_circle in range(1,10):
    print(walk_circle)
    if walk_circle == 5:
        break
print("Walking complete")
print(walk_circle)

# continue statements; Skip the rest of the current loop body and move to the next iteration
walk_circle = 0
for walk_circle in range(1,10):
    if walk_circle == 5:
        continue
    print(walk_circle)
print("Walking complete")
print(walk_circle)




# Task for the day
# Traffic Light Simulator
# • Rules:
# • If the light is Green → Print "Go“
# • If the light is Yellow → Print "Slow Down“
# • If the light is Red → Print "Stop“
# • The simulation should run for 10 seconds.

for seconds in range(1,11):
    if seconds <= 4:
        light = "Green"
    elif seconds <= 7:
        light = "Yellow"
    else:
        light = "Red"

    if light == "Green":
        print(seconds, "seconds - Go")
    elif light == "Yellow":
        print(seconds, "seconds - Slow Down")
    else:
        print(seconds, "seconds - Stop")

