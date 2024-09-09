import random # Used to generate random numbers in python

# List in python
# Used to store multiple values in a single variable
food = ["pizza", "pasta", "burger", "chips"]
dinner = random.choice(food)


# Dictionary in python
# Used to store key value pairs
dict = {'name': "Anup", 'color': "red", 'food': dinner}


# If Operator and Comparision in python
age = 15
if age > 19:  # ==, !=, <=, >=, <, >
    print("You are an adult")
elif age >12:
    print("You are an Teen")
elif age >1:
    print("You are a child")
else:
    print("You are a baby")


# String in python
fname="Anup"
lname="Alone"
print("Concantination:-- " "Hello my name is " + fname + " " + lname)

print(f"FString:--  Hello my name is {fname} {lname}")

print(f"""Multiple Line of String :--
Adding Multiple Line for FString
Hello my name is {fname} {lname}
""")

# Type of Operataor
print("CHECKING DATATYPE IN PYTHON")
name = "Anup"
print(type(name))
print(type(name) == str)

# Check for Instance
print("CHECKING INSTNACE IN PYTHON")
print(isinstance(name, str))

# Transforming One Data Type to Another
age = int("20")
num = float(2)

# Function in python
# Indentation is very important in python
def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ") # Taking Input from the user
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options) # Define a variable in python
    # print(player_choice, computer_choice)
    choices = {'player': player_choice, 'computer': computer_choice, }
    return choices

def check_win(player, computer):
    player = player.lower()
    computer = computer.lower()
    print(f"You choose '{player}', computer choose '{computer}'")

    if(player == computer):
        return print("Its a Tie")
    elif(player == "rock"):
        if(computer == "scissors"):
            return print("Player Won")
        else:
            return print("Computer Won")
    elif(player == "paper"):
        if(computer == "rock"):
            return print("Player Won")
        else: 
            return print("Computer Won")
    else:
        if(computer == "paper"):
            return print("Player Won")
        else:
            return print("Computer Won")


choices = get_choices()
checkWin = check_win(choices['player'], choices['computer'])







