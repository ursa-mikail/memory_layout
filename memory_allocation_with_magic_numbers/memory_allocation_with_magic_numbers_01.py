import random
import secrets

def generate_random_hex_bytes(length):
    return secrets.token_hex(length // 2)

def xxd_p_simulation_with_addresses(memory, mem_start, columns=16):
    hex_lines = []
    for i, row in enumerate(memory):
        address = '{:08X}'.format(mem_start + (i * columns))
        hex_line = address + ' ' + ' '.join(row)
        hex_lines.append(hex_line)
    return '\n'.join(hex_lines)

# Configuration
rows = 16  # Number of rows
columns = 16  # Number of columns per row
top_define = 'AA'
bottom_define = 'EE'
left_define = 'dd'
right_define = 'bb'

# Initialize memory array with incrementing hex values
memory = [['{:02X}'.format(i * columns + j) for j in range(columns)] for i in range(rows)]

# Apply defines
for j in range(columns):
    memory[0][j] = top_define
    memory[-1][j] = bottom_define

for i in range(rows):
    memory[i][0] = left_define
    memory[i][-1] = right_define

# Function to simulate xxd -p output with memory addresses
def xxd_p_simulation_with_addresses(memory, mem_start, columns=16):
    hex_lines = []
    for i, row in enumerate(memory):
        address = '{:08X}'.format(mem_start + (i * columns)) # address = 'mem+{:X}'.format(i * columns)
        hex_line = address + ' ' + ' '.join(row)
        hex_lines.append(hex_line)
    return '\n'.join(hex_lines)

# Random starting address
starting_index = random.randint(0, rows * columns - 1)
# mem_start = 0x1000 # static starting address or (generate random hex 8 bytes)

# Generate a random 8-byte hexadecimal starting address
mem_start = int(generate_random_hex_bytes(8), 16)

print(f"Starting index: {starting_index}")

# Print the memory layout with addresses
print("Memory layout with addresses:")
print(xxd_p_simulation_with_addresses(memory, mem_start))

# Simulate xxd -p output
def xxd_p_simulation(memory):
    hex_stream = ''
    for row in memory:
        for value in row:
            hex_stream += value
    return hex_stream.lower()

xxd_output = xxd_p_simulation(memory)
print("\nxxd -p simulation:")
print(xxd_output)

# Optionally, slice the output from the random starting address
print("\nxxd -p output from random starting address:")
print(xxd_output[starting_index*2:])  # *2 because each hex value is 2 characters


"""
Starting index: 146
Memory layout with addresses:
3EE7B7A2 dd AA AA AA AA AA AA AA AA AA AA AA AA AA AA bb
3EE7B7B2 dd 11 12 13 14 15 16 17 18 19 1A 1B 1C 1D 1E bb
3EE7B7C2 dd 21 22 23 24 25 26 27 28 29 2A 2B 2C 2D 2E bb
3EE7B7D2 dd 31 32 33 34 35 36 37 38 39 3A 3B 3C 3D 3E bb
3EE7B7E2 dd 41 42 43 44 45 46 47 48 49 4A 4B 4C 4D 4E bb
3EE7B7F2 dd 51 52 53 54 55 56 57 58 59 5A 5B 5C 5D 5E bb
3EE7B802 dd 61 62 63 64 65 66 67 68 69 6A 6B 6C 6D 6E bb
3EE7B812 dd 71 72 73 74 75 76 77 78 79 7A 7B 7C 7D 7E bb
3EE7B822 dd 81 82 83 84 85 86 87 88 89 8A 8B 8C 8D 8E bb
3EE7B832 dd 91 92 93 94 95 96 97 98 99 9A 9B 9C 9D 9E bb
3EE7B842 dd A1 A2 A3 A4 A5 A6 A7 A8 A9 AA AB AC AD AE bb
3EE7B852 dd B1 B2 B3 B4 B5 B6 B7 B8 B9 BA BB BC BD BE bb
3EE7B862 dd C1 C2 C3 C4 C5 C6 C7 C8 C9 CA CB CC CD CE bb
3EE7B872 dd D1 D2 D3 D4 D5 D6 D7 D8 D9 DA DB DC DD DE bb
3EE7B882 dd E1 E2 E3 E4 E5 E6 E7 E8 E9 EA EB EC ED EE bb
3EE7B892 dd EE EE EE EE EE EE EE EE EE EE EE EE EE EE bb

xxd -p simulation:
ddaaaaaaaaaaaaaaaaaaaaaaaaaaaabbdd1112131415161718191a1b1c1d1ebbdd2122232425262728292a2b2c2d2ebbdd3132333435363738393a3b3c3d3ebbdd4142434445464748494a4b4c4d4ebbdd5152535455565758595a5b5c5d5ebbdd6162636465666768696a6b6c6d6ebbdd7172737475767778797a7b7c7d7ebbdd8182838485868788898a8b8c8d8ebbdd9192939495969798999a9b9c9d9ebbdda1a2a3a4a5a6a7a8a9aaabacadaebbddb1b2b3b4b5b6b7b8b9babbbcbdbebbddc1c2c3c4c5c6c7c8c9cacbcccdcebbddd1d2d3d4d5d6d7d8d9dadbdcdddebbdde1e2e3e4e5e6e7e8e9eaebecedeebbddeeeeeeeeeeeeeeeeeeeeeeeeeeeebb

xxd -p output from random starting address:
92939495969798999a9b9c9d9ebbdda1a2a3a4a5a6a7a8a9aaabacadaebbddb1b2b3b4b5b6b7b8b9babbbcbdbebbddc1c2c3c4c5c6c7c8c9cacbcccdcebbddd1d2d3d4d5d6d7d8d9dadbdcdddebbdde1e2e3e4e5e6e7e8e9eaebecedeebbddeeeeeeeeeeeeeeeeeeeeeeeeeeeebb
"""