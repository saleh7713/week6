def decrypt_cypher_text(encrypted_text, key):
    """
    Decrypts an encrypted text using a given key.

    Parameters:
    ----------
    encrypted_text : str
        The text to be decrypted.
    key : int
        The key used to decrypt the text.

    Returns:
    -------
    str:
        The decrypted text as a single string.
    
    Example:
    --------
    encrypted_text = "Hdfk#huuru#|rx#pdnh#lq#surjudpplqj#lv#dq#rssruwxqlw|#wr#ehfrph#d#ehwwhu#ghyhorshu$"
    key = 3
    decrypt_cypher_text(encrypted_text, key)
    # Output: "Face error you make in programming is an opportunity to become a better developer."
    """
    
    # function implementation here...
    decrypted_text = ""  # Initialize an empty string to store the decrypted text.

    for char in encrypted_text:
        # Convert the character to its ASCII code, subtract the key, and find the remainder modulo 256.
        decrypted_ascii = (ord(char) - key) % 256
        # Convert the ASCII code back to a character.
        decrypted_char = chr(decrypted_ascii)
        # Append the decrypted character to the decrypted_text string.
        decrypted_text += decrypted_char
        
    return decrypted_text