class Game:
    def __init__(self, message):
        # Players' score
        self.score1 = 0
        self.score2 = 0
        # Round count
        self.round = 0
        # Print out welcome message
        print(f"{message}")

    def score(self, player):
        match player:
            case "player1":
                self.round += 1
                self.score1 = self.score1 + 1
                print(f"player1 score: {self.score1}")
            case "player2":
                self.round += 1
                self.score2 = self.score2 + 1
                print(f"player1 score: {self.score2}")
            case _:
                print("Invalid player!")

    def is_game_over(self) -> bool:
        # 2nd round and a player has 2 points
        if self.round == 2 and abs(self.score1 - self.score2):
            return True
        elif self.round >= 3:
            return True
        else:
            return False


welcome_message = "Hello, let's play!"
game = Game(welcome_message)

#Init

def init():
    pass
