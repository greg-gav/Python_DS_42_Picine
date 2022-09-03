import sys


def encode(phrase, shift):
    result = ""
    for c in phrase:
        if c.isalpha() and c.isupper():
            result += chr((ord(c) + shift - 65) % 26 + 65)
        elif c.isalpha() and c.islower():
            result += chr((ord(c) + shift - 97) % 26 + 97)
        else:
            result += c
    print(result)


def decode(phrase, shift):
    result = ""
    for c in phrase:
        if c.isalpha() and c.isupper():
            result += chr((ord(c) - shift - 65) % 26 + 65)
        elif c.isalpha() and c.islower():
            result += chr((ord(c) - shift - 97) % 26 + 97)
        else:
            result += c
    print(result)


def run():
    if len(sys.argv) != 4:
        raise Exception("Incorrect number of arguments")
    for c in sys.argv[2]:
        if not 0 <= ord(c) <= 127:
            raise Exception(f"The script does not support your language yet")
    if sys.argv[1] == "encode":
        encode(phrase=sys.argv[2], shift=int(sys.argv[3]))
    elif sys.argv[1] == "decode":
        decode(phrase=sys.argv[2], shift=int(sys.argv[3]))


if __name__ == "__main__":
    run()
