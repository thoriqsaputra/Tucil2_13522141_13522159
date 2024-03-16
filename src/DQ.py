import numpy as np
import matplotlib.pyplot as plt

def midpoint(p1, p2):
    return [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]

def bezier_curve(control_points, iterations):
    if iterations == 0:
        return control_points
    else:
        temp = []
        for i in range(len(control_points) - 1):
            temp.append(midpoint(control_points[i], control_points[i+1]))
        print(temp)
        while len(temp) > 1:
            temp = [midpoint(temp[i], temp[i+1]) for i in range(len(temp) - 1)]
        new_points = []
        new_points.append(control_points[0])
        new_points.extend(temp)
        new_points.append(control_points[-1])
        return bezier_curve(new_points, iterations - 1)

def plot_curve(control_points, iterations):
    curve_points = bezier_curve(control_points, iterations)
    bc = []
    bc.append(control_points[0])
    bc.extend(curve_points)
    bc.append(control_points[-1])
    bc = np.array(bc)
    print(curve_points)
    plt.plot(control_points[:, 0], control_points[:, 1], 'ro-', label='Control Points')
    plt.plot(bc[:, 0], bc[:, 1], 'bo-', label=f'Bezier Curve ({iterations} iterations)')
    plt.title('Bezier Curve')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()

# Example control points
control_points = np.array([[0, 0], [1, 3], [2, -1]])

# Number of iterations
iterations = 1

# Plot the curve
plot_curve(control_points, iterations)
