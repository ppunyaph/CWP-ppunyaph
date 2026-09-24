import sys

def shrink(text: str) -> str:
    return(text[slice(8)])

def enlarge(text: str) -> str:
    return text + "Z" * (8 - len(text))

def main():
    if len(sys.argv) == 1:
        print("none")
        return

    perams = sys.argv[1:]

    for i in perams:
        if len(i) < 8:
            print(enlarge(i))
        else:
            print(shrink(i))

main()