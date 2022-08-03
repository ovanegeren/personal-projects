from spellchecker import SpellChecker

spell = SpellChecker()
# TODO: Find a package that filters out web adresses.
my_sentance = "yolanda is a massive fucking nerd"
print(my_sentance)

split_sentance = spell.split_words(my_sentance)

correct = spell.known(split_sentance)
num_c = len(correct)

misspelled = spell.unknown(split_sentance)
num_m = len(misspelled)

spelling_rate = num_c / (num_c + num_m)

print(split_sentance)
print(correct)
print(misspelled)
print("Speling rate is: ", spelling_rate * 100)

