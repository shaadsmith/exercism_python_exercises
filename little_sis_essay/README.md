# Instructions
In this exercise you are helping your younger sister edit her paper for school. The teacher is looking for correct punctuation, grammar, and excellent word choice.

You have four tasks to clean up and modify strings.
 
### Task 1: Capitalize the title of the paper

Any good paper needs a properly formatted title. Implement the function `capitalize_title(<title>)` which takes a title `str` as a parameter and capitalizes the first letter of each word. This function should return a `str` in title case.

```py
>>> capitalize_title("my hobbies")
"My Hobbies"
```

### Task 2: Check if each sentence ends with a period

You want to make sure that the punctuation in the paper is perfect. Implement the function `check_sentence_ending()` that takes `sentence` as a parameter. This function should return a bool.

```py
>>> check_sentence_ending("I like to hike, bake, and read.")
True
```

### Task 3: Clean up spacing

To make the paper look professional, unnecessary spacing needs to be removed. Implement the function `clean_up_spacing()` that takes `sentence` as a parameter. The function should remove extra whitespace at both the beginning and the end of the sentence, returning a new, updated sentence `str`.

```py
>>> clean_up_spacing(" I like to go on hikes with my dog.  ")
"I like to go on hikes with my dog."
```

### Task 4: Replace words with a synonym

To make the paper even better, you can replace some of the adjectives with their synonyms. Write the function `replace_word_choice()` that takes `sentence`, `old_word`, and `new_word` as parameters. This function should replace all instances of the `old_word` with the `new_word`, and return a new `str` with the updated sentence.

```py
>>> replace_word_choice("I bake good cakes.", "good", "amazing")
"I bake amazing cakes."
```