

import heapq


if __name__ == '__main__':
    h = [1,3,2,4]
    heapq.heapify(h)
    n = heapq.nlargest(2,h)
    print(n)