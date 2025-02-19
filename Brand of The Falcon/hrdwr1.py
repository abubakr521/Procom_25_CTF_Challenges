#!/usr/bin/env python3

import random

def encrypt(data, key):
    encrypted = [(data[i] ^ key[i]) for i in range(16)]
    encrypted[2] = ~key[2] & 1
    encrypted[7] = ~key[7] & 1
    encrypted[12] = ~key[12] & 1
    return encrypted

def check_backdoor(data):
    backdoor_pattern = [0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1]
    return data == backdoor_pattern

def main():
    FLAG = "AxP25{N0t_th4t_h4rd_w4r3}"
    key = [random.randint(0, 1) for _ in range(16)]  # Simulated key from VHDL
    
    print("Enter a 16-bit binary string:")
    user_input = input().strip()
    
    if len(user_input) != 16 or any(c not in '01' for c in user_input):
        print("Invalid input. Must be a 16-bit binary string.")
        return
    
    data = [int(bit) for bit in user_input]
    
    if check_backdoor(data):
        print(f"Correct! Here is your flag: {FLAG}")
    else:
        encrypted_data = encrypt(data, key)
        print("Incorrect input. Encrypted Output:", ''.join(map(str, encrypted_data)))

if __name__ == "__main__":
    main()
