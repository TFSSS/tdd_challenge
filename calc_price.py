from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

class Calc_Price:
    def __init__(self,inputtxt):
        self._inputtxt = inputtxt

    def calc_price(self):
        for line in self._inputtxt.readlines():
            prices = line.split(",")
            priceSumCt = sum(prices) * 1.1
            priceSumCt = Decimal(str(priceSumCt)).quantize(Decimal('0'), rounding=ROUND_HALF_UP)
            print(priceSumCt)

if __name__ == '__main__':
    # 本番はこんな感じで使うことを想定
    kvs = SomeKVSUsingDynamoDB()
    my_memory = MyMemory(kvs)
    my_memory.set_favorite('ボルダリング')
    print(my_memory.get_favorite())