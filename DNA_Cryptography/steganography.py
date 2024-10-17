from PIL import Image


def hide_message_in_image(image_path, message, output_image_path):
    img = Image.open(image_path)
    encoded = img.copy()
    width, height = img.size
    message += '####'  # End-of-message delimiter

    binary_message = ''.join([format(ord(char), '08b') for char in message])
    message_len = len(binary_message)

    idx = 0
    for row in range(height):
        for col in range(width):
            if idx < message_len:
                r, g, b = img.getpixel((col, row))
                r_bin = format(r, '08b')
                new_r = int(r_bin[:-1] + binary_message[idx], 2)
                encoded.putpixel((col, row), (new_r, g, b))
                idx += 1
            if idx >= message_len:
                break
        if idx >= message_len:
            break
    encoded.save(output_image_path)


def extract_message_from_image(image_path):
    img = Image.open(image_path)
    binary_message = ''

    width, height = img.size
    for row in range(height):
        for col in range(width):
            r, g, b = img.getpixel((col, row))
            r_bin = format(r, '08b')
            binary_message += r_bin[-1]

    all_bytes = [binary_message[i:i + 8] for i in range(0, len(binary_message), 8)]
    decoded_message = ''.join([chr(int(byte, 2)) for byte in all_bytes])

    # Look for the end-of-message delimiter
    if '####' in decoded_message:
        return decoded_message[:decoded_message.index('####')]
    else:
        return None
