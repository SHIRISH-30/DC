def calculate_need(max_matrix, allocation_matrix):
    n = len(max_matrix)
    m = len(max_matrix[0])
    need = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(max_matrix[i][j] - allocation_matrix[i][j])
        need.append(row)
    return need

def is_safe_state(n, m, available, max_matrix, allocation_matrix):
    need = calculate_need(max_matrix, allocation_matrix)
    finish = [False] * n
    work = available.copy()
    safe_sequence = []

    while len(safe_sequence) < n:
        found = False
        for i in range(n):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(m)):
                for j in range(m):
                    work[j] += allocation_matrix[i][j]
                finish[i] = True
                safe_sequence.append(i)
                print(f"Process {i} has completed.")
                found = True
        if not found:
            print("System is in an unsafe state. Deadlock may occur.")
            return False

    print("System is in a safe state. No deadlock detected.")
    print("Safe sequence:", ' → '.join(f"P{p}" for p in safe_sequence))
    return True

def main():
    try:
        n = int(input("Enter the number of processes: "))
        m = int(input("Enter the number of resources: "))

        print("Enter Max matrix:")
        max_matrix = [list(map(int, input(f"Max for process {i}: ").split())) for i in range(n)]

        print("Enter Allocation matrix:")
        allocation_matrix = [list(map(int, input(f"Allocation for process {i}: ").split())) for i in range(n)]

        available = list(map(int, input("Enter available resources: ").split()))

        is_safe_state(n, m, available, max_matrix, allocation_matrix)

    except ValueError:
        print("Invalid input! Please enter valid integers.")

if __name__ == "__main__":
    main()
