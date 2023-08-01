# Instructions

Elyse is really looking forward to playing some poker (and other card games) during her upcoming trip to Vegas. Being a big fan of "self-tracking" she wants to put together some small functions that will help her with tracking tasks and has asked for your help thinking them through.

### Task 1: Tracking Poker Rounds

Elyse is especially fond of poker, and wants to track how many rounds she plays - and which rounds those are. Every round has its own number, and every table shows the round number currently being played. Elyse chooses a table and sits down to play her first round. She plans on playing three rounds.

Implement a function `get_rounds(<round_number>)` that takes the current round number and returns a single `list` with that round and the next two that are coming up:

```py
>>> get_rounds(27)
[27, 28, 29]
```

### Task 2: Keeping all Rounds in the Same Place

Elyse played a few rounds at the first table, then took a break and played some more rounds at a second table ... but ended up with a different list for each table! She wants to put the two lists together, so she can track all of the poker rounds in the same place.

Implement a function `concatenate_rounds(<rounds_1>, <rounds_2>)` that takes two lists and returns a single `list` consisting of all the rounds in the first `list`, followed by all the rounds in the second `list`:

```py
>>> concatenate_rounds([27, 28, 29], [35, 36])
[27, 28, 29, 35, 36]
```

### Task 3: Finding Prior Rounds

Talking about some of the prior Poker rounds, another player remarks how similarly two of them played out. Elyse is not sure if she played those rounds or not.

Implement a function `list_contains_round(<rounds>, <round_number>)` that takes two arguments, a list of rounds played and a round number. The function will return `True` if the round is in the list of rounds played, `False` if not:

```py
>>> list_contains_round([27, 28, 29, 35, 36], 29)
True

>>> list_contains_round([27, 28, 29, 35, 36], 30)
False
```

### Task 4: Averaging Card Values

Elyse wants to try out a new game called Black Joe. It's similar to Black Jack - where your goal is to have the cards in your hand add up to a target value - but in Black Joe the goal is to get the average of the card values to be 7. The average can be found by summing up all the card values and then dividing that sum by the number of cards in the hand.

Implement a function `card_average(<hand>)` that will return the average value of a hand of Black Joe.

```py
>>> card_average([5, 6, 7])
6.0
```

### Task 5: Alternate Averages

In Black Joe, speed is important. Elyse is going to try and find a faster way of finding the average.

She has thought of two ways of getting an average-like number:

- Take the average of the first and last number in the hand.
- Using the median (middle card) of the hand.

Implement the function `approx_average_is_average(<hand>)`, given `hand`, a list containing the values of the cards in your hand.

Return `True` if either one `or` both of the, above named, strategies result in a number equal to the actual average.

Note: The length of all hands are odd, to make finding a median easier.

```py
>>> approx_average_is_average([1, 2, 3])
True

>>> approx_average_is_average([2, 3, 4, 8, 8])
True

>>> approx_average_is_average([1, 2, 3, 5, 9])
False
```

### Task 6: More Averaging Techniques

Intrigued by the results of her averaging experiment, Elyse is wondering if taking the average of the cards at the even positions versus the average of the cards at the odd positions would give the same results. Time for another test function!

Implement a function `average_even_is_average_odd(<hand>)` that returns a Boolean indicating if the average of the cards at even indexes is the same as the average of the cards at odd indexes.

```py
>>> average_even_is_average_odd([1, 2, 3])
True

>>> average_even_is_average_odd([1, 2, 3, 4])
False
```

### Task 7: Bonus Round Rules

Every 11th hand in Black Joe is a bonus hand with a bonus rule: if the last card you draw is a Jack, you double its value.

Implement a function `maybe_double_last(<hand>)` that takes a hand and checks if the last card is a Jack (11). If the last card **is** a Jack (11), double its value before returning the hand.

```py
>>> hand = [5, 9, 11]
>>> maybe_double_last(hand)
[5, 9, 22]

>>> hand = [5, 9, 10]
>>> maybe_double_last(hand)
[5, 9, 10]
```