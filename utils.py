def check_bool_input():
    while True:
        input_switch = input("[Yes/No]\n")
        match input_switch:
            case "yes" | "y" | "Yes":
                return True
            case "no" | "n" | "No":
                return False
            case _:
                print("Illegal input. Please try again:\n")
