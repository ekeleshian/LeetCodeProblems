import math

def kClosest(points, K):
    """
    :type points: List[List[int]]
    :type K: int
    :rtype: List[List[int]]
    """
    distances = {}
    for idx, row in enumerate(points):
        answer = 0
        for num in row:
            answer += num**2
            distances[idx] = math.sqrt(answer)
    blah = sorted(distances.items(), key=lambda x: x[1])

    answer = blah[:K]
    soln = []
    for idx, dist in answer:
        soln.append(points[idx])
    return soln


print(kClosest([[1, 3], [-2, 2]], 1))