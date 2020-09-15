#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random
moves = ['rock', 'paper', 'scissors']
modes = ['sd', 'fn']
players = ['default', 'human', 'random', 'reflect', 'cycle']	  #Seif's Over

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return(random.choice(moves))


class HumanPlayer(Player):
    def move(self):
        move = ''
        while move not in moves:
            move = input("Rock, paper or scissors? > ").lower()
            if move == 'quit':
                print("Bye!")
                raise SystemExit()
        return move


class ReflectPlayer(Player):
    def __init__(self):
        self.oppmove = ''

    def move(self):
        if len(self.oppmove) == 0:
            return(random.choice(moves))
        else:
            return self.oppmove

    def learn(self, my_move, their_move):
        self.oppmove = their_move
        return self.oppmove


class CyclePlayer(Player):
    def __init__(self):
        self.mymove = ''

    def move(self):
        if len(self.mymove) == 0:
            return(random.choice(moves))
        else:
            return self.mymove

    def learn(self, my_move, their_move):
        n = moves.index(my_move)
        if len(moves) - n == 1:
            self.mymove = moves[0]
        else:
            self.mymove = moves[n+1]


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score = [0, 0]

    def keep_score(self, one, two):
        if beats(one, two):
            self.score[0] += 1
            print("** PLAYER ONE WINS **")
        elif beats(two, one):
            self.score[1] += 1
            print("** PLAYER TWO WINS **")
        else:
            print("** TIE **")
        return self.score

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.keep_score(move1, move2)
        print(f"Score: Player One {self.score[0]}, " +
              f"Player Two {self.score[1]}\n")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    ''' Plays the game accoording to the chosen mode:
    whether winning by certain score difference
    or playing fixed number of rounds'''
    def win_mode(self, choice):          #Seif's Over
        if choice == 'sd':
            diff = ''
            while True:
                diff = input("Enter score difference (Min 3): ")
                if diff.isdigit():
                    diff = int(diff)
                    if diff > 2:
                        break
                elif diff == 'quit':
                    print("Bye!")
                    raise SystemExit()
            r = 1
            print("Game start!\n")
            while True:
                print(f"Round {r}:")
                self.play_round()
                r += 1
                if((self.score[0] - self.score[1] == diff) or
                   (self.score[1] - self.score[0] == diff)):
                    break
        elif choice == 'fn':
            rounds = ''
            while True:
                rounds = input("Enter number of rounds (Min 3): ")
                if rounds.isdigit():
                    rounds = int(rounds)
                    if rounds > 2:
                        break
                elif rounds == 'quit':
                    print("Bye!")
                    raise SystemExit()
            rounds = int(rounds)
            print("Game start!\n")
            for round in range(rounds):
                print(f"Round {round+1}:")
                self.play_round()

    def play_game(self):
        mode = ''
        print("Choose mode:\nWin by score difference(sd) OR "
              + "After fixed number of rounds(fn)")           #Seif's Over
        while mode not in modes:
            mode = input("Type 'sd' OR 'fn' >> ").lower()
            if mode == 'quit':
                print("Bye!")
                raise SystemExit()
        self.win_mode(mode)
        if self.score[0] > self.score[1]:
            print("\n\nWinner Winner Chicken Dinner... PLAYER ONE")
        elif self.score[1] > self.score[0]:
            print("\n\nWinner Winner Chicken Dinner... PLAYER TWO")
        else:
            print("\n\nGreat game, but TIES happen. Meh!")
        self.score = [0, 0]
        print("**********\nGame over!\n**********\n")


if __name__ == '__main__':
    opponent = ''
    # Prompts user to choose opponent strategy
    while opponent not in players:			 #Seif's Over
        opponent = input(f"Choose your opponent from {players}:\n").lower()
        if opponent == 'quit':
            print("Bye!")
            raise SystemExit()
    if opponent == players[0]:
        game = Game(HumanPlayer(), Player())
    elif opponent == players[1]:
        game = Game(HumanPlayer(), HumanPlayer())
    elif opponent == players[2]:
        game = Game(HumanPlayer(), RandomPlayer())
    elif opponent == players[3]:
        game = Game(HumanPlayer(), ReflectPlayer())
    elif opponent == players[4]:
        game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()


# game = rps_code.Game(rps_code.__Player(), rps_code.__Player())
# game.play_game()