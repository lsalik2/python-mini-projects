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
        print("0. Exit")

        mode_choice = input("Please select between Quick QR Code or Custom QR Code: ").strip()

        if mode_choice == '1':
            quick_qr()
            break
        elif mode_choice == '2':
            custom_qr()
            break
        elif mode_choice == '0':
            print("Exiting QR Code Generator.")
            break
        else:
            print('Please type a valid number.')

def info_type():
    while True:
        print("\nWhat type of information are you encoding?")
        print("1. Text")
        print("2. Website Link")
        print("3. Contact Information")
        print("4. Wifi Passwords")
        print("5. Geolocation")
        print("6. Image")
        print("7. EPC (European Payment Council QR Codes)")
        print("0. Cancel")

        choice = input("Enter number: ").strip()

        mapping = {
            '1': 'text',
            '2': 'link',
            '3': 'contact',
            '4': 'wifi',
            '5': 'geo',
            '6': 'image',
            '7': 'epc',
            '0': 'cancel'
        }

        if choice in mapping:
            return mapping[choice]
        else:
            print('Please type a valid number.')

def info_content(info_type_choice):
    if info_type_choice == 'text':
        return input("Enter the text to encode: ")
    elif info_type_choice == 'link':
        return input("Enter the URL to encode: ")
    elif info_type_choice in ['contact', 'wifi', 'geo', 'image', 'epc']:
        print(f"The '{info_type_choice}' type is not implemented yet.")
        return None
    elif info_type_choice == 'cancel':
        return None
    else:
        print("Unknown type.")
        return None

def quick_qr():
    pass

def custom_qr():
    pass

start()