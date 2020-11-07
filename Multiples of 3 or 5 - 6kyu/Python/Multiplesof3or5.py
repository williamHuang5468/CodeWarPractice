class Multiplesof3or5(object):
    def solution(self, number):
        if (number < 0): return 0
        factorList = []
        for i in range(1, number):
            if i % 3 == 0:
                factorList.append(i)
            elif i % 5 == 0:
                factorList.append(i)
            else:
                continue
        return sum(i for i in factorList)