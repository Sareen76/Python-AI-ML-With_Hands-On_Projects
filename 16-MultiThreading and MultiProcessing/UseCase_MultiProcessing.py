'''
Factorial Calculation using MultiProcessing
Calculating the factorial of a number is a common mathematical operation. When dealing with large numbers or a large list of numbers, the computation can be time-consuming. MultiProcessing can help speed up the process by distributing the calculations across multiple CPU cores.
'''

import multiprocessing
import math
import time
import sys


sys.set_int_max_str_digits(100000)

def compute_factorial(num):
    print(f"Computing factorial of {num}")
    result = math.factorial(num)
    print(f"Factorial of {num} is computed")
    return result

if __name__ == "__main__":
    number = [1000, 2000, 3000, 4000, 5000]

    start_time = time.time()
    
    # Create a pool of proce
    # sses
    with multiprocessing.Pool() as pool:
        results = pool.map(compute_factorial, number)

    end_time = time.time()-start_time
    print("Factorials Computed: ", results)
    print(f"Time taken with multiprocessing: {end_time} seconds")