from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

class CalcPrice:
    def calc_price(self,priceList):
        priceSumCt = sum(priceList) * 1.1
        return Decimal(str(priceSumCt)).quantize(Decimal('0'), rounding=ROUND_HALF_UP)