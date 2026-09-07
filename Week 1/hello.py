# Activity 1 : Create your First Python Program and add it to the repository
print("=============================")
print("Welcome here")
print("My first post!")
print("=============================")

# git add git add "Week 2/hello.py"; Prepares your changes to be committed.
# git status; You should see your Python file as modified. Checks the current state of your repository.
# git commit -m "First Post"; "Save this version"
# git log; Shows your commit history.
# q; quit



# Activity 2: Update your Profile and add it to the repository 
username = "cool_creator"
bio = "Fun Blogger"
followers = 100

print("Username:", username)
print("Bio:", bio)
print("Followers:", followers)

# git diff; Checks the difference in the repository files
# git add hello.py; Prepares your changes to be committed.
# git status; You should see your Python file as modified. Checks the current state of your repository.
# git commit -m "Added Profile Variables"; "Save this version"
# git log; Shows your commit history.
# q; quit



# Activity 3: Follower Growth tracker 
followers += 50  # Increment followers by 50
print("Day 1:", followers)

followers += 20  # Increment followers by 20
print("Day 2:", followers)

followers -= 10 # Decrement followers by 10
print("Day 3:", followers)

# git status; You should see your Python file as modified. Checks the current state of your repository.
# git add hello.py; Prepares your changes to be committed.
# git commit -m "Assignment Variables; "Save this version"
# git log; Shows your commit history.
# q; quit



# Activity 4: Interactive profile creator 
username = input("Enter your username: ")
age = int(input("Enter your age: "))
category = input("Enter Content Category: ")

print("\nInstagram Profile Created!")
print("=============================")
print("Username:", username)
print("Age:", age)
print("Content Category:", category)

# git status; You should see your Python file as modified. Checks the current state of your repository.
# git add hello.py; Prepares your changes to be committed.
# git commit -m "Dynamic profile"; "Save this version"
# git log; Shows your commit history.
# q; quit



# Activity 5: Something fun to think about.
# input() always returns a string (str).
# 2 conditions being checked.
username = input("Enter your username: ")
age = int(input("Enter your age: "))
category = input("Enter Content Category: ")

print("\nInstagram Profile Created!")
print("=============================")
print("Username:", username)
print("Age:", age)
print("Content Category:", category)

if age>40 and category == "fun":
    print("You are old what is fun for you??")
# elif age<40 and category == "fun":
#     print("You are young, have fun!")

# git status; You should see your Python file as modified. Checks the current state of your repository.
# git add hello.py; Prepares your changes to be committed.
# git commit -m "Fun Conditions"
# git log; Shows your commit history.
# q; quit