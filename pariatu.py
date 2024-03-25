# Optimized code to generate a list of lists with sequences of numbers
lists = [[i, i+1, i+2] for i in range(0, 10, 3)]
# Adjust the last list if the range does not divide evenly
if lists[-1][-1] >= 10:
    lists[-1] = lists[-1][:10 % 3]
print(lists)
