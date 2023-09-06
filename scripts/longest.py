# Write the solution for "Longest Word".

# open file and read in the words
with open("inputs/longest.txt", "r") as f:
    words = f.read().splitlines()

words = words[0].split(" ")
longest_word = max(words, key=len)

# surround the longest word (or equal lens) with asterisks
for i in range(len(words)):
    if words[i] == longest_word or len(words[i]) == len(longest_word):
        words[i] = "**" + words[i] + "**"

# write the output to a file
with open("outputs/longest.md", "w") as f:
    f.write(" ".join(words))
