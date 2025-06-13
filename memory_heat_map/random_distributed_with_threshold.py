import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameters
N = 20  # smaller grid size for better visibility
iterations = 1000  # more iterations to get meaningful frequencies

# Simulate filling the grid
grid_counts = np.zeros((N, N), dtype=int)

for _ in range(iterations):
    i, j = np.random.randint(0, N, size=2) 
    grid_counts[i, j] += 1

# Normalize to get frequency percentage
expected_per_cell = iterations / (N * N)
grid_freq = (grid_counts / expected_per_cell) * 100  # percentage relative to expected

print(f"Grid size: {N}x{N}")
print(f"Iterations: {iterations}")
print(f"Expected hits per cell: {expected_per_cell:.1f}")
print(f"Frequency range: {grid_freq.min():.1f}% - {grid_freq.max():.1f}%")

# Create figure with subplots
fig = plt.figure(figsize=(16, 8))

# 3D Plot (rotatable)
ax1 = fig.add_subplot(121, projection='3d')

x, y = np.meshgrid(np.arange(N), np.arange(N))
surface = ax1.plot_surface(x, y, grid_freq, cmap='viridis', alpha=0.8)
ax1.set_title("3D Frequency Surface (Click and drag to rotate)")
ax1.set_xlabel('X Position')
ax1.set_ylabel('Y Position')
ax1.set_zlabel('Frequency (% of expected)')

# Add colorbar for 3D plot
fig.colorbar(surface, ax=ax1, shrink=0.5, aspect=5)

# 2D Color Mapping
color_map = np.zeros((N, N, 3))

# Count cells in each category for statistics
black_count = blue_count = white_count = red_count = 0

for i in range(N):
    for j in range(N):
        val = grid_freq[i, j]
        if val < 5:
            color_map[i, j] = [0, 0, 0]  # black
            black_count += 1
        elif 5 <= val < 85:
            color_map[i, j] = [0, 0, 1]  # blue
            blue_count += 1
        elif 85 <= val < 95:
            color_map[i, j] = [1, 1, 1]  # white
            white_count += 1
        else:
            color_map[i, j] = [1, 0, 0]  # red
            red_count += 1

# 2D Plot
ax2 = fig.add_subplot(122)
im = ax2.imshow(color_map, origin='lower', extent=[0, N, 0, N])
ax2.set_title("2D Frequency Color Map")
ax2.set_xlabel('X Position')
ax2.set_ylabel('Y Position')

# Add legend for color coding
legend_text = f"""Color Legend:
Black: < 5% ({black_count} cells)
Blue: 5-85% ({blue_count} cells)  
White: 85-95% ({white_count} cells)
Red: > 95% ({red_count} cells)"""

ax2.text(1.02, 0.5, legend_text, transform=ax2.transAxes, 
         verticalalignment='center', bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgray"))

plt.tight_layout()
plt.show()

# Print some statistics
print(f"\nColor distribution:")
print(f"Black (< 5%): {black_count} cells")
print(f"Blue (5-85%): {blue_count} cells")
print(f"White (85-95%): {white_count} cells")
print(f"Red (> 95%): {red_count} cells")

"""
Grid size: 20x20
Iterations: 1000
Expected hits per cell: 2.5
Frequency range: 0.0% - 320.0%


Color distribution:
Black (< 5%): 32 cells
Blue (5-85%): 189 cells
White (85-95%): 0 cells
Red (> 95%): 179 cells
"""