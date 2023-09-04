# Write the solution for "Filter Vowels".

# open file and read in the words
with open("inputs/vowels.txt", "r") as f:
    words = f.read().splitlines()

vowels = {"a", "e", "i", "o", "u"}

# filter out the vowels
res = 0
for i in words:
    for j in i:
        if j.lower() in vowels:
            res += 1

# write the output to a file
file_name = f"vowels-{res}.txt"
with open(f"outputs/{file_name}", "w") as f:
    f.write("\n".join(words))
