import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.stats import multivariate_normal

# Parameters
N = 30  # grid size
iterations = 200000  # more iterations for better patterns

# Reset grid
grid_counts = np.zeros((N, N), dtype=int)

# Define Gaussian clusters with coordinates that fit our grid
clusters = [
    {"mean": [8, 8], "cov": [[8, 0], [0, 8]], "weight": 0.35},      # cluster in lower left
    {"mean": [22, 22], "cov": [[12, 0], [0, 12]], "weight": 0.35},   # cluster in upper right  
    {"mean": [15, 5], "cov": [[6, 0], [0, 6]], "weight": 0.2},      # cluster in lower center
    {"mean": [5, 20], "cov": [[4, 0], [0, 4]], "weight": 0.1}       # small cluster in upper left
]

print(f"Grid size: {N}x{N}")
print(f"Iterations: {iterations}")
print("Cluster centers:", [cluster["mean"] for cluster in clusters])

# Create a probability map using the Gaussian clusters
prob_map = np.zeros((N, N))
x, y = np.meshgrid(np.arange(N), np.arange(N))
pos = np.dstack((x, y))

for i, cluster in enumerate(clusters):
    rv = multivariate_normal(mean=cluster["mean"], cov=cluster["cov"])
    cluster_prob = cluster["weight"] * rv.pdf(pos)
    prob_map += cluster_prob
    print(f"Cluster {i+1} max probability: {cluster_prob.max():.6f}")

# Normalize to make it a probability distribution
prob_map /= np.sum(prob_map)
print(f"Probability map sum: {np.sum(prob_map):.6f}")
print(f"Max probability: {prob_map.max():.6f}")

# Use the probability map to choose grid cells
flat_indices = np.random.choice(N*N, size=iterations, p=prob_map.ravel())
for idx in flat_indices:
    i, j = divmod(idx, N)
    grid_counts[i, j] += 1

# Calculate frequency as percentage of total iterations
grid_freq = (grid_counts / iterations) * 100  # absolute percentage
print(f"Frequency range: {grid_freq.min():.3f}% - {grid_freq.max():.3f}%")

# Create figure with subplots
fig = plt.figure(figsize=(18, 8))

# 3D Plot (rotatable)
ax1 = fig.add_subplot(131, projection='3d')
surface = ax1.plot_surface(x, y, grid_freq, cmap='plasma', alpha=0.9)
ax1.set_title("3D Frequency Surface\n(Gaussian Clusters)")
ax1.set_xlabel('X Position')
ax1.set_ylabel('Y Position') 
ax1.set_zlabel('Frequency (%)')
ax1.view_init(elev=30, azim=45)  # Better initial viewing angle

# Add colorbar for 3D plot
fig.colorbar(surface, ax=ax1, shrink=0.6, aspect=10)

# 2D Color Mapping with the original thresholds
color_map = np.zeros((N, N, 3))
black_count = blue_count = white_count = red_count = 0

for i in range(N):
    for j in range(N):
        val = grid_freq[i, j]
        if val < 0.05:  # adjusted threshold for absolute percentage
            color_map[i, j] = [0, 0, 0]  # black
            black_count += 1
        elif 0.05 <= val < 0.5:  # adjusted threshold  
            color_map[i, j] = [0, 0, 1]  # blue
            blue_count += 1
        elif 0.5 <= val < 1.0:  # adjusted threshold
            color_map[i, j] = [1, 1, 1]  # white
            white_count += 1
        else:
            color_map[i, j] = [1, 0, 0]  # red
            red_count += 1

# 2D Plot
ax2 = fig.add_subplot(132)
im = ax2.imshow(color_map, origin='lower', extent=[0, N, 0, N])
ax2.set_title("2D Frequency Color Map\n(Gaussian Clusters)")
ax2.set_xlabel('X Position')
ax2.set_ylabel('Y Position')

# Add cluster centers as markers
for i, cluster in enumerate(clusters):
    ax2.plot(cluster["mean"][0], cluster["mean"][1], 'yo', markersize=8, 
             markeredgecolor='black', label=f'Cluster {i+1}')
ax2.legend()

# Add a third plot showing the underlying probability map
ax3 = fig.add_subplot(133)
prob_plot = ax3.imshow(prob_map, origin='lower', extent=[0, N, 0, N], cmap='viridis')
ax3.set_title("Underlying Probability Map")
ax3.set_xlabel('X Position')
ax3.set_ylabel('Y Position')
fig.colorbar(prob_plot, ax=ax3, shrink=0.6)

# Add cluster centers to probability map too
for i, cluster in enumerate(clusters):
    ax3.plot(cluster["mean"][0], cluster["mean"][1], 'ro', markersize=6, 
             markeredgecolor='white')

plt.tight_layout()

# Print statistics
print(f"\nColor distribution (adjusted thresholds):")
print(f"Black (< 0.05%): {black_count} cells")
print(f"Blue (0.05-0.5%): {blue_count} cells")
print(f"White (0.5-1.0%): {white_count} cells") 
print(f"Red (> 1.0%): {red_count} cells")

# Show some high-frequency cells
high_freq_cells = np.where(grid_freq > 0.5)
if len(high_freq_cells[0]) > 0:
    print(f"\nHigh frequency cells (> 0.5%):")
    for i, j in zip(high_freq_cells[0][:5], high_freq_cells[1][:5]):  # show first 5
        print(f"  Cell ({i},{j}): {grid_freq[i,j]:.3f}%")

plt.show()

"""
Grid size: 30x30
Iterations: 200000
Cluster centers: [[8, 8], [22, 22], [15, 5], [5, 20]]
Cluster 1 max probability: 0.006963
Cluster 2 max probability: 0.004642
Cluster 3 max probability: 0.005305
Cluster 4 max probability: 0.003979
Probability map sum: 1.000000
Max probability: 0.007104
Frequency range: 0.000% - 0.714%

Color distribution (adjusted thresholds):
Black (< 0.05%): 470 cells
Blue (0.05-0.5%): 404 cells
White (0.5-1.0%): 26 cells
Red (> 1.0%): 0 cells

High frequency cells (> 0.5%):
  Cell (5,14): 0.528%
  Cell (5,15): 0.523%
  Cell (6,7): 0.509%
  Cell (6,8): 0.564%
  Cell (6,9): 0.582%
"""