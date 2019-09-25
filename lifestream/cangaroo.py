
def sign(number):
    if number >= 0:
        return '+'
    return '-'


def test_run(x1, v1, x2, v2):
    while True:
        diff = x1 - x2
        x1 += v1
        x2 += v2
        diff2 = x1 - x2
        
        if diff2 == 0:
            return 'YES'
        if abs(diff) <= abs(diff2) or sign(diff) != sign(diff2):
            return 'NO'


if __name__ == '__main__':
    print(test_run(0, 3, 4, 2))
    print(test_run(0, 2, 5, 3))
