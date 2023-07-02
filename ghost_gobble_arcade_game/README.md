# Instructions
In this exercise, you need to implement some rules from Pac-Man, the classic 1980s-era arcade-game.

You have four rules to implement, all related to the game states.

### Task 1: Define if Pac-Man eats a ghost
Define the `eat_ghost()` function that takes two parameters (if Pac-Man has a power pellet active and if Pac-Man is touching a ghost) and returns a Boolean value if Pac-Man is able to eat the ghost. The function should return `True` only if Pac-Man has a power pellet active and is touching a ghost.
```py
>>> eat_ghost(False, True)
...
False
```

### Task 2: Define if Pac-Man scores
Define the `score()` function that takes two parameters (if Pac-Man is touching a power pellet and if Pac-Man is touching a dot) and returns a Boolean value if Pac-Man scored. The function should return `True` if Pac-Man is touching a power pellet or a dot.
```py
>>> score(True, True)
...
True
```

### Task 3: Define if Pac-Man loses
Define the `lose()` function that takes two parameters (if Pac-Man has a power pellet active and if Pac-Man is touching a ghost) and returns a Boolean value if Pac-Man loses. The function should return `True` if Pac-Man is touching a ghost and does not have a power pellet active.
```py
>>> lose(False, True)
...
True
```

### Task 4: Define if Pac-Man wins
Define the `win()` function that takes three parameters (if Pac-Man has eaten all of the dots, if Pac-Man has a power pellet active, and if Pac-Man is touching a ghost) and returns a Boolean value if Pac-Man wins. The function should return `True` if Pac-Man has eaten all of the dots and has not lost based on the parameters defined in part 3.
```py
>>> win(False, True, False)
...
False
```

Evaluating Boolean experssions using `and`, `or`, and `not` operators:
```py
>>> true_variable = True and True
>>> false_variable = True and False

>>> true_variable = False or True
>>> false_variable = False or False

>>> true_variable = not False
>>> false_variable = not True
```