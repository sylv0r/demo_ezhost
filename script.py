import time
import sys

def main():
    i = 0
    while True:
        i = i + 1
        print("HELLO EZHOST " + str(i))
        sys.stdout.flush()
        time.sleep(5)

if __name__ == "__main__":
    main()
