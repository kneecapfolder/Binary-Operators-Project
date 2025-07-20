def xor_encrypt_img(path, key):
    # Read the image as bytes
    with open(path, 'rb') as file:
        image_data = bytearray(file.read())

    # XOR each byte with the key
    encrypted_data = bytearray([byte ^ key for byte in image_data])

    # Write the encrypted image
    with open(path, 'wb') as file:
        file.write(encrypted_data)

xor_encrypt_img("./encryption(bonus)/cat.png", key = 123)
