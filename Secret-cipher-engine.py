def secret_cipher_engine():
    print("==================================================")
    print("MINIMAL CYBER-ENCRYPTER & DIARY PROTOCOL ")
    print("==================================================")
    
    print("1. Encrypt a Secret Message (Normal Text -> Secret Code)")
    print("2. Decrypt a Secret Message (Secret Code -> Normal Text)")
    choice = input("Choose your action protocol (1 or 2): ")
    
    if choice not in ["1", "2"]:
        print("Invalid command. Mainframe shutting down.")
        return
        
    message = input("\nEnter your target message: ")
    key = 3 
    
    processed_message = ""
    
    # Core Logic Engine
    for character in message:
        if character.isalpha(): # Check kar raha hai ki input letter hai ya koi number/space
            # Character ko computer ke numerical code (ASCII) mein badalna
            start_pos = ord('a') if character.islower() else ord('A')
            
            if choice == "1": # Encryption Logic (Aage badhao)
                new_char = chr((ord(character) - start_pos + key) % 26 + start_pos)
            else: # Decryption Logic
                new_char = chr((ord(character) - start_pos - key) % 26 + start_pos)
                
            processed_message += new_char
        else:
            # Agar space ya symbol hai (jaise ! ya ?), toh use bina badle jod do
            processed_message += character

    print("\n==================================================")
    if choice == "1":
        print(f" ENCRYPTED SECRET CODE: {processed_message}")
    else:
        print(f" DECRYPTED ORIGINAL TEXT: {processed_message}")
    print("==================================================")

# Run the cyber engine
secret_cipher_engine()
