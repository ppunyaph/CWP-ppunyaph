def average(students: list) -> float:
    return sum(students) / len(students)

def main():
    class_3B = {
        "marine": 18,
        "jean": 15,
        "coline": 8,
        "luc": 9
        }
    class_3C = {
        "quentin": 17,
        "julie": 15,
        "marc": 8,
        "stephanie": 13
        }
    print(f"Average for class 3B: {average(list(class_3B.values()))}.")
    print(f"Average for class 3C: {average(list(class_3C.values()))}.")

main()