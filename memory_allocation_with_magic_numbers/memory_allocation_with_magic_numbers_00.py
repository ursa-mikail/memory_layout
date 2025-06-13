import random

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

# Function to simulate xxd -p output
def xxd_p_simulation(memory):
    hex_stream = ''
    for row in memory:
        for value in row:
            hex_stream += value
    return hex_stream.lower()

# Random starting address
starting_index = random.randint(0, rows * columns - 1)
print(f"Starting index: {starting_index}")

# Print the memory layout
for row in memory:
    print(' '.join(row))

# Simulate xxd -p output
xxd_output = xxd_p_simulation(memory)
print("\nxxd -p simulation:")
print(xxd_output)

# Optionally, slice the output from the random starting address
print("\nxxd -p output from random starting address:")
print(xxd_output[starting_index*2:])  # *2 because each hex value is 2 characters


"""
Starting index: 24
dd AA AA AA AA AA AA AA AA AA AA AA AA AA AA bb
dd 11 12 13 14 15 16 17 18 19 1A 1B 1C 1D 1E bb
dd 21 22 23 24 25 26 27 28 29 2A 2B 2C 2D 2E bb
dd EE EE EE EE EE EE EE EE EE EE EE EE EE EE bb

xxd -p simulation:
ddaaaaaaaaaaaaaaaaaaaaaaaaaaaabbdd1112131415161718191a1b1c1d1ebbdd2122232425262728292a2b2c2d2ebbddeeeeeeeeeeeeeeeeeeeeeeeeeeeebb

xxd -p output from random starting address:
18191a1b1c1d1ebbdd2122232425262728292a2b2c2d2ebbddeeeeeeeeeeeeeeeeeeeeeeeeeeeebb

"""