# WEEK 6: SIMPLE SPN IMPLEMENTATION

# 4-bit S-Box (non-linear substitution)
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

# Permutation function (diffusion step)
def permute(bits):
    # swaps positions of bits
    return bits[2] + bits[0] + bits[3] + bits[1]

# INPUT SECTION
plaintext = input("Enter 4-bit plaintext (e.g. 1010): ")
key = input("Enter 4-bit key (e.g. 0101): ")

print("\n--- SPN PROCESS START ---")

# STEP 1: KEY MIXING (XOR)
mixed = format(int(plaintext, 2) ^ int(key, 2), '04b')
print("After Key Mixing (XOR):", mixed)

# STEP 2: SUBSTITUTION (S-BOX)
substituted = SBOX[mixed]
print("After Substitution (S-Box):", substituted)

# STEP 3: PERMUTATION
permuted = permute(substituted)
print("After Permutation:", permuted)

print("\nFINAL CIPHERTEXT:", permuted)
print("--- SPN PROCESS END ---")