class ProductOfNumbers:

    def __init__(self):
        self.prefix = [1]   # prefix[i] = product of the last i numbers since the latest zero

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix = [1]          # everything before a zero is cut off
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix):      # the last k numbers include a zero
            return 0
        return self.prefix[-1] // self.prefix[-1 - k]