import random
import math

"""TASK 1"""


def initialization(first_turn):
    return {
        'rounds_played': 0,
        'rounds_winner': [],
        'current_player': first_turn
    }


def alpha_beta_pruning(depth, alpha, beta, player_turn):
    if depth == 0:
        return random.choice([-1, 1])

    if player_turn:  # Sub-Zero's turn
        max_v = -math.inf
        for i in range(2):
            v = alpha_beta_pruning(depth - 1, alpha, beta, False)
            max_v = max(max_v, v)
            alpha = max(alpha, v)
            if alpha >= beta:
                break
        return max_v

    else:  # Scorpion's turn
        min_v = math.inf
        for i in range(2):
            v = alpha_beta_pruning(depth - 1, alpha, beta, True)
            min_v = min(min_v, v)
            beta = min(beta, v)
            if alpha >= beta:
                break
        return min_v


def play_round(game_state):
    player_turn = (game_state['current_player'] == 1)
    result = alpha_beta_pruning(5, -math.inf, math.inf, player_turn)
    winner = "Scorpion" if result == -1 else "Sub-Zero"
    game_state['rounds_winner'].append(winner)
    game_state['rounds_played'] += 1
    game_state['current_player'] = 1 - game_state['current_player']


def mortal_kombat(first_turn):
    game_state = initialization(first_turn)
    while game_state['rounds_played'] < 3:
        play_round(game_state)
    return game_state['rounds_winner']


def display_results(rounds_winner):
    game_winner = "Scorpion" if rounds_winner.count("Scorpion") >= 2 else "Sub-Zero"
    print(f"Game Winner: {game_winner}")
    print(f"Total Rounds Played: {len(rounds_winner)}")
    for winner in enumerate(rounds_winner):
        print(f"Winner of Round {winner[0] + 1}: {winner[1]}")


def player_choice():
    return int(input())


first_turn = player_choice()
rounds_winner = mortal_kombat(first_turn)
display_results(rounds_winner)

"""TASK 2"""


def pacman_game(c):
    def minimax(depth, idx, maximizingPlayer, arr, alpha, beta):
        if depth == 3:
            return arr[idx]
        if maximizingPlayer:
            max_v = -math.inf
            for i in range(2):
                v = minimax(depth + 1, idx * 2 + i, False, arr, alpha, beta)
                max_v = max(max_v, v)
                alpha = max(alpha, max_v)
                if alpha >= beta:
                    break
            return max_v
        else:
            min_v = math.inf
            for i in range(2):
                v = minimax(depth + 1, idx * 2 + i, True, arr, alpha, beta)
                min_v = min(min_v, v)
                beta = min(beta, min_v)
                if alpha >= beta:
                    break
            return min_v
    if (max(leaf_nodes) - c) > final:
        maxi = max(leaf_nodes)
        if leaf_nodes.index(maxi)+1 > len(leaf_nodes)/2:
            print(f"The new minimax value is {max(leaf_nodes) - c}. Pacman goes right and uses dark magic")
        else:
            print(f"The new minimax value is {max(leaf_nodes) - c}. Pacman goes left and uses dark magic")
    else:
        print(f"The minimax value is {final}. Pacman does not use dark magic")


c = int(input())
pacman_game(c)
