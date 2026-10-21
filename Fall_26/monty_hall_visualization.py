# Monty Hall Problem: Multiple Games Simulation
import random

import matplotlib.pyplot as plt


def main():
    """Simulate multiple Monty Hall games and count the number of wins."""

    number_of_games: int = 1000000
    choice: str = "n"

    wins: int = 0
    losses: int = 0

    for game in range(number_of_games):
        win = single_game(choice)
        if win:
            wins += 1
        else:
            losses += 1

    print("Total wins:", wins, f"({wins / number_of_games * 100}%)")
    print("Total losses:", losses, f"({losses / number_of_games * 100}%)")

    graph_results(wins, losses)
    # graph_using_turtles(wins, losses)


def single_game(player_switch):
    # Track the positions of the car and goats behind the doors
    spots: list[int] = [0, 1, 2]
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
        player_choice = if_else_approach(player_choice, open_door)

    if player_choice == car_door:
        return True
    else:
        return False


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


def graph_results(wins, losses):
    """Generate a bar chart of the Monty Hall simulation results."""
    plt.bar(["Wins", "Losses"], [wins, losses])
    plt.xlabel("Outcome")
    plt.ylabel("Count")
    plt.title("Monty Hall Simulation Results")
    plt.show()


def graph_using_turtles(wins, losses):
    """Generate a bar chart of the Monty Hall simulation results."""
    import turtle
    
    screen = turtle.Screen()
    screen.title("Monty Hall Simulation Results")

    t = turtle.Turtle()
    t.speed(0)

    data = [("Wins", wins), ("Losses", losses)]
    max_count = max(wins, losses)
    
    # --- Draw X and Y Axes ---
    t.penup()
    t.goto(-100, 0)      # Move to origin
    t.pendown()
    t.goto(200, 0)       # Draw X-axis to the right
    
    t.penup()
    t.goto(-100, 0)      # Go back to origin
    t.pendown()
    t.goto(-100, 220)    # Draw Y-axis upwards
    # -------------------------

    # Starting X coordinate for the first bar
    x_pos = -50 

    for label, count in data:
        height = (count / max_count) * 200
        
        # Move to bar starting point
        t.penup()
        t.goto(x_pos, 0)
        t.pendown()

        # Draw the rectangular bar
        t.begin_fill()
        for _ in range(2):
            t.forward(50)
            t.left(90)
            t.forward(height)
            t.left(90)
        t.end_fill()

        # Add the label centered under the bar
        t.penup()
        t.goto(x_pos + 25, -20) 
        t.write(label, align="center")
        
        # Shift the X coordinate over for the next bar
        x_pos += 100

    t.hideturtle()
    turtle.done()

main()