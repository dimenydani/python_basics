def within_range(num: int, min: int, max: int) -> bool:
     return (min < number and number <= max)

def give_message() -> None:
    state: str = ""
    if 0 < number and number <= 99:
        # OK
        if number <= 25:
            state = "young"
        elif number < 50:
            state = "adult"
        elif number < 75:
            state = "elderly"
        elif number < 99:
            state = "ghost"

    match state:
        case "young":
            print("Luck(e)y")
        case "adult":
            print("♥")
        case "elderly":
            print("legend")
        case "ghost":
            print("Fart")
        case _:
            pass

while (True):
    answer: str = input("How old are you?")
    # Check if valid number
    try:
            number = int(answer)
    except ValueError as err:
            print("Give a valid number")
            continue
    # Check if input is between 0 and 99
    valid: bool = within_range(number, 0, 99)
    if not valid:
         print("You gave wrong number (0 - 99)")
         continue

    give_message(number)
    break