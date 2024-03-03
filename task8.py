from collections import UserList


class AmountPaymentList(UserList):
    def amount_payment(self):
        return sum(map(lambda x: int(x) if x > 0 else 0, self.data))


payment = AmountPaymentList([1, -3, 4])
print(payment.amount_payment())
        