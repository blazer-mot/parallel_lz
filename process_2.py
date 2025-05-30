import multiprocessing
import random

def square(number):
    return number ** 2

def generate():
    return [random.randint(-1_000_000, 1_000_000) for _ in range(1000)]

def kvadr():
    list = generate()  
    process_num = 2

    with multiprocessing.Pool(processes=process_num) as pool:
        squares = pool.map(square, list)  

    print("Квадраты чисел:", squares) 


