import random

NUM_NODES=5

nodes = [random.randint(1, 100) for _ in range(NUM_NODES)]
print("Initial node values:", nodes)

ROUNDS=8

for r in range(ROUNDS):
    print(f"\n--- Round {r + 1} ---")

    random.shuffle(nodes)

    for i in range(0, len(nodes) - 1, 2):
        avg = (nodes[i] + nodes[i + 1]) / 2
        nodes[i] = avg
        nodes[i + 1] = avg
        print(f"Node {i} and Node {i+1} exchanged values -> New value: {avg}")
    print("Current values:", [round(x, 2) for x in nodes])
    # print("nodes " , *nodes)

final_avg = sum(nodes) / len(nodes)
print("\nFinal approximate global average at all nodes:", round(final_avg, 2))
