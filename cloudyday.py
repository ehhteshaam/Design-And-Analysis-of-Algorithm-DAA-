import math
import os
import random
import sys
import re
from collections import defaultdict

def maximumPeople(t, cloud_S, cloud_E):
    t = sorted(t)
    cloud_S = sorted(cloud_S)
    cloud_E = sorted(cloud_E)
    cloud_S_i = 0
    cloud_E_i = 0
    clds = set()
    d = defaultdict(int)
    free = 0
    for t_ind in range(len(t)):
        t_pos = t[t_ind][0]
        while cloud_S_i < len(cloud_S) and cloud_S[cloud_S_i][0] <= t_pos:
            clds.add(cloud_S[cloud_S_i][1])
            cloud_S_i += 1
        while cloud_E_i < len(cloud_E) and cloud_E[cloud_E_i][0] < t_pos:
            clds.remove(cloud_E[cloud_E_i][1])
            cloud_E_i += 1
        if len(clds) == 1:
            t[t_ind][2] = list(clds)[0]
            d[list(clds)[0]] += t[t_ind][1]
        elif len(clds) == 0:
            free += t[t_ind][1]
    return max(d.values(), default=0) + free

if __name__ == "__main__":
    n = int(input().strip())
    p = [int(x) for x in input().strip().split()]
    x = [int(x) for x in input().strip().split()]
    t = [[xi, pi, -1] for xi, pi in zip(x, p)]
    m = int(input().strip())
    y = [int(x) for x in input().strip().split()]
    r = [int(x) for x in input().strip().split()]
    cloud_S = [[y[i]-r[i], i] for i in range(m)]
    cloud_E = [[y[i]+r[i], i] for i in range(m)]
    result = maximumPeople(t, cloud_S, cloud_E)
    print(result)
