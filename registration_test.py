import registration
from utils import check_bool_input

devices = registration.scan(filter_unregistered=True)
for device in devices:
    print(f"Register device:\n{device}\n?")
    if check_bool_input():
        device.register()
        print("Success!")


