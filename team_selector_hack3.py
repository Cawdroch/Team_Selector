import random
# Create list of players
players = []
# Print welcome message
print("Welcome to Team - Player Allocator!")
number_of_players = input("How many players are there? ")

for i in range(1, int(number_of_players)+1):
    players.append(i)
# Randomise the player list
while True:
    random.shuffle(players)
# Find out if its a team sport or individual sport
    response = input("Is it a team game or individual sport?\n Type team\
                     or individual: ")
    if response == "team":
        # Split players list in half and assign that new list to variable team1
        team1 = players[:len(players)//2]
        # Random select player from team1 to be captain
        print("Team 1 captain: "+str(random.choice(team1)))
        # Print the players in list team1 using a for loop to iterate
        print("Team 1:")
        for player in team1:
            print(player)
        # Repeat for team 2
        team2 = players[len(players)//2:]
        print("\nTeam 2 captain: "+str(random.choice(team2)))
        print("Team 2:")
        for player in team2:
            print(player)
    else:
        for i in range(0, len(players), 2):
            print(str(players[i])+" vs "+str(players[i+1]))
            start = random.randrange(i, i+2)
            print(str(players[start])+" starts\n")
    response = input("Pick teams again? Type y or n: ")
    if response == "n":
        break
