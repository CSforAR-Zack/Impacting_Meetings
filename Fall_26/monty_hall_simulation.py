# Monty Hall Problem: Single Game
import random


def main():
    """Simulate multiple Monty Hall games and count the number of wins."""

    number_of_games = 10000000

    wins = 0
    losses = 0

    for game in range(number_of_games):
        win = single_game("n")
        if win:
            wins += 1
        else:
            losses += 1

    print("Total wins:", wins, "(", wins / number_of_games * 100, "%)")
    print("Total losses:", losses, "(", losses / number_of_games * 100, "%)")


def single_game(player_switch):
    # Track the positions of the car and goats behind the doors
    spots = [0, 1, 2]
    random.shuffle(spots)

    car_door = spots[0]
    goat1_door = spots[1]
    goat2_door = spots[2]

    player_choice = random.choice([0, 1, 2])

    # Host opens a door with a goat
    possible_doors = [goat1_door, goat2_door]

    if player_choice in possible_doors:
        possible_doors.remove(player_choice)

    open_door = random.choice(possible_doors)

    # Ask the player if they want to switch doors
    if player_switch == "y":
        player_choice = math_approach(player_choice, open_door)

    if player_choice == car_door:
        return True
    else:
        return False


def math_approach(player_choice, open_door):
    """Return the door number that the player should switch to using the mathematical approach."""
    return 3 - player_choice - open_door


def if_else_approach(player_choice, open_door):
    """Return the door number that the player should switch to using the if/else approach."""
    if player_choice == 2:
        if open_door == 1:
            return 0
        else:
            return 1
    elif player_choice == 1:
        if open_door == 0:
            return 2
        else:
            return 0
    else:
        if open_door == 1:
            return 2
        else:
            return 1


def simplified_if_else_approach(player_choice, open_door):
    """Return the door number that the player should switch to using the simplified if/else approach."""
    if player_choice == 2 and open_door == 1:
        return 0
    elif player_choice == 2:
        return 1
    elif player_choice == 1 and open_door == 0:
        return 2
    elif player_choice == 1:
        return 0
    elif open_door == 1:
        return 2
    else:
        return 1


main()