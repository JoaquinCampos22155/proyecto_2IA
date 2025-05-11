import matplotlib.pyplot as plt

def plot_maze(maze):
    plt.imshow(maze.grid, cmap='binary')
    plt.title('Laberinto')
    plt.axis('off')

def plot_explored(maze, explored, show=True, save_path=None):
    plot_maze(maze)
    ys, xs = zip(*explored)
    plt.scatter(xs, ys, s=1, label='Explorados')
    plt.legend()
    if save_path: plt.savefig(save_path, bbox_inches='tight')
    if show: plt.show()
    plt.clf()

def plot_path(maze, path, show=True, save_path=None):
    plot_maze(maze)
    ys, xs = zip(*path)
    plt.plot(xs, ys, linewidth=1, label='Camino')
    plt.legend()
    if save_path: plt.savefig(save_path, bbox_inches='tight')
    if show: plt.show()
    plt.clf()
