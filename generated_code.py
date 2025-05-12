```
import random
import logging

class Board:
    def __init__(self, size):
        self.size = size
        self.board = [[0 for _ in range(size)] for _ in range(size)]

    def print_board(self):
        for row in self.board:
            print(" ".join(str(cell) for cell in row))

class Agent:
    def __init__(self, name, strategy):
        self.name = name
        self.strategy = strategy
        self.score = 0

    def make_move(self, board):
        if self.strategy == "random":
            return random.randint(0, board.size - 1)
        elif self.strategy == "minimax":
            # implement minimax algorithm
            pass
        else:
            raise ValueError("Invalid strategy")

class Game:
    def __init__(self, board_size, agent1, agent2):
        self.board = Board(board_size)
        self.agent1 = agent1
        self.agent2 = agent2
        self.current_turn = 1

    def start_game(self):
        while True:
            self.board.print_board()
            move = self.agent1.make_move(self.board)
            self.board.board[self.current_turn - 1][move] = 1
            self.current_turn = 2 if self.current_turn == 1 else 1
            if self.check_win():
                self.board.print_board()
                print(f"{self.agent1.name} wins!")
                break

    def check_win(self):
        for i in range(self.board.size):
            if self.board.board[0][i] == 1 and self.board.board[1][i] == 1:
                return True
        return False

if __name__ == "__main__":
    agent1 = Agent("Agent 1", "random")
    agent2 = Agent("Agent 2", "random")
    game = Game(3, agent1, agent2)
    game.start_game()
```