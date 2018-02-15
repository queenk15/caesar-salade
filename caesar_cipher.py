def shift(letter, shift_amount):
    unicode_value = ord(letter) + shift_amount

    if unicode_value > 126:
        remainder = unicode_value - 126
        new_value = 31 + remainder
        new_letter = chr(new_value)

    elif unicode_value < 32:
        remainder = 32 - unicode_value
        new_value = 127 - remainder
        new_letter = chr(new_value)
        
    else:
        new_letter = chr(unicode_value)

    return new_letter

def encrypt(message, shift_amount):
    result = ""

    for letter in message:
        result += shift(letter, shift_amount)

        
            
        
    return result


def decrypt(message, shift_amount):
    return encrypt(message, -1 * shift_amount)

secret_message = "~KYERRA IS THE BEST~(p.s. this is hard) [<user>] @112234554444:'\\//ADBC"
encrypted_message = encrypt(secret_message, 20)
unencrypted_message = secret_message
decrypted_message = decrypt(encrypted_message, 20)

print(unencrypted_message)
print(encrypted_message)
print(decrypted_message)

