import numpy as np
import matplotlib.pyplot as plt
import time

def midpoint(p0, p1):
    return [(p0[0]+p1[0])/2, (p0[1]+p1[1])/2]

def bezier_curve(points,iterations, isleft):
    if iterations == 0 and isleft == 0:
        points = [points[i] for i in range(len(points)) if i % 2 == 0]
        print('points')
        print(points)
        return points
    if iterations == 0 and isleft == 1:
        points = [points[i] for i in range(1,len(points)) if i % 2 == 0]
        print('points')
        print(points)
        return points
    else:
        new_points = []
        for i in range(len(points)-1):
            new_points.append(midpoint(points[i], points[i+1]))
        midpoints = []
        for i in range(len(new_points)-1):
            midpoints.append(midpoint(new_points[i], new_points[i+1]))
        new_array = []
        for i in range(len(new_points) + len(midpoints)):
            if i%2 == 0:
                new_array.append(new_points[int(i/2)])
            else:
                new_array.append(midpoints[int(i/2)])
        
        left = [points[0]]
        for i in range(len(new_array)//2+1):
            left.append(new_array[i])
        print('left')
        if iterations == 1 and isleft == 1:
            left.pop(0)
            left.pop(0)
        print(left)
        right = []
        for i in range(len(new_array)//2, len(new_array)):
            right.append(new_array[i])
        right.append(points[-1])
        print('right')
        print(right)

        return bezier_curve(left, iterations-1,0) + bezier_curve(right, iterations-1,1)
        
def plot_bezier_curve(points, iterations):
    curve_points = bezier_curve(points, iterations,0)
    curve_points = np.array(curve_points)
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
    points = [[3,1], [7,4], [5,7]]
    
    # num_points = int(input('Enter the number of control points: '))

    # for i in range(num_points):
    #     x = float(input(f'Masukan titik X{i}: '))
    #     y = float(input(f'Masukan titik Y{i}: '))
    #     points.append([x, y])

    iterations = int(input('Enter the number of iterations: '))
    plot_bezier_curve(points, iterations)

if __name__ == "__main__":
    main()