import random

NUM_NODES = int(input("Enter the number of nodes: "))

# Take input from user for each node
nodes = []
for i in range(NUM_NODES):
    val = float(input(f"Enter value for node {i + 1}: "))
    nodes.append(val)

print("\nInitial node values:", [int(x) if x.is_integer() else x for x in nodes])

ROUNDS = 8

for r in range(ROUNDS):
    print(f"\n--- Round {r + 1} ---")

    # Shuffle indices instead of values
    indices = list(range(NUM_NODES))
    random.shuffle(indices)

    # Process in pairs using shuffled indices
    for i in range(0, NUM_NODES - 1, 2):
        idx1 = indices[i]
        idx2 = indices[i + 1]

        avg = (nodes[idx1] + nodes[idx2]) / 2
        nodes[idx1] = avg
        nodes[idx2] = avg

        print(f"Node {idx1} and Node {idx2} exchanged values -> New value: {round(avg, 2)}")

    print("Current values:", [round(x, 2) for x in nodes])

# Final average
final_avg = sum(nodes) / len(nodes)
print("\nFinal approximate global average at all nodes:", round(final_avg, 2))
