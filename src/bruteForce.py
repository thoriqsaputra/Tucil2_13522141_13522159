import numpy as np
import matplotlib.pyplot as plt
import time

def bezier_curve(points, iterations):

    # Membuat nilai t dari 0 sampai 1 dengan jarak sepanjang iterasi
    time_start = time.time()
    t = np.linspace(0, 1, iterations)
    t = t.tolist()
    # Membuat array 2D untuk menyimpan titik bezier curve
    curve = [[0 for _ in range(2)] for _ in range(iterations)]
    
    # Menghitung titik bezier curve
    for i in range(iterations):
        Qx = []
        Qy = []
        for j in range(len(points) - 1):
            tempx = (1-t[i])*points[j][0] + t[i]*points[j+1][0]
            tempy = (1-t[i])*points[j][1] + t[i]*points[j+1][1]
            Qx.append(tempx)
            Qy.append(tempy)
        while len(Qx) > 1:
            Rx = []
            Ry = []
            for j in range(len(Qx) - 1):
                tempx = (1-t[i])*(Qx[j]) + t[i]*(Qx[j+1])
                tempy = (1-t[i])*(Qy[j]) + t[i]*(Qy[j+1])
                Rx.append(tempx)
                Ry.append(tempy)
            Qx = Rx
            Qy = Ry
        curve[i][0] = Qx[0]
        curve[i][1] = Qy[0]
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
    
    num_points = int(input('Enter the number of control points: '))

    for i in range(num_points):
        x = float(input(f'Masukan titik X{i}: '))
        y = float(input(f'Masukan titik Y{i}: '))
        points.append([x, y])

    iterations = int(input('Enter the number of iterations: '))
    plot_bezier_curve(points, iterations)

if __name__ == "__main__":
    main()
