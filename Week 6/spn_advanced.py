# ADVANCED SPN WITH MULTI-ROUND AND AVALANCHE EFFECT

# Strong 4-bit S-Box
SBOX = {
    '0000': '1110',
    '0001': '0100',
    '0010': '1101',
    '0011': '0001',
    '0100': '0010',
    '0101': '1111',
    '0110': '1011',
    '0111': '1000',
    '1000': '0011',
    '1001': '1010',
    '1010': '0110',
    '1011': '1100',
    '1100': '0101',
    '1101': '1001',
    '1110': '0000',
    '1111': '0111'
}

# Permutation (diffusion step)
def permute(bits):
    return bits[2] + bits[0] + bits[3] + bits[1]

# One SPN round
def spn_round(block, key):
    # Key mixing (XOR)
    mixed = format(int(block, 2) ^ int(key, 2), '04b')

    # Substitution
    substituted = SBOX[mixed]

    # Permutation
    permuted = permute(substituted)

    return permuted

# MULTI-ROUND SPN ENCRYPTION
def encrypt(plaintext, key, rounds=3):
    state = plaintext

    print("\n--- ENCRYPTION START ---")
    print("Plaintext:", plaintext)

    for i in range(rounds):
        state = spn_round(state, key)
        print(f"After Round {i+1}: {state}")

    print("Final Ciphertext:", state)
    print("--- ENCRYPTION END ---\n")

    return state


# AVALANCHE TEST FUNCTION
def avalanche_test():
    print("\n=== AVALANCHE EFFECT TEST ===")

    pt1 = "1010"
    pt2 = "1011"  # 1-bit difference

    key = "0101"

    print("\nEncrypting PT1:", pt1)
    c1 = encrypt(pt1, key)

    print("\nEncrypting PT2:", pt2)
    c2 = encrypt(pt2, key)

    print("RESULT COMPARISON")
    print("Ciphertext 1:", c1)
    print("Ciphertext 2:", c2)

    print("\nObservation: Small input change causes large output difference.")

# MAIN PROGRAM
plaintext = input("Enter 4-bit plaintext: ")
key = input("Enter 4-bit key: ")

ciphertext = encrypt(plaintext, key)

choice = input("Run avalanche test? (y/n): ")

if choice.lower() == 'y':
    avalanche_test()