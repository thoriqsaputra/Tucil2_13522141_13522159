import numpy as np
import matplotlib.pyplot as plt
import time

def bezier_curve(points, iterations):
    
    # n = len(points) - 1
    # # Membuat nilai t dari 0 sampai 1 dengan jarak sepanjang iterasi
    # t = np.linspace(0, 1, iterations)
    # t = t.tolist()
    # # Membuat array 2D untuk menyimpan titik bezier curve
    # curve = [[0 for _ in range(2)] for _ in range(iterations)]
    
    # # Menghitung titik bezier curve
    # for i in range(iterations):
    #     for j in range(len(points)):
    #         curve[i][0] += ((1 - t[i]) ** (n - j)) * (t[i] ** j) * points[j][0]
    #         curve[i][1] += ((1 - t[i]) ** (n - j)) * (t[i] ** j) * points[j][1]
    # print(curve)
    # curve = np.array(curve)
    # return curve


    # Membuat nilai t dari 0 sampai 1 dengan jarak sepanjang iterasi
    time_start = time.time()
    t = np.linspace(0, 1, iterations)
    t = t.tolist()
    # Membuat array 2D untuk menyimpan titik bezier curve
    curve = [[0 for _ in range(2)] for _ in range(iterations)]
    
    # Menghitung titik bezier curve
    for i in range(iterations):
        curve[i][0] = (1-t[i])*((1-t[i])*points[0][0] + t[i]*points[1][0]) + t[i]*((1-t[i])*points[1][0] + t[i]*points[2][0])
        curve[i][1] = (1-t[i])*((1-t[i])*points[0][1] + t[i]*points[1][1]) + t[i]*((1-t[i])*points[1][1] + t[i]*points[2][1])
    time_end = time.time()
    print(f'Waktu eksekusi: {time_end - time_start} detik')
    curve = np.array(curve)
    return curve

def plot_bezier_curve(points, iterations):
    curve_points = bezier_curve(points, iterations)
    points = np.array(points)
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
        x = float(input(f'Masukan titik X{i}: '))
        y = float(input(f'Masukan titik Y{i}: '))
        points.append([x, y])

    iterations = int(input('Enter the number of iterations: '))
    plot_bezier_curve(points, iterations)

if __name__ == "__main__":
    main()
