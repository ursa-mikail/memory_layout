#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define ROWS 16
#define COLUMNS 16
#define TOP_DEFINE 0xAA
#define BOTTOM_DEFINE 0xEE
#define LEFT_DEFINE 0xDD
#define RIGHT_DEFINE 0xBB

// Function to generate a random 8-byte hexadecimal starting address
unsigned long generate_random_hex_address() {
    unsigned long address = ((unsigned long)rand() << 32) | rand();
    return address;
}

// Function to simulate xxd -p output with memory addresses
void print_memory_with_addresses(unsigned char memory[ROWS][COLUMNS], unsigned long mem_start) {
    for (int i = 0; i < ROWS; i++) {
        printf("%08lX ", mem_start + (i * COLUMNS));
        for (int j = 0; j < COLUMNS; j++) {
            printf("%02X ", memory[i][j]);
        }
        printf("\n");
    }
}

// Function to simulate xxd -p output
void print_xxd_simulation(unsigned char memory[ROWS][COLUMNS]) {
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLUMNS; j++) {
            printf("%02x", memory[i][j]);
        }
    }
    printf("\n");
}

int main() {
    unsigned char memory[ROWS][COLUMNS];

    // Initialize memory array with incrementing hex values
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLUMNS; j++) {
            memory[i][j] = (i * COLUMNS + j) & 0xFF;
        }
    }

    // Apply defines
    for (int j = 0; j < COLUMNS; j++) {
        memory[0][j] = TOP_DEFINE;
        memory[ROWS - 1][j] = BOTTOM_DEFINE;
    }

    for (int i = 0; i < ROWS; i++) {
        memory[i][0] = LEFT_DEFINE;
        memory[i][COLUMNS - 1] = RIGHT_DEFINE;
    }

    // Generate a random 8-byte hexadecimal starting address
    srand(time(NULL));
    unsigned long mem_start = generate_random_hex_address();

    printf("Memory layout with addresses:\n");
    print_memory_with_addresses(memory, mem_start);

    printf("\nxxd -p simulation:\n");
    print_xxd_simulation(memory);

    // Optionally, slice the output from the random starting address
    int starting_index = rand() % (ROWS * COLUMNS);
    printf("\nxxd -p output from random starting address:\n");
    for (int i = starting_index; i < ROWS * COLUMNS; i++) {
        printf("%02x", memory[i / COLUMNS][i % COLUMNS]);
    }
    printf("\n");

    return 0;
}


/*
Memory layout with addresses:
2FF9FD166AF85968 DD AA AA AA AA AA AA AA AA AA AA AA AA AA AA BB 
2FF9FD166AF85978 DD 11 12 13 14 15 16 17 18 19 1A 1B 1C 1D 1E BB 
2FF9FD166AF85988 DD 21 22 23 24 25 26 27 28 29 2A 2B 2C 2D 2E BB 
2FF9FD166AF85998 DD 31 32 33 34 35 36 37 38 39 3A 3B 3C 3D 3E BB 
2FF9FD166AF859A8 DD 41 42 43 44 45 46 47 48 49 4A 4B 4C 4D 4E BB 
2FF9FD166AF859B8 DD 51 52 53 54 55 56 57 58 59 5A 5B 5C 5D 5E BB 
2FF9FD166AF859C8 DD 61 62 63 64 65 66 67 68 69 6A 6B 6C 6D 6E BB 
2FF9FD166AF859D8 DD 71 72 73 74 75 76 77 78 79 7A 7B 7C 7D 7E BB 
2FF9FD166AF859E8 DD 81 82 83 84 85 86 87 88 89 8A 8B 8C 8D 8E BB 
2FF9FD166AF859F8 DD 91 92 93 94 95 96 97 98 99 9A 9B 9C 9D 9E BB 
2FF9FD166AF85A08 DD A1 A2 A3 A4 A5 A6 A7 A8 A9 AA AB AC AD AE BB 
2FF9FD166AF85A18 DD B1 B2 B3 B4 B5 B6 B7 B8 B9 BA BB BC BD BE BB 
2FF9FD166AF85A28 DD C1 C2 C3 C4 C5 C6 C7 C8 C9 CA CB CC CD CE BB 
2FF9FD166AF85A38 DD D1 D2 D3 D4 D5 D6 D7 D8 D9 DA DB DC DD DE BB 
2FF9FD166AF85A48 DD E1 E2 E3 E4 E5 E6 E7 E8 E9 EA EB EC ED EE BB 
2FF9FD166AF85A58 DD EE EE EE EE EE EE EE EE EE EE EE EE EE EE BB 

xxd -p simulation:
ddaaaaaaaaaaaaaaaaaaaaaaaaaaaabbdd1112131415161718191a1b1c1d1ebbdd2122232425262728292a2b2c2d2ebbdd3132333435363738393a3b3c3d3ebbdd4142434445464748494a4b4c4d4ebbdd5152535455565758595a5b5c5d5ebbdd6162636465666768696a6b6c6d6ebbdd7172737475767778797a7b7c7d7ebbdd8182838485868788898a8b8c8d8ebbdd9192939495969798999a9b9c9d9ebbdda1a2a3a4a5a6a7a8a9aaabacadaebbddb1b2b3b4b5b6b7b8b9babbbcbdbebbddc1c2c3c4c5c6c7c8c9cacbcccdcebbddd1d2d3d4d5d6d7d8d9dadbdcdddebbdde1e2e3e4e5e6e7e8e9eaebecedeebbddeeeeeeeeeeeeeeeeeeeeeeeeeeeebb

xxd -p output from random starting address:
3c3d3ebbdd4142434445464748494a4b4c4d4ebbdd5152535455565758595a5b5c5d5ebbdd6162636465666768696a6b6c6d6ebbdd7172737475767778797a7b7c7d7ebbdd8182838485868788898a8b8c8d8ebbdd9192939495969798999a9b9c9d9ebbdda1a2a3a4a5a6a7a8a9aaabacadaebbddb1b2b3b4b5b6b7b8b9babbbcbdbebbddc1c2c3c4c5c6c7c8c9cacbcccdcebbddd1d2d3d4d5d6d7d8d9dadbdcdddebbdde1e2e3e4e5e6e7e8e9eaebecedeebbddeeeeeeeeeeeeeeeeeeeeeeeeeeeebb


*/