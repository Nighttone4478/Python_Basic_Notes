def card_to_point(card):
    if card == 'A': return 1
    elif card in {'J','Q','K'}: return 0.5
    else : return int(card)

def main():
    n = int(input())
    point = [0] * (n + 1)

    money = list(map(int,input().split()))
    cards = [[0] for _ in range(n+1)]
    first_card = input().split()

    first_card.append(first_card.pop(0))
    for i in range(len(first_card)):
        point[i] += card_to_point(first_card[i])
        cards[i][0] = first_card[i]
    
    i = 0
    while i < n:
        s = input().split()
        if s[0] == 'Y':
            point[i] += card_to_point(s[1])
            cards[i].append(s[1])
            if point[i] == 10.5:
                i += 1
            elif point[i] > 10.5:
                point[i] = 11
                i += 1
            elif len(cards[i]) == 5:
                point[i] = 10.5
                i += 1
        elif s[0] == 'N':
            i += 1
    
    if not all((x == 10.5 or x == 11) for x in point[:-1]):
        while point[-1] < min(point[:-1]):
            card = input()
            cards[-1].append(card)
            point[-1] += card_to_point(card)
            if point[-1] == 10.5:
                break
            elif point[-1] > 10.5:
                point[-1] = -1
                break
            
    for i in range(len(point)-1):
        if point[i] == 11:
            print(f"Player{i} -{money[i]}")
        elif point[i] == 10.5:
            print(f"Player{i} +{money[i]}")
        elif point[i] > point[-1]:
            print(f"Player{i} +{money[i]}")
        else:
            print(f"Player{i} -{money[i]}")



if __name__ == "__main__":
    main()