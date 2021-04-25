import random
# Create list of players
players = ["Martin", "Craig", "Sue", "Claire",
           "Dave", "Alice", "Luciana", "Harry", "Jack",
           "Rose", "Lexi", "Maria", "Thomas", "James",
           "William", "Ada", "Grace", "Jean", "Marissa", "Alan",
           "Marigold", "Pete"]
# Print welcome message
print("Welcome to Team Allocator!")
# Randomise the player list
while True:
    random.shuffle(players)
# Split players list in half and assign that new list to variable team1
    team1 = players[:len(players)//2]
# Random select player from team1 to be captain
    print("Team 1 captain: "+random.choice(team1))
# Print the players in list team1 using a for loop to iterate
    print("Team 1:")
    for player in team1:
        print(player)
# Repeat for team 2
    team2 = players[len(players)//2:]
    print("\nTeam 2 captain: "+random.choice(team2))
    print("Team 2:")
    for player in team2:
        print(player)
    response = input("Pick teams again? Type y or n: ")
    if response == "n":
        break
