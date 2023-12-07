from functools import lru_cache

def parse(input):
    return [[set(numbers.split(' ')) - set([' ', '']) for numbers in card.split(': ')[-1].split(" | ")] for card in input.read().splitlines()] 

def part_1(scratch_cards):
    """Calculates the sum of points of all cards"""
    return sum([2**((len(card[0] & card[1]))-1) if len(card[0] & card[1]) != 0 else 0 for card in scratch_cards])

@lru_cache(maxsize=None)
def get_number_of_cards(i):
    """Calculates the number of cards that can be scratched from a given card"""
    global scratch_cards
    new_cards = 1
    n = len(scratch_cards[i][0] & scratch_cards[i][1])
    if n == 0:
        return new_cards
    for j in range(i+1, min(len(scratch_cards), i+n+1)):
        new_cards += get_number_of_cards(j)
    return new_cards

def part_2(scratch_cards):
    """Calculates the number of cards that can be scratched from all cards"""
    new_cards = 0
    for card in scratch_cards:
        new_cards += get_number_of_cards(scratch_cards.index(card))
    return new_cards

if __name__ == "__main__":
    scratch_cards = parse(open("input.txt", "r"))
    print("Part 1: ", part_1(scratch_cards)) # 18619
    print("Part 2: ", part_2(scratch_cards)) # 8063216
