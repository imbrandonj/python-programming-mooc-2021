# Part 5 Exercise 3
# Go

def who_won(game_board: list):
    """ Based off the game, 'Go'
        Reads game_board list and determines the winner
        0 value is an empty square
        1 value is player 1 game piece
        2 value is player 2 game piece
        If player 1 wins, return 1
        If player 2 wins, return 2
        If a tie, return 0 """

    player_one = 0
    player_two = 0

    for row in game_board:
        for i in row:
            if i == 1:
                player_one += 1
            elif i == 2:
                player_two += 1
            elif i == 0:
                continue
    
    if player_one > player_two:
        return 1
    elif player_one < player_two:
        return 2
    elif player_one == player_two:
        return 0