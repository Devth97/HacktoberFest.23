def binary_shift(text, shift):
    shifted_text = ""
    for char in text:
        if char.isalpha():
            # For alphabetic characters, shift only the letters and maintain the case
            is_upper = char.isupper()
            char = char.lower()
            char_code = ord(char) - ord('a')
            shifted_char_code = (char_code + shift) % 26
            shifted_char = chr(shifted_char_code + ord('a'))
            if is_upper:
                shifted_char = shifted_char.upper()
            shifted_text += shifted_char
        else:
            # For non-alphabetic characters, keep them as is
            shifted_text += char

    return shifted_text

# Example usage
plaintext = "Hello, World! 123"
shift_amount = 3
cipher = binary_shift(plaintext, shift_amount)
print("Original Text:", plaintext)
print("Shifted Text:", cipher)
