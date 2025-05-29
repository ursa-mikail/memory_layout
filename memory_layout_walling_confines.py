import random

# Initialize memory array with incrementing hex values
def initialize_memory(rows, columns):
    return [['{:02X}'.format(i * columns + j) for j in range(columns)] for i in range(rows)]

def apply_mem_wall_confines(memory, top_define, bottom_define, left_define, right_define):
    rows, columns = len(memory), len(memory[0])

    for j in range(columns):
        memory[0][j] = top_define
        memory[-1][j] = bottom_define

    for i in range(rows):
        memory[i][0] = left_define
        memory[i][-1] = right_define

    return memory

# Function to simulate xxd -p output with memory addresses
def xxd_p_simulation_with_addresses(memory):
    hex_lines = []
    for i, row in enumerate(memory):
        address = 'mem+{:X}'.format(i * columns)
        hex_line = address + ' ' + ' '.join(row)
        hex_lines.append(hex_line)
    return '\n'.join(hex_lines)

# Checksum computation based on r_i, c_i
def compute_checksum(memory, rows, columns):
    checksum = 0
    for i in range(rows):
        for j in range(columns):
            r_i = random.randint(0, 255)  # Random value for r_i
            c_i = random.randint(0, 255)  # Random value for c_i
            modulus = columns  # Modulus based on number of columns
            checksum += (modulus * r_i + c_i - modulus)
    return checksum

# Simulate xxd -p output
def xxd_p_simulation(memory):
    hex_stream = ''
    for row in memory:
        for value in row:
            hex_stream += value
    return hex_stream.lower()

