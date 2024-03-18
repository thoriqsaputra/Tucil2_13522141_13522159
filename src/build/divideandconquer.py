def midpoint(p0, p1):
    return [(p0[0]+p1[0])/2, (p0[1]+p1[1])/2]

def bezier_curve_dnc(points,iterations, isleft):
    if iterations == 0 and isleft == 0:
        points = [points[i] for i in range(len(points)) if i % 2 == 0]
        return points
    if iterations == 0 and isleft == 1:
        points = [points[i] for i in range(1,len(points)) if i % 2 == 0]
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
        if iterations == 1 and isleft == 1:
            left.pop(0)
            left.pop(0)
        right = []
        for i in range(len(new_array)//2, len(new_array)):
            right.append(new_array[i])
        right.append(points[-1])

        return bezier_curve_dnc(left, iterations-1,0) + bezier_curve_dnc(right, iterations-1,1)
    