import re

with open('g_085_5_server.txt', 'r', errors='replace') as file:
    lines = file.readlines()

# Extract the round number and average test accuracy from each result
round_test_accs = []
for line in lines:
    if "Results after" in line:
        match_round = re.search(r"Results after (\d+) rounds of training:", line)
        if match_round:
            current_round = int(match_round.group(1))
    elif "Avg Test Accuracy:" in line:
        match_acc = re.search(r"Avg Test Accuracy: (\d+\.\d+)", line)
        if match_acc:
            test_acc = float(match_acc.group(1))
            round_test_accs.append((current_round, test_acc))

# Get the maximum average test accuracy and the corresponding round number
max_round, max_test_acc = max(round_test_accs, key=lambda x: x[1])
print("Round with maximum average test accuracy:", max_round)
print("Maximum average test accuracy:", max_test_acc)
