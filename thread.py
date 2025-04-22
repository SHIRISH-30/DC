import threading

print_lock=threading.Lock()
def add(a, b):
    with print_lock:
        print("Thread 1 started adding")
        result = a + b
        print(f"The result is {result}")

def subtract(x, y):
    with print_lock:
        print("Thread 2 started subtracting")
        result = x - y
        print(f"The result is {result}")

def main():
    # Get user inputs first
    a = int(input("Enter first number for addition: "))
    b = int(input("Enter second number for addition: "))
    x = int(input("Enter first number for subtraction: "))
    y = int(input("Enter second number for subtraction: "))

    # Create threads with arguments
    t1 = threading.Thread(target=add, args=(a, b))
    t2 = threading.Thread(target=subtract, args=(x, y))

    # Start and join threads
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("Both threads have finished.")

if __name__ == "__main__":
    main()
