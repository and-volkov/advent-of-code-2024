# Day one link: https://adventofcode.com/2024/day/1


from collections import Counter

list_1 = []
list_2 = []

with open("input.txt", "r") as f:
    for line in f:
        list_1.append(int(line.strip().split()[0]))
        list_2.append(int(line.strip().split()[1]))


l1_sorted = sorted(list_1)
l2_sorted = sorted(list_2)

distance = 0
for i in range(len(l1_sorted)):
    distance += abs(l1_sorted[i] - l2_sorted[i])


print(f"Distance between lists: {distance}")


l2_freq = Counter(l2_sorted)

similarity_score = 0

for num in l1_sorted:
    if num in l2_freq:
        similarity_score += num * l2_freq[num]

print(f"Similarity score: {similarity_score}")
