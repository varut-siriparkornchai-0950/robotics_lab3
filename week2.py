def validate_pin(pin):
    let = len(pin)
    if pin.isdigit() == True and (let == 4 or let == 6):
        print(True)
    else:
        print(False)

validate_pin(pin)

