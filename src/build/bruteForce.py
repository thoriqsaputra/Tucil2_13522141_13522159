import numpy as np

def bezier_curve_bf(points, iterations):
    iterations = pow(2, iterations)+1
    t = np.linspace(0, 1, iterations)
    t = t.tolist()
    curve = [[0 for _ in range(2)] for _ in range(iterations)]
    
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
    curve = np.array(curve)
    return curve