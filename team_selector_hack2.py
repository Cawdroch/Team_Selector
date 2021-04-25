import random
# Create list of players
players = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
           "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
# Print welcome message
print("Welcome to Team - Player Allocator!")
# Randomise the player list
while True:
    random.shuffle(players)
# Find out if its a team sport or individual sport
    response = input("Is it a team game or individual sport?\n Type team or\
                     individual: ")
    if response == "team":
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
    else:
        for i in range(0, len(players), 2):
            print(players[i]+" vs "+players[i+1])
            start = random.randrange(i, i+2)
            print(players[start]+" starts\n")
    response = input("Pick teams again? Type y or n: ")
    if response == "n":
        break
