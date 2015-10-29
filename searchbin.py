def search_binary(xs, target):
    lb = 0
    ub = len(xs)
    
    while True:
        if lb == ub:
            return -1
        mid = (lb + up) // 2
        miditem = xs[mid]
        
        if miditem == target:
            return mid
        if miditem < target:
            lb = mid + 1
        else:
            ub = mid


def main():
    xs = [2,3,5,7,11,13,17,23,29,31,37,43,47,53]
    test(search_binary(xs, 20) == -1)
    test(search_binary(xs, 99) == -1)
    test(search_binary(xs, 1) == -1)
    for (i, v) in enumerate(xs):
        test(search_binary(xs, v) == i)
