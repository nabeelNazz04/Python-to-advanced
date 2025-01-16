import time
import threading

def calc_square(numbers):
    """
    Function to calculate and print the squares of a list of numbers.
    Each calculation includes a delay of 0.2 seconds to simulate a time-intensive task.
    """
    print("Calculating squares of numbers...")
    for n in numbers:
        time.sleep(0.2)
        print(f"Square of {n}: {n * n}")

def calc_cube(numbers):
    """
    Function to calculate and print the cubes of a list of numbers.
    Each calculation includes a delay of 0.2 seconds to simulate a time-intensive task.
    """
    print("Calculating cubes of numbers...")
    for n in numbers:
        time.sleep(0.2)
        print(f"Cube of {n}: {n * n * n}")

if __name__ == "__main__":
    # Input list of numbers
    numbers = [2, 3, 8, 9]

    print("Without Multithreading:")
    start_time = time.time()

    # Sequential execution
    calc_square(numbers)
    calc_cube(numbers)

    print(f"Execution time without multithreading: {time.time() - start_time:.2f} seconds\n")

    print("************************************")
    print("With Multithreading:")

    # Reset start time
    start_time = time.time()

    # Create threads for parallel execution
    thread1 = threading.Thread(target=calc_square, args=(numbers,))
    thread2 = threading.Thread(target=calc_cube, args=(numbers,))

    # Start the threads
    thread1.start()
    thread2.start()

    # Wait for both threads to complete
    thread1.join()
    thread2.join()

    print(f"Execution time with multithreading: {time.time() - start_time:.2f} seconds")
