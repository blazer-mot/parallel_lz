from potoki_1 import posled, potok
from process_2 import generate, calculate

def main():
    first_1 = posled()
    first_2 = potok()

if __name__ == "__main__":
    main()



def main():
    parent_conn, child_conn = multiprocessing.Pipe()

    process_generator = multiprocessing.Process(target=generate_numbers, args=(child_conn,))
    process_calculator = multiprocessing.Process(target=calculate_squares, args=(parent_conn,))

    process_generator.start()
    process_calculator.start()

    process_generator.join()
    process_calculator.join()

