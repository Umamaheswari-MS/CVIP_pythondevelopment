def remove_common_letters(name1, name2):
    common_letters = set(name1) & set(name2)
    name1 = ''.join(char for char in name1 if char not in common_letters)
    name2 = ''.join(char for char in name2 if char not in common_letters)
    return name1, name2

def flames_result(name1, name2):
    flames = ['Friends', 'Lovers', 'Affectionate', 'Marriage', 'Enemies', 'Siblings']
    remaining_letters = len(name1) + len(name2)

    while len(flames) > 1:
        count = remaining_letters % len(flames)
        flames.pop(count - 1)
        flames = flames[count - 1:] + flames[:count - 1]

    return flames[0]

def play_flames():
    print("Welcome to the FLAMES game!")
    name1 = input("Enter the first person's name: ").strip().lower()
    name2 = input("Enter the second person's name: ").strip().lower()

    name1, name2 = remove_common_letters(name1, name2)
    result = flames_result(name1, name2)

    print(f"The relationship status between {name1.capitalize()} and {name2.capitalize()} is: {result}")

if __name__ == "__main__":
    play_flames()
