import collections
from random import choice

Card = collections.namedtuple('Card',['rank','suit'])

class FrenchDeck:
	ranks=[str(n) for n in range(2,11)]+list('JQKA')
	suits='spades diamonds clubs hearts'.split()
	
	def __init__(self):
		self._cards=[Card(rank,suit) for rank in self.ranks
									for suit in self.suits]
	def __len__(self):
		return len(self._cards)
	#实现了这个函数这个类变得可以迭代了
	def __getitem__(self,position):
		return self._cards[position]

	
	

def main():
	cards=FrenchDeck()
	#for c in reversed(cards):
		#print(c)

	#print(choice(cards))
	for card in sorted(cards,key=spades_high):
		print(card)

if __name__=="__main__":
	main()