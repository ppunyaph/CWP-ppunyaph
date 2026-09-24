import sys

def lowcase_it(s):
    return s.lower()

if len(sys.argv) == 1:
    print("none")
else:
    for arg in sys.argv[1:]:
        print(lowcase_it(arg))