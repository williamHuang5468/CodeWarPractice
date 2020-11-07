class Multiplesof3or5(object):
    def solution(self, number):
        if (number < 0): return 0
        multiples3 = set(i for i in range(3, number, 3))
        multiples5 = set(i for i in range(5, number, 5))
        return sum((multiples3 | multiples5))