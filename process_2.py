import multiprocessing
import random

col = 1000
min = -1_000_000
max = 1_000_000

def generate(pipe_conn):
    numbers = [random.randint(min, max) for _ in range(col)]
    pipe_conn.send(numbers)
    pipe_conn.close()

def calculate(pipe_conn):
    numbers = pipe_conn.recv()
    squar = [num ** 2 for num in numbers]
    print("Рассчитанные квадраты чисел:")
    print(squar)