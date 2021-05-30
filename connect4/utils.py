def get_int_input() -> int:

    while True:
        try:
            val = int(input())
        except ValueError:
            print("Value should be positive integer")
            pass

        if val <= 0:
            print("Value should be positive integer")
            continue

        return val
