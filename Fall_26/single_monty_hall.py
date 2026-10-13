# Monty Hall Problem: Single Game
import random


def main():
    # Graphics
    goat: str = "\U0001F410"
    car: str = "\U0001F697"
    door: str = "\U0001F6AA"

    doors = [door, door, door]

    # Track the positions of the car and goats behind the doors
    spots = [0, 1, 2]
    random.shuffle(spots)

    car_door = spots[0]
    goat1_door = spots[1]
    goat2_door = spots[2]

    print(doors)

    player_choice = int(input("Choose a door (0, 1, 2): "))
    print("Player chose door:", player_choice)

    # Host opens a door with a goat
    possible_doors = [goat1_door, goat2_door]

    if player_choice in possible_doors:
        possible_doors.remove(player_choice)

    open_door = random.choice(possible_doors)
    doors[open_door] = goat
    print("Host opens door:", open_door, doors)

    # Ask the player if they want to switch doors
    player_switch = input("Do you want to switch doors? (y/n): ")
    if player_switch == "y":
        # Solution 1: Mathematical approach
        player_choice = math_approach(player_choice, open_door)
        
        # Solution 2: If/else approach
        # SLO 2: Use if/else statements to make decisions in a program based on specific conditions.
        player_choice = if_else_approach(player_choice, open_door)

        # Solution 3: Simplified if/else approach
        player_choice = simplified_if_else_approach(player_choice, open_door)

    # Reveal the result
    doors[car_door] = car
    doors[goat1_door] = goat
    doors[goat2_door] = goat

    if player_choice == car_door:
        print("Player wins! Car is behind door:", player_choice)
    else:
        print("Player loses. Car was behind door:", car_door)

    print(doors)


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