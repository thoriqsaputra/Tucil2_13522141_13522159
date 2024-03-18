import numpy as np
import matplotlib.pyplot as plt
import time

def midpoint(p0, p1):
    return [(p0[0]+p1[0])/2, (p0[1]+p1[1])/2]

# def divide(points):
#         new_points = []
#         for i in range(len(points)-1):
#             new_points.append(midpoint(points[i], points[i+1]))
#         midpoints = []
#         for i in range(len(new_points)-1):
#             midpoints.append(midpoint(new_points[i], new_points[i+1]))
#         new_array = []
#         for i in range(len(new_points) + len(midpoints)):
#             if i%2 == 0:
#                 new_array.append(new_points[int(i/2)])
#             else:
#                 new_array.append(midpoints[int(i/2)])
        
#         left = [points[0]]
#         for i in range(len(new_array)//2+2):
#             left.append(new_array[i])
#         right = []
        
#         for i in range(len(new_array)//2-1, len(new_array)):
#             right.append(new_array[i])
#         right.append(points[-1])
#         return left, right

# def bazier_curveleft(points, iterations, isleft):
#     if iterations == 0 and isleft == 0:
#         points = [points[i] for i in range(len(points)-1) if i % 2 == 0]
#         print('left points')
#         print(points)
#         return points
#     elif iterations == 0 and isleft == 1:
#         points = [points[i] for i in range(1,len(points)) if i % 2 == 0]
#         print('right points')
#         print(points)
#         return points
#     else:
#         new_points = []
#         for i in range(len(points)-1):
#             new_points.append(midpoint(points[i], points[i+1]))
#         midpoints = []
#         for i in range(len(new_points)-1):
#             midpoints.append(midpoint(new_points[i], new_points[i+1]))
#         new_array = []
#         for i in range(len(new_points) + len(midpoints)):
#             if i%2 == 0:
#                 new_array.append(new_points[int(i/2)])
#             else:
#                 new_array.append(midpoints[int(i/2)])
        
#         left = [points[0]]
#         for i in range(len(new_array)//2+2):
#             left.append(new_array[i])
#         print('left')
#         print(left)
#         right = []
        
#         for i in range(len(new_array)//2-1, len(new_array)):
#             right.append(new_array[i])
#         right.append(points[-1])
#         print('right')
#         print(right)
    
#     return bazier_curveleft(left, iterations-1,0) + bazier_curveleft(right, iterations-1,1) 

# def bazier_curveright(points, iterations, isleft):
#     if iterations == 0 and isleft == 0:
#         points = [points[i] for i in range(len(points)-1) if i % 2 == 1]
#         print('right points')
#         print(points)
#         return points
#     elif iterations == 0 and isleft == 1:
#         points = [points[i] for i in range(1,len(points)) if i % 2 == 1]
#         print('left points')
#         print(points)
#         return points
#     else:
#         new_points = []
#         for i in range(len(points)-1):
#             new_points.append(midpoint(points[i], points[i+1]))
#         midpoints = []
#         for i in range(len(new_points)-1):
#             midpoints.append(midpoint(new_points[i], new_points[i+1]))
#         new_array = []
#         for i in range(len(new_points) + len(midpoints)):
#             if i%2 == 0:
#                 new_array.append(new_points[int(i/2)])
#             else:
#                 new_array.append(midpoints[int(i/2)])
        
#         left = [points[0]]
#         for i in range(len(new_array)//2+2):
#             left.append(new_array[i])
#         print('left')
#         print(left)
#         right = []
        
#         for i in range(len(new_array)//2-1, len(new_array)):
#             right.append(new_array[i])
#         right.append(points[-1])
#         print('right')
#         print(right)
    
#     return bazier_curveright(left, iterations-1,0) + bazier_curveright(right, iterations-1,1)

def bezier_curve(points,iterations, isleft,iter):
    if iterations == 0 and isleft == 0:
        points = [points[i] for i in range(len(points)) if i % 2 == 0]
        print('points')
        print(points)
        return points
    elif iterations == 0 and isleft == 1:
        points = [points[i] for i in range(2,len(points)) if i % 2 == 0]
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
        print('iterasi ke', iter)
        for i in range(len(new_points) + len(midpoints)):
            if i%2 == 0:
                new_array.append(new_points[int(i/2)])
            else:
                new_array.append(midpoints[int(i/2)])
        left =[]
        if isleft == 0:
            left = [points[0]]
        for i in range(len(new_array)//2+2):
            left.append(new_array[i]) 
        if isleft == 1:
            left.pop(0)
        print('left')
        print(left)
        right = []
        
        for i in range(len(new_array)//2-1, len(new_array)):
            right.append(new_array[i])
        if iter >0: 
            right.pop(0)
        right.append(points[-1])
        print('right')
        print(right)

        return bezier_curve(left, iterations-1,0,iter+1) + bezier_curve(right, iterations-1,1,iter+1)
        
def plot_bezier_curve(points, iterations):
    curve_points = bezier_curve(points, iterations, 0,0)
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
    points = [[3,1],[7,4],[5,7],[2,6]]
    
    # num_points = int(input('Enter the number of control points: '))

    # for i in range(num_points):
    #     x = float(input(f'Masukan titik X{i}: '))
    #     y = float(input(f'Masukan titik Y{i}: '))
    #     points.append([x, y])

    iterations = int(input('Enter the number of iterations: '))
    plot_bezier_curve(points, iterations)

if __name__ == "__main__":
    main()