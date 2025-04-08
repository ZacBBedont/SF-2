from __future__ import annotations
from functools import total_ordering

@total_ordering
class Account:
    def __init__(self,gold):
        '''
        create account with "gold" gold
        '''
        self.gold = gold
    def addGold(self,amount:int):
        self.gold += amount
    def zeroGold(self):
        self.gold = 0
    def doubleGold(self):
        self.gold *= 2
    def __lt__(self,other_acc:Account) -> bool:
        '''
        return true if account and other account is of the same type and gold of account is less than gold of other
        '''
        return isinstance(other_acc,Account) and self.gold < other_acc.gold
    def __eq__(self,other_acc:Account) -> bool:
        return isinstance(other_acc,Account) and other_acc.gold == self.gold
    def __repr__(self):
        return f'gold in account: {self.gold}'
###################
acc1 = Account(500)
acc2 = Account(500)
acc3 = Account(56)
acc4 = Account(34)
value = 500

print(acc1)
print(acc4 < acc3)
print(acc1 < acc4)
print(acc1 == acc3)
print(acc1 == acc2)
print(acc1 == value)
print()
print(acc1 > acc3)
print(acc1 > acc2)
print(acc1 >= acc2)

