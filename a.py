import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class MobiusStrip:
    def __init__(self, R, w, n):
        self.R = R
        self.w = w
        self.n = n
        self.u = np.linspace(0, 2 * np.pi, n)
        self.v = np.linspace(-w / 2, w / 2, n)
        self.U, self.V = np.meshgrid(self.u, self.v)
        self.compute_surface()

    def compute_surface(self):
        U2 = self.U / 2
        self.X = (self.R + self.V * np.cos(U2)) * np.cos(self.U)
        self.Y = (self.R + self.V * np.cos(U2)) * np.sin(self.U)
        self.Z = self.V * np.sin(U2)

    def plot(self):
        fig = plt.figure(figsize=(10, 7))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(self.X, self.Y, self.Z, cmap='viridis', edgecolor='k', linewidth=0.1)
        ax.set_title('Möbius Strip')
        plt.show()

    def approximate_surface_area(self):
        du = 2 * np.pi / (self.n - 1)
        dv = self.w / (self.n - 1)
        U2 = self.U / 2

        dXdu = - (self.R + self.V * np.cos(U2)) * np.sin(self.U) - 0.5 * self.V * np.sin(U2) * np.cos(self.U)
        dYdu = (self.R + self.V * np.cos(U2)) * np.cos(self.U) - 0.5 * self.V * np.sin(U2) * np.sin(self.U)
        dZdu = 0.5 * self.V * np.cos(U2)

        dXdv = np.cos(U2) * np.cos(self.U)
        dYdv = np.cos(U2) * np.sin(self.U)
        dZdv = np.sin(U2)

        cross = np.sqrt((dYdu * dZdv - dZdu * dYdv) ** 2 +
                        (dZdu * dXdv - dXdu * dZdv) ** 2 +
                        (dXdu * dYdv - dYdu * dXdv) ** 2)

        return np.sum(cross) * du * dv

    def approximate_edge_length(self):
        u = self.u
        v = self.w / 2
        x = (self.R + v * np.cos(u / 2)) * np.cos(u)
        y = (self.R + v * np.cos(u / 2)) * np.sin(u)
        z = v * np.sin(u / 2)

        dx = np.gradient(x)
        dy = np.gradient(y)
        dz = np.gradient(z)

        return np.sum(np.sqrt(dx**2 + dy**2 + dz**2))

if __name__ == "__main__":
    try:
        R = float(input("Enter radius R (e.g., 1.0): "))
        w = float(input("Enter strip width w (e.g., 0.4): "))
        n = int(input("Enter resolution n (e.g., 300): "))
        
        strip = MobiusStrip(R, w, n)
        strip.plot()
        
        area = strip.approximate_surface_area()
        edge = strip.approximate_edge_length()
        
        print(f"\nApproximate Surface Area: {area:.4f}")
        print(f"Approximate Edge Length: {edge:.4f}")
    
    except Exception as e:
        print(f"Error: {e}")
