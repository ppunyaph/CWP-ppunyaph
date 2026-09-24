import sys
if len(sys.argv) > 1:
    print("parameters:", len(sys.argv) - 1)
    for param in sys.argv[1:]:
        print(param + ":", len(param))
else:
    print("none")