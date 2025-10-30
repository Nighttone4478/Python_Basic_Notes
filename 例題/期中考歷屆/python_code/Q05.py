def card_to_point(card):
    if card == 'A': return 1
    elif card == 'J': return 11
    elif card == 'Q': return 12
    elif card == 'K': return 13
    else: return int(card)

def iscontinue(points):
    points = sorted(points)
    
    if 1 in points and 13 in points:
        while min(points) < 9:
            points[0] += 13
            points = sorted(points)
    if all(points[i] + 1 == points[i+1] for i in range(len(points)-1)): return True 
    return False

def determine(cards):
    number = []
    suit = []
    for x,y in cards:
        number.append(x)
        suit.append(y)
    
    if iscontinue(number) and len(set(suit)) == 1: return 9
    elif any(number.count(x)==4 for x in number): return 8
    elif any(number.count(x)==3 for x in number) and any(number.count(x)==2 for x in number): return 7
    elif len(set(suit)) == 1: return 6
    elif iscontinue(number): return 5
    elif any(number.count(x)==3 for x in number): return 4
    else :
        tmp = set()
        for x in number:
            if number.count(x) == 2:
                tmp.add(x)
        if len(tmp) == 2: return 3
        elif len(tmp) == 1: return 2

        else: return 1

def main():
    suit_table = {'S','H','D','C'}
    point_table = {'A','2','3','4','5','6','7','8','9','10','J','Q','K'}
    data = []
    isDuplicate = False
    isErroe = False

    for _ in range(2):
        cards = input().split()

        if sorted(cards) != sorted(list(set(cards))):
            isDuplicate = True
        
        cards = [[x[:-1],x[-1]] for x in cards]

        for card in cards :
            if len(card) != 2: isErroe = True
            if card[0] not in point_table: isErroe = True
            if card[1] not in suit_table: isErroe = True
        
        cards = [[card_to_point(x),y] for x,y in cards]
        data.append(cards)

    if isErroe: print("Error input") ; return
    elif isDuplicate: print("Duplicate deal") ; return 

    _max = 0

    for d in data:
        _max = max(determine(d),_max)

    print(_max)
if __name__ == "__main__":
    main()