#!python3
import sys
import resource


def use_gen(file):
    while True:
        line = file.readline()
        if not line:
            break
        yield line

def run():
    if len(sys.argv) != 2:
        sys.exit(1)

    with open(sys.argv[1], 'r') as file:
        for line in use_gen(file):
            pass


if __name__ == "__main__":
    try:
        run()
        print(f"Peak Memory Usage = "
        f"{resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000000000:.3f} GB")
        print(f"User Mode Time + System Mode Time = "
        f"{resource.getrusage(resource.RUSAGE_SELF).ru_utime + resource.getrusage(resource.RUSAGE_SELF).ru_stime:.2f}s")
    except Exception as e:
        print(f"Error caught: {e}")
