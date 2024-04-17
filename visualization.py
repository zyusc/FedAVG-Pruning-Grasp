import matplotlib.pyplot as plt
import re

with open('g_095_10.txt', 'r', errors='replace') as file:
    lines = file.readlines()

round_count = 0
max_accuracy = 0

with open('new_file.txt', 'w') as file:
    for line in lines:
        if "Results after" in line:
            round_count += 1
            max_accuracy = 0
            file.write(line)
        elif "Avg Test Accuracy" in line:
            accuracy = float(line.split(':')[-1])
            max_accuracy = max(max_accuracy, accuracy)
            file.write(line.strip() + "\n")
            file.write(f"max_acc, {max_accuracy}\n")
        else:
            file.write(line)

# Read experiment results from the text file
filename = 'new_file.txt'
with open(filename, 'r') as file:
    lines = file.readlines()

# Extract max accuracy and average training loss
max_acc_values = []
avg_loss_values = []
for line in lines:
    if line.startswith("max_acc"):
        max_acc = float(line.split(',')[1].strip())
        max_acc_values.append(max_acc)
    elif line.startswith("--->"):

        # Split the string based on the decimal point
        parts = line.split('.')
        integer_part = parts[0]
        decimal_part = parts[1][:3]  # Retain only 3 digits after the decimal point

        # Combine the integer and truncated decimal parts with a decimal point
        truncated_line = integer_part + '.' + decimal_part
        match = re.search(r'[-+]?\d*\.\d+|\d+', truncated_line)
        if match:
            truncated_line = match.group()
            avg_loss = float(truncated_line)
            # print(avg_loss)  # Just for testing
        else:
            print("No numerical value found in the line")

        # Convert the truncated string to a float
        avg_loss = float(truncated_line)
        avg_loss_values.append(avg_loss)

# Generate training rounds
training_rounds = list(range(1, min(len(max_acc_values), len(avg_loss_values)) + 1))

# Plot max accuracy change
plt.figure(figsize=(10, 5))
plt.plot(training_rounds, max_acc_values[:len(training_rounds)], marker='o', color='b')
plt.title('Maximum Accuracy Change Over Training Rounds')
plt.xlabel('Training Rounds')
plt.ylabel('Maximum Accuracy')
plt.grid(True)
plt.show()

# Plot average training loss change
plt.figure(figsize=(10, 5))
plt.plot(training_rounds, avg_loss_values[:len(training_rounds)], marker='o', color='r')
plt.title('Average Training Loss Change Over Training Rounds')
plt.xlabel('Training Rounds')
plt.ylabel('Average Training Loss')
plt.grid(True)
plt.show()