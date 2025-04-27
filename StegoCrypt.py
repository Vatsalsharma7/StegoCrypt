from PIL import Image

def encode_message(image_path, message, output_path):

    message += '~'
    binary_message = ''.join(format(ord(c), '08b') for c in message)

    image = Image.open(image_path)
    if image.mode not in ('RGB', 'RGBA'):
        image = image.convert('RGBA')

    pixels = image.load()
    width, height = image.size
    idx = 0

    for y in range(height):
        for x in range(width):
            if idx >= len(binary_message):
                break

            pixel = list(pixels[x, y])

            for n in range(3):
                if idx < len(binary_message):
                    pixel[n] = (pixel[n] & 0xFE) | int(binary_message[idx])
                    idx += 1

            pixels[x, y] = tuple(pixel)

    image.save(output_path)
    print("Message encoded and saved successfully!")


def decode_message(image_path):
    image = Image.open(image_path)
    if image.mode not in ('RGB', 'RGBA'):
        image = image.convert('RGBA')

    pixels = image.load()
    width, height = image.size
    binary_message = ''

    for y in range(height):
        for x in range(width):
            pixel = pixels[x, y]

            for n in range(3):
                binary_message += str(pixel[n] & 1)

    decoded_message = ''
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        if len(byte) == 8:
            char = chr(int(byte, 2))
            if char == '~':
                break
            decoded_message += char

    return decoded_message


if __name__ == "__main__":
    print("=== StegoCrypt - Python Steganography Tool ===")
    print("1. Encode a message into an image")
    print("2. Decode a message from an image")
    choice = input("Select an option (1 or 2): ")

    if choice == '1':
        img_path = input("Enter the path of the original image: ").strip()
        message = input("Enter the message to hide: ")
        output_path = input("Enter the path to save the encoded image: ").strip()
        encode_message(img_path, message, output_path)

    elif choice == '2':
        img_path = input("Enter the path of the encoded image: ").strip()
        hidden_message = decode_message(img_path)
        print(f"🔎 Hidden message: {hidden_message}")

    else:
        print("Invalid choice. Please select 1 or 2.")
