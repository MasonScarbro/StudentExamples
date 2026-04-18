import sys
import tokenizer
from executor import execute_tokens
from easytello import tello
def run_tello_file(filename, scanner, executor):
    # Read file
    with open(filename, "r") as f:
        source = f.read()

    # Tokenize
    tokens = scanner(source).scan_tokens()
    my_drone = tello.Tello()
    my_drone.takeoff()
    # Execute
    executor(tokens, my_drone=my_drone)



if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py file.tello")
        exit(1)

    file_path = sys.argv[1]

    run_tello_file(
        file_path,
        tokenizer.Scanner,
        execute_tokens
    )