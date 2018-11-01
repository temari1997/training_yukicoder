import collections
hand = list(input().split())
duplicate = collections.Counter(hand)
#print(sorted(duplicate.values()))

if sorted(duplicate.values()) == [1,1,1,1,1]:
    yaku = ("NO HAND")
elif sorted(duplicate.values()) == [1,1,1,2]:
    yaku = ("ONE PAIR")
elif sorted(duplicate.values()) == [1,2,2]:
    yaku = ("TWO PAIR")
elif sorted(duplicate.values()) == [1,1,3]:
    yaku = ("THREE CARD")
elif sorted(duplicate.values()) == [2,3]:
    yaku = ("FULL HOUSE")
else :
    yaku = ("NO HAND")
print(yaku)
