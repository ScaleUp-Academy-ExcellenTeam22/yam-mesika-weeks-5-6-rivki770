def get_recipe_price(prices, optionals=[], **ingredients):
    cost = 0
    for i in ingredients:
        if i not in optionals:
            cost += prices[i] * (ingredients[i] / 100)
    return int(cost)


def main():
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))
    print(get_recipe_price({}))


if __name__ == '__main__' :
    main()