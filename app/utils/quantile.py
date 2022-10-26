import math


class Quantile:
    def __init__(self, arr=[], percentile=1):
        self.arr = arr
        self.percentile = percentile
        self.arr.sort()

    """
    R‑1, SAS‑3, Maple‑1 based on rounding
    """

    def r1(self):
        if self.percentile == 100:
            return self.arr[-1]
        n = len(self.arr)
        h = n * self.percentile / 100.0
        return self.arr[int(h)]

    """
    R‑2, SAS‑5, Maple‑2, Stata based on rounding
    """

    def r2(self):
        n = len(self.arr)
        h = n * self.percentile / 100.0 + 0.5
        return self.arr[int(h - 0.5)] * 0.5 + self.arr[int(h + 0.5)] * 0.5

    """
    R‑3, SAS‑2 based on rounding
    """

    def r3(self):
        n = len(self.arr)
        h = n * self.percentile / 100.0 - 0.5
        return self.arr[int(h)]

    """
    The P2 Algorithm for Dynamic Statistical Computing Calculation of Quantiles and
    Robert G. Sargent Editor Histograms Without Storing Observations
    """

    def p2(self):
        estimator = P2QuantileEstimator(self.percentile)
        for value in self.arr:
            estimator.add_value(value)

        return estimator.get_quantile()


class P2QuantileEstimator:
    def __init__(self, percentile):
        self.p = percentile / 100.0
        self.n = [0] * 5
        self.ns = [0] * 5
        self.q = [0] * 5
        self.count = 0

    def add_value(self, x):
        if self.count < 5:
            self.count += 1
            self.q[self.count] = x
            if self.count == 5:
                self.q.sort()
                self.n = [0, 1, 2, 3, 4]

                self.ns[0] = 0
                self.ns[1] = 2 * self.p
                self.ns[2] = 4 * self.p
                self.ns[3] = 2 + 2 * self.p
                self.ns[4] = 4

        k = 3
        if x < self.q[0]:
            self.q[0] = x
            k = 0
        elif x < self.q[1]:
            k = 0
        elif x < self.q[2]:
            k = 1
        elif x < self.q[3]:
            k = 2
        elif x < self.q[4]:
            k = 3
        else:
            self.q[4] = x

        for i in range(k + 1, 5):
            self.n[i] += 1

        self.ns[1] = self.count * self.p / 2
        self.ns[2] = self.count * self.p
        self.ns[3] = self.count * (1 + self.p) / 2
        self.ns[4] = self.count

        for i in range(1, 4):
            d = self.ns[i] - self.n[i]
            if (d >= 1) and (self.n[i + 1] - self.n[i] > 1) or (d <= -1) and (self.n[i - 1] - self.n[i] < -1):
                sign = lambda v: math.copysign(1, v)
                d_int = sign(d)
                qs = self.parabolic(i, d_int)
                if self.q[i - 1] < qs < self.q[i + 1]:
                    self.q[i] = qs
                else:
                    self.q[i] = self.linear(i, d_int)
                self.n[i] += d_int
        self.count += 1

    def parabolic(self, i, d):
        return self.q[i] + d / (self.n[i + 1] - self.n[i - 1]) * (
                (self.n[i] - self.n[i - 1] + d) * (self.q[i + 1] - self.q[i]) / (self.n[i + 1] - self.n[i]) +
                (self.n[i + 1] - self.n[i] - d) * (self.q[i] -
                                                   self.q[i - 1]) / (self.n[i] - self.n[i - 1])
        )

    def linear(self, i, d):
        return self.q[i] + d * (self.q[i + d] - self.q[i]) / (self.n[i + d] - self.n[i])

    def get_quantile(self):
        if self.count == 0:
            return 0
        if self.count <= 5:
            self.q.sort()
            index = int((self.count - 1) * p)
            return self.q[index]
        return self.q[2]
