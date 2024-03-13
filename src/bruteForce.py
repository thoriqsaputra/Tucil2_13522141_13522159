import numpy as np
import matplotlib.pyplot as plt

def bezier_curve(points, iterations):
    n = len(points) - 1
    # Membuat nilai t dari 0 sampai 1 dengan jarak sepanjang iterasi
    # contoh : [0. 0.11111111 0.22222222 0.33333333 0.44444444 0.55555556 0.66666667 0.77777778 0.88888889 1.]
    t = np.linspace(0, 1, iterations)
    
    # Membuat array 2D dengan ukuran (iterasi, 2) yang berisi nilai 0
    # iterasi merepresentasikan jumlah titik yang akan dihitung
    curve = np.zeros((iterations, 2))
    
    # Menghitung titik bezier curve
    for i in range(iterations):
        for j in range(n + 1):
            curve[i] += np.multiply(points[j], (1 - t[i]) ** (n - j) * t[i] ** j)
    return curve

def plot_bezier_curve(points, iterations):
    curve_points = bezier_curve(points, iterations)
    plt.plot(curve_points[:,0], curve_points[:,1], label='Bezier Curve', color='blue')
    plt.scatter(points[:,0], points[:,1], label='Control Points', color='red')
    plt.legend()
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Bezier Curve Visualization')
    plt.grid(True)
    plt.show()

def main():
    points = []
    num_points = 3

    for i in range(num_points):
        x = float(input(f'Enter x-coordinate for point {i+1}: '))
        y = float(input(f'Enter y-coordinate for point {i+1}: '))
        points.append([x, y])

    iterations = int(input('Enter the number of iterations: '))

    bezier_curve(np.array(points), iterations)

if __name__ == "__main__":
    main()
