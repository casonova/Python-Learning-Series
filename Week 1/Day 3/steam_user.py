class SteamUser:
    
    def __init__(self, username, games):
        self.username = username
        self.games = games
        self.played_hours = 0
        
    def play(self, game, hours):
        if game in self.games:
            self.played_hours += hours
            return f"{self.username} is playing {game}"
        return f"{game} is not in library"
    
    def buy_game(self, game):
        if game not in self.games:    
            self.games.append(game)
            return f"{self.username} bought {game}"
        return f"{game} is already in your library"
    
    def status(self):
        return f"{self.username} has {len(self.games)} games. Total play time: {self.played_hours}"
    
# Creating a Steam user
user1 = SteamUser("Player1", ["Game1", "Game2"])

# Test case 1: Playing a game that exists in the library
print(user1.play("Game1", 5))  # Output: Player1 is playing Game1

# Test case 2: Playing a game that doesn't exist in the library
print(user1.play("Game3", 3))  # Output: Game3 is not in library

# Test case 3: Buying a game that is not in the library
print(user1.buy_game("Game3"))  # Output: Player1 bought Game3

# Test case 4: Buying a game that is already in the library
print(user1.buy_game("Game2"))  # Output: Game2 is already in your library

# Test case 5: Checking user's status
print(user1.status())  # Output: Player1 has 3 games. Total play time: 5
    