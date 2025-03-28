import segno

# When run, prompt the user with the choice of "Quick QR Code" or "Custom QR Code"
    # Quick QR Code will just create a basic QR code.
    # Custom QR Code will let the user customize colors, size, etc.

# For both, prompt the user for the information being converted into the QR code. 
    # Ask for information type (text, link, contact info (MeCard or vCard), wifi password, geolocation, eventually images too: see guides.md).
        # There's also European Payments Council Quick Response Codes (EPC QR Codes), though I'm putting this off until later.
    # Ask for the information content (either point a file or paste the info, TBD)
    # At this point, Quick QR Code is finished.

# From here on out, only Custom QR Code will follow these steps.
    # Ask user for size
    # Ask user for color or custom image option
        # If color option chosen, prompt user with options for dark, data_dark and data_light options with color codes.
        # If custom image option is chosen, ask user for filepath to image
# At this point, Custom QR Code is finished.

# Future Plans:
    # Add GUI
    # Implement image encoding
    # Implement EPC QR Codes
    # Add web dev functionalities

def start():
    print("=== QR Code Generator ===")
    while True:
        print("1. Quick QR Code")
        print("2. Custom QR Code")

        mode_choice = input("Please select between Quick QR Code or Custom QR Code: ").strip()

        if mode_choice == '1':
            quick_qr()
        elif mode_choice == '2':
            custom_qr()
        else:
            print('Please type a valid number.')

def info_type():
    while True:
        print("1. Text")
        print("2. Website Link")
        print("3. Contact Information")
        print("4. Wifi Passwords")
        print("5. Geolocation")
        print("6. Image")
        print("7. EPC (European Payment Council QR Codes)")

        info_type_choice = input("Please select what type of information you are encoding: ").strip()

        if info_type_choice == '1':
            return 'text'
        elif info_type_choice == '2':
            return 'link'
        elif info_type_choice == '3':
            return 'contact'
        elif info_type_choice == '4':
            return 'wifi'
        elif info_type_choice == '5':
            return 'geo'
        elif info_type_choice == '6':
            return 'image'
        elif info_type_choice == '7':
            return 'epc'
        else:
            print('Please type a valid number.')


def info_content():
    pass

def quick_qr():
    info_type_choice = info_type()
    if info_type_choice == 'text':
        pass
    elif info_type_choice == 'link':
        pass
    elif info_type_choice == 'contact':
        pass
    elif info_type_choice == 'wifi':
        pass
    elif info_type_choice == 'geo':
        pass
    else:
        print('This feature is not yet implemented :(')
        pass

def custom_qr():
    info_type_choice = info_type()
    if info_type_choice == 'text':
        pass
    elif info_type_choice == 'link':
        pass
    elif info_type_choice == 'contact':
        pass
    elif info_type_choice == 'wifi':
        pass
    elif info_type_choice == 'geo':
        pass
    else:
        print('This feature is not yet implemented :(')
        pass

start()