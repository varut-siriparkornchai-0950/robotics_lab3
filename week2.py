def validate_pin(pin):
    let = len(pin)                                          # len(pin) -> counting letter in 'pin'
    if pin.isdigit() == True and (let == 4 or let == 6):    # .isdigit() -> check pin, Is that digital(number)?
        print(True)
    else:
        print(False)

validate_pin(pin)

