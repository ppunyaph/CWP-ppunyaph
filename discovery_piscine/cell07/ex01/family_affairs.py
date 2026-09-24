def find_the_redheads(family: dict) -> list:
    redheads = []
    for member in family:
        if family[member] == 'red':
            redheads.append(member)
    return redheads

def main():
    dupont_family = {
        "florian": "red",
        "marie": "blond",
        "virginie": "brunette",
        "david": "red",
        "franck": "red"
        }

    print(find_the_redheads(dupont_family))

main()