def xxd_simulation(data, cols=16):
    result = []
    offset = 0

    # Flatten data if it's a 2D list
    flat_data = b''.join(bytes.fromhex(value) for row in data for value in row)

    while offset < len(flat_data):
        chunk = flat_data[offset:offset + cols]
        hex_part = ' '.join(f"{byte:02x}" for byte in chunk)
        ascii_part = ''.join(chr(byte) if 32 <= byte <= 126 else '.' for byte in chunk)

        # Format hex into two 8-byte groups with extra spacing (like xxd does)
        hex_part_formatted = ' '.join([
            hex_part[:cols * 3 // 2].strip(),  # First 8 bytes
            hex_part[cols * 3 // 2:].strip()   # Second 8 bytes
        ])

        result.append(f"{offset:08x}: {hex_part_formatted:<48}  {ascii_part}")
        offset += cols

    return '\n'.join(result)

## [Usage]
# Configuration
rows = 16  # Number of rows
columns = 16  # Number of columns per row
top_define = 'AA'
bottom_define = 'EE'
left_define = 'dd'
right_define = 'bb'

# Initialize memory array with incrementing hex values
memory = initialize_memory(rows, columns)
remapped_memory = apply_mem_wall_confines(memory, top_define, bottom_define, left_define, right_define)

# Random starting address
starting_index = random.randint(0, rows * columns - 1)
print(f"Starting index: {starting_index}")

# Print the memory layout with addresses
print("Memory layout with addresses:")
print(xxd_p_simulation_with_addresses(remapped_memory))

xxd_output = xxd_simulation(remapped_memory)
print("\nxxd simulation:")
print(xxd_output)

# Optionally, slice the output from the random starting address
print("\nxxd -p output from random starting address:")
print(xxd_output[starting_index*2:])  # *2 because each hex value is 2 characters

# Calculate and print checksum
checksum = compute_checksum(remapped_memory, rows, columns)
print(f"\nChecksum: {checksum}")

##
memory = initialize_memory(rows, columns)
memory = apply_mem_wall_confines(memory, top_define, bottom_define, left_define, right_define)

# Random starting address
starting_index = random.randint(0, rows * columns - 1)
print(f"Starting index: {starting_index}")

# Print the memory layout with addresses
print("Memory layout with addresses:")
print(xxd_p_simulation_with_addresses(memory))

xxd_output = xxd_p_simulation(memory)
print("\nxxd -p simulation:")
print(xxd_output)

# Optionally, slice the output from the random starting address
print("\nxxd -p output from random starting address:")
print(xxd_output[starting_index*2:])  # *2 because each hex value is 2 characters

###
memory = initialize_memory(rows, columns)
memory = apply_mem_wall_confines(memory, top_define, bottom_define, left_define, right_define)

# Random starting address
starting_index = random.randint(0, rows * columns - 1)
print(f"Starting index: {starting_index}")

# Print the memory layout with addresses
print("Memory layout with addresses:")
print(xxd_p_simulation_with_addresses(memory))

xxd_output = xxd_p_simulation(memory)
print("\nxxd -p simulation:")
print(xxd_output)

# Optionally, slice the output from the random starting address
print("\nxxd -p output from random starting address:")
print(xxd_output[starting_index*2:])  # *2 because each hex value is 2 characters

###
memory = initialize_memory(rows, columns)
remapped_memory = apply_mem_wall_confines(memory, top_define, bottom_define, left_define, right_define)

# Random starting address
starting_index = random.randint(0, rows * columns - 1)
print(f"Starting index: {starting_index}")

# Print the memory layout with addresses
print("Memory layout with addresses:")
print(xxd_p_simulation_with_addresses(remapped_memory))

xxd_output = xxd_p_simulation(remapped_memory)
print("\nxxd -p simulation:")
print(xxd_output)

# Optionally, slice the output from the random starting address
print("\nxxd -p output from random starting address:")
print(xxd_output[starting_index*2:])  # *2 because each hex value is 2 characters

# Calculate and print checksum
checksum = compute_checksum(remapped_memory, rows, columns)
print(f"\nChecksum: {checksum}")

"""
Starting index: 51
Memory layout with addresses:
mem+0 dd AA AA AA AA AA AA AA AA AA AA AA AA AA AA bb
mem+10 dd 11 12 13 14 15 16 17 18 19 1A 1B 1C 1D 1E bb
mem+20 dd 21 22 23 24 25 26 27 28 29 2A 2B 2C 2D 2E bb
mem+30 dd 31 32 33 34 35 36 37 38 39 3A 3B 3C 3D 3E bb
mem+40 dd 41 42 43 44 45 46 47 48 49 4A 4B 4C 4D 4E bb
mem+50 dd 51 52 53 54 55 56 57 58 59 5A 5B 5C 5D 5E bb
mem+60 dd 61 62 63 64 65 66 67 68 69 6A 6B 6C 6D 6E bb
mem+70 dd 71 72 73 74 75 76 77 78 79 7A 7B 7C 7D 7E bb
mem+80 dd 81 82 83 84 85 86 87 88 89 8A 8B 8C 8D 8E bb
mem+90 dd 91 92 93 94 95 96 97 98 99 9A 9B 9C 9D 9E bb
mem+A0 dd A1 A2 A3 A4 A5 A6 A7 A8 A9 AA AB AC AD AE bb
mem+B0 dd B1 B2 B3 B4 B5 B6 B7 B8 B9 BA BB BC BD BE bb
mem+C0 dd C1 C2 C3 C4 C5 C6 C7 C8 C9 CA CB CC CD CE bb
mem+D0 dd D1 D2 D3 D4 D5 D6 D7 D8 D9 DA DB DC DD DE bb
mem+E0 dd E1 E2 E3 E4 E5 E6 E7 E8 E9 EA EB EC ED EE bb
mem+F0 dd EE EE EE EE EE EE EE EE EE EE EE EE EE EE bb

xxd simulation:
00000000: dd aa aa aa aa aa aa aa aa aa aa aa aa aa aa bb   ................
00000010: dd 11 12 13 14 15 16 17 18 19 1a 1b 1c 1d 1e bb   ................
00000020: dd 21 22 23 24 25 26 27 28 29 2a 2b 2c 2d 2e bb   .!"#$%&'()*+,-..
00000030: dd 31 32 33 34 35 36 37 38 39 3a 3b 3c 3d 3e bb   .123456789:;<=>.
00000040: dd 41 42 43 44 45 46 47 48 49 4a 4b 4c 4d 4e bb   .ABCDEFGHIJKLMN.
00000050: dd 51 52 53 54 55 56 57 58 59 5a 5b 5c 5d 5e bb   .QRSTUVWXYZ[\]^.
00000060: dd 61 62 63 64 65 66 67 68 69 6a 6b 6c 6d 6e bb   .abcdefghijklmn.
00000070: dd 71 72 73 74 75 76 77 78 79 7a 7b 7c 7d 7e bb   .qrstuvwxyz{|}~.
00000080: dd 81 82 83 84 85 86 87 88 89 8a 8b 8c 8d 8e bb   ................
00000090: dd 91 92 93 94 95 96 97 98 99 9a 9b 9c 9d 9e bb   ................
000000a0: dd a1 a2 a3 a4 a5 a6 a7 a8 a9 aa ab ac ad ae bb   ................
000000b0: dd b1 b2 b3 b4 b5 b6 b7 b8 b9 ba bb bc bd be bb   ................
000000c0: dd c1 c2 c3 c4 c5 c6 c7 c8 c9 ca cb cc cd ce bb   ................
000000d0: dd d1 d2 d3 d4 d5 d6 d7 d8 d9 da db dc dd de bb   ................
000000e0: dd e1 e2 e3 e4 e5 e6 e7 e8 e9 ea eb ec ed ee bb   ................
000000f0: dd ee ee ee ee ee ee ee ee ee ee ee ee ee ee bb   ................

xxd -p output from random starting address:
15 16 17 18 19 1a 1b 1c 1d 1e bb   ................
00000020: dd 21 22 23 24 25 26 27 28 29 2a 2b 2c 2d 2e bb   .!"#$%&'()*+,-..
00000030: dd 31 32 33 34 35 36 37 38 39 3a 3b 3c 3d 3e bb   .123456789:;<=>.
00000040: dd 41 42 43 44 45 46 47 48 49 4a 4b 4c 4d 4e bb   .ABCDEFGHIJKLMN.
00000050: dd 51 52 53 54 55 56 57 58 59 5a 5b 5c 5d 5e bb   .QRSTUVWXYZ[\]^.
00000060: dd 61 62 63 64 65 66 67 68 69 6a 6b 6c 6d 6e bb   .abcdefghijklmn.
00000070: dd 71 72 73 74 75 76 77 78 79 7a 7b 7c 7d 7e bb   .qrstuvwxyz{|}~.
00000080: dd 81 82 83 84 85 86 87 88 89 8a 8b 8c 8d 8e bb   ................
00000090: dd 91 92 93 94 95 96 97 98 99 9a 9b 9c 9d 9e bb   ................
000000a0: dd a1 a2 a3 a4 a5 a6 a7 a8 a9 aa ab ac ad ae bb   ................
000000b0: dd b1 b2 b3 b4 b5 b6 b7 b8 b9 ba bb bc bd be bb   ................
000000c0: dd c1 c2 c3 c4 c5 c6 c7 c8 c9 ca cb cc cd ce bb   ................
000000d0: dd d1 d2 d3 d4 d5 d6 d7 d8 d9 da db dc dd de bb   ................
000000e0: dd e1 e2 e3 e4 e5 e6 e7 e8 e9 ea eb ec ed ee bb   ................
000000f0: dd ee ee ee ee ee ee ee ee ee ee ee ee ee ee bb   ................

Checksum: 539969
Starting index: 227
Memory layout with addresses:
mem+0 dd AA AA AA AA AA AA AA AA AA AA AA AA AA AA bb
mem+10 dd 11 12 13 14 15 16 17 18 19 1A 1B 1C 1D 1E bb
mem+20 dd 21 22 23 24 25 26 27 28 29 2A 2B 2C 2D 2E bb
mem+30 dd 31 32 33 34 35 36 37 38 39 3A 3B 3C 3D 3E bb
mem+40 dd 41 42 43 44 45 46 47 48 49 4A 4B 4C 4D 4E bb
mem+50 dd 51 52 53 54 55 56 57 58 59 5A 5B 5C 5D 5E bb
mem+60 dd 61 62 63 64 65 66 67 68 69 6A 6B 6C 6D 6E bb
mem+70 dd 71 72 73 74 75 76 77 78 79 7A 7B 7C 7D 7E bb
mem+80 dd 81 82 83 84 85 86 87 88 89 8A 8B 8C 8D 8E bb
mem+90 dd 91 92 93 94 95 96 97 98 99 9A 9B 9C 9D 9E bb
mem+A0 dd A1 A2 A3 A4 A5 A6 A7 A8 A9 AA AB AC AD AE bb
mem+B0 dd B1 B2 B3 B4 B5 B6 B7 B8 B9 BA BB BC BD BE bb
mem+C0 dd C1 C2 C3 C4 C5 C6 C7 C8 C9 CA CB CC CD CE bb
mem+D0 dd D1 D2 D3 D4 D5 D6 D7 D8 D9 DA DB DC DD DE bb
mem+E0 dd E1 E2 E3 E4 E5 E6 E7 E8 E9 EA EB EC ED EE bb
mem+F0 dd EE EE EE EE EE EE EE EE EE EE EE EE EE EE bb

xxd -p simulation:
ddaaaaaaaaaaaaaaaaaaaaaaaaaaaabbdd1112131415161718191a1b1c1d1ebbdd2122232425262728292a2b2c2d2ebbdd3132333435363738393a3b3c3d3ebbdd4142434445464748494a4b4c4d4ebbdd5152535455565758595a5b5c5d5ebbdd6162636465666768696a6b6c6d6ebbdd7172737475767778797a7b7c7d7ebbdd8182838485868788898a8b8c8d8ebbdd9192939495969798999a9b9c9d9ebbdda1a2a3a4a5a6a7a8a9aaabacadaebbddb1b2b3b4b5b6b7b8b9babbbcbdbebbddc1c2c3c4c5c6c7c8c9cacbcccdcebbddd1d2d3d4d5d6d7d8d9dadbdcdddebbdde1e2e3e4e5e6e7e8e9eaebecedeebbddeeeeeeeeeeeeeeeeeeeeeeeeeeeebb

xxd -p output from random starting address:
e3e4e5e6e7e8e9eaebecedeebbddeeeeeeeeeeeeeeeeeeeeeeeeeeeebb
Starting index: 74
Memory layout with addresses:
mem+0 dd AA AA AA AA AA AA AA AA AA AA AA AA AA AA bb
mem+10 dd 11 12 13 14 15 16 17 18 19 1A 1B 1C 1D 1E bb
mem+20 dd 21 22 23 24 25 26 27 28 29 2A 2B 2C 2D 2E bb
mem+30 dd 31 32 33 34 35 36 37 38 39 3A 3B 3C 3D 3E bb
mem+40 dd 41 42 43 44 45 46 47 48 49 4A 4B 4C 4D 4E bb
mem+50 dd 51 52 53 54 55 56 57 58 59 5A 5B 5C 5D 5E bb
mem+60 dd 61 62 63 64 65 66 67 68 69 6A 6B 6C 6D 6E bb
mem+70 dd 71 72 73 74 75 76 77 78 79 7A 7B 7C 7D 7E bb
mem+80 dd 81 82 83 84 85 86 87 88 89 8A 8B 8C 8D 8E bb
mem+90 dd 91 92 93 94 95 96 97 98 99 9A 9B 9C 9D 9E bb
mem+A0 dd A1 A2 A3 A4 A5 A6 A7 A8 A9 AA AB AC AD AE bb
mem+B0 dd B1 B2 B3 B4 B5 B6 B7 B8 B9 BA BB BC BD BE bb
mem+C0 dd C1 C2 C3 C4 C5 C6 C7 C8 C9 CA CB CC CD CE bb
mem+D0 dd D1 D2 D3 D4 D5 D6 D7 D8 D9 DA DB DC DD DE bb
mem+E0 dd E1 E2 E3 E4 E5 E6 E7 E8 E9 EA EB EC ED EE bb
mem+F0 dd EE EE EE EE EE EE EE EE EE EE EE EE EE EE bb

xxd -p simulation:
ddaaaaaaaaaaaaaaaaaaaaaaaaaaaabbdd1112131415161718191a1b1c1d1ebbdd2122232425262728292a2b2c2d2ebbdd3132333435363738393a3b3c3d3ebbdd4142434445464748494a4b4c4d4ebbdd5152535455565758595a5b5c5d5ebbdd6162636465666768696a6b6c6d6ebbdd7172737475767778797a7b7c7d7ebbdd8182838485868788898a8b8c8d8ebbdd9192939495969798999a9b9c9d9ebbdda1a2a3a4a5a6a7a8a9aaabacadaebbddb1b2b3b4b5b6b7b8b9babbbcbdbebbddc1c2c3c4c5c6c7c8c9cacbcccdcebbddd1d2d3d4d5d6d7d8d9dadbdcdddebbdde1e2e3e4e5e6e7e8e9eaebecedeebbddeeeeeeeeeeeeeeeeeeeeeeeeeeeebb

xxd -p output from random starting address:
4a4b4c4d4ebbdd5152535455565758595a5b5c5d5ebbdd6162636465666768696a6b6c6d6ebbdd7172737475767778797a7b7c7d7ebbdd8182838485868788898a8b8c8d8ebbdd9192939495969798999a9b9c9d9ebbdda1a2a3a4a5a6a7a8a9aaabacadaebbddb1b2b3b4b5b6b7b8b9babbbcbdbebbddc1c2c3c4c5c6c7c8c9cacbcccdcebbddd1d2d3d4d5d6d7d8d9dadbdcdddebbdde1e2e3e4e5e6e7e8e9eaebecedeebbddeeeeeeeeeeeeeeeeeeeeeeeeeeeebb
Starting index: 23
Memory layout with addresses:
mem+0 dd AA AA AA AA AA AA AA AA AA AA AA AA AA AA bb
mem+10 dd 11 12 13 14 15 16 17 18 19 1A 1B 1C 1D 1E bb
mem+20 dd 21 22 23 24 25 26 27 28 29 2A 2B 2C 2D 2E bb
mem+30 dd 31 32 33 34 35 36 37 38 39 3A 3B 3C 3D 3E bb
mem+40 dd 41 42 43 44 45 46 47 48 49 4A 4B 4C 4D 4E bb
mem+50 dd 51 52 53 54 55 56 57 58 59 5A 5B 5C 5D 5E bb
mem+60 dd 61 62 63 64 65 66 67 68 69 6A 6B 6C 6D 6E bb
mem+70 dd 71 72 73 74 75 76 77 78 79 7A 7B 7C 7D 7E bb
mem+80 dd 81 82 83 84 85 86 87 88 89 8A 8B 8C 8D 8E bb
mem+90 dd 91 92 93 94 95 96 97 98 99 9A 9B 9C 9D 9E bb
mem+A0 dd A1 A2 A3 A4 A5 A6 A7 A8 A9 AA AB AC AD AE bb
mem+B0 dd B1 B2 B3 B4 B5 B6 B7 B8 B9 BA BB BC BD BE bb
mem+C0 dd C1 C2 C3 C4 C5 C6 C7 C8 C9 CA CB CC CD CE bb
mem+D0 dd D1 D2 D3 D4 D5 D6 D7 D8 D9 DA DB DC DD DE bb
mem+E0 dd E1 E2 E3 E4 E5 E6 E7 E8 E9 EA EB EC ED EE bb
mem+F0 dd EE EE EE EE EE EE EE EE EE EE EE EE EE EE bb

xxd -p simulation:
ddaaaaaaaaaaaaaaaaaaaaaaaaaaaabbdd1112131415161718191a1b1c1d1ebbdd2122232425262728292a2b2c2d2ebbdd3132333435363738393a3b3c3d3ebbdd4142434445464748494a4b4c4d4ebbdd5152535455565758595a5b5c5d5ebbdd6162636465666768696a6b6c6d6ebbdd7172737475767778797a7b7c7d7ebbdd8182838485868788898a8b8c8d8ebbdd9192939495969798999a9b9c9d9ebbdda1a2a3a4a5a6a7a8a9aaabacadaebbddb1b2b3b4b5b6b7b8b9babbbcbdbebbddc1c2c3c4c5c6c7c8c9cacbcccdcebbddd1d2d3d4d5d6d7d8d9dadbdcdddebbdde1e2e3e4e5e6e7e8e9eaebecedeebbddeeeeeeeeeeeeeeeeeeeeeeeeeeeebb

xxd -p output from random starting address:
1718191a1b1c1d1ebbdd2122232425262728292a2b2c2d2ebbdd3132333435363738393a3b3c3d3ebbdd4142434445464748494a4b4c4d4ebbdd5152535455565758595a5b5c5d5ebbdd6162636465666768696a6b6c6d6ebbdd7172737475767778797a7b7c7d7ebbdd8182838485868788898a8b8c8d8ebbdd9192939495969798999a9b9c9d9ebbdda1a2a3a4a5a6a7a8a9aaabacadaebbddb1b2b3b4b5b6b7b8b9babbbcbdbebbddc1c2c3c4c5c6c7c8c9cacbcccdcebbddd1d2d3d4d5d6d7d8d9dadbdcdddebbdde1e2e3e4e5e6e7e8e9eaebecedeebbddeeeeeeeeeeeeeeeeeeeeeeeeeeeebb

Checksum: 538502

1. Checksum Calculation:
The function compute_checksum computes the checksum by iterating over each element in the memory array.

For each element, it generates random values for r_i and c_i, which are integers between 0 and 255 (you can adjust this range if necessary).

Add a simple checksum, we need to choose random values for each row (r_i) and column (c_i), and then calculate the checksum for the memory layout using the formula:

simple additional checksum to choose from random {r_i, c_i}
where the sum is \sum^{number_of_items} (modulus of same or number of columns)*r_i + c_i - (modulus of same or number of columns)

where modulus := number of columns.

2. Random Values for r_i and c_i:

The values for r_i and c_i are chosen randomly in the range 0 to 255, but you can adjust this to suit your needs.

3. Checksum Output: After generating the memory layout, the checksum is computed and printed at the end.

- The memory will be displayed in the format with addresses, similar to xxd -p.

- The checksum will be displayed at the end, providing a numeric validation for the content in the memory.

A checksum based on randomly selected values for r_i and c_i for each element in the memory array.

"""