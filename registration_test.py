import registration

devices = registration.scan()
for device in devices:
    print(f"Register device:\n{device}\n?")
    input_switch = input("[Yes/No]")
    match input_switch:
        case "yes" | "y" | "Yes":
            device.register()
        case "no" | "n" | "No":
            continue
        case _:
            raise Exception("Illegal input.")

