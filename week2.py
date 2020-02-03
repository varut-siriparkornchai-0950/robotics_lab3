def validate_pin(pin):
    let = len(pin)                                          # len(pin) -> counting letter in 'pin'
    for a in pin:
        if a in range(10):
            if pin.isdigit() == True and (let == 4 or let == 6):    # .isdigit() -> check pin, Is that digital(number)?
                 print(True)
            else:
                print(False)
        else:
            break
    print(False)


print("here")
validate_pin(m)



