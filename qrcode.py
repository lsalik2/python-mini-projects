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

def quick_qr:
    if info_type == text:
        pass
    elif info_type == link:
        pass
    elif info_type == contact:
        pass
    elif info_type == wifi:
        pass
    elif info_type == geo:
        pass
    else:
        print('This feature is not yet implemented :(')
        break

def custom_qr:
    if info_type == text:
        pass
    elif info_type == link:
        pass
    elif info_type == contact:
        pass
    elif info_type == wifi:
        pass
    elif info_type == geo:
        pass
    else:
        print('This feature is not yet implemented :(')
        break