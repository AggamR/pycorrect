# pycorrect
Text correction in python, accounting for similarity of the "typo" to actual predefined-words, and key proximity on the keyboard.

The function receives a word ("the typo"), and a bank of possible words. I originally intended for this to be used in an application launcher, but have since abandoned the idea. It attempts to score each word in the bank, to determine which matches best to "the typo".