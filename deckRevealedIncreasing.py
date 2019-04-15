from pdb import set_trace
import collections

"""
In a deck of cards, every card has a unique integer.  You can order the deck 
in any order you want.

Initially, all the cards start face down (unrevealed) in one deck.

Now, you do the following steps repeatedly, until all cards are revealed:

1. Take the top card of the deck, reveal it, and take it out of the deck.
2. If there are still cards in the deck, put the next top card of the deck at the 
   bottom of the deck.
   If there are still unrevealed cards, go back to step 1.  Otherwise, stop.
3. Return an ordering of the deck that would reveal the cards in increasing order.

The first entry in the answer is considered to be the top of the deck.

"""

def deckRevealedIncreasing(deck):
	# set_trace()
	N = len(deck)
	index = collections.deque(range(N))
	ans = [None]*N

	for card in sorted(deck):
		set_trace()
		ans[index.popleft()] = card
		if index:
			index.append(index.popleft())

	return ans


def deckRevealedIncreasing_2(deck):
	deck = sorted(deck)
	if len(deck) <= 1:
		return deck
	res = []
	start_pos = 0
	for idx in reversed(deck):
		if not res:
			res.append(idx)
			continue
		# set_trace()
		res.extend([res[start_pos], idx])
		start_pos +=1
	set_trace()
	return list(reversed(res[start_pos:]))


deck = [17, 13, 11, 2, 3, 5, 7]
deckRevealedIncreasing_2(deck)
set_trace()

