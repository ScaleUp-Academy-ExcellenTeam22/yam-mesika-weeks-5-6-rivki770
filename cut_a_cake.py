import functools


def get_recipe_price(prices: dict, optionals=[], **ingredients) -> int:
    """
    The function calculates the cost of the products for the recipe.
    :param prices: Dictionary with products and prices per 100 grams.
    :param optionals: List of products to download from the recipe.
    :param ingredients: Unlimited amount of products, and how many grams to use from each.
    :return: The cost of the recipe.
    """
    list_of_relevantive_components = [component for component in ingredients if component not in optionals]

    if len(list_of_relevantive_components) == 0:
        return 0
    if len(list_of_relevantive_components) == 1:
        return int(prices[list_of_relevantive_components[0]] * (ingredients[list_of_relevantive_components[0]] / 100))
    return int(functools.reduce(lambda a, b: prices[a] * (ingredients[a] / 100) +
                                             prices[b] * (ingredients[b] / 100), list_of_relevantive_components))


def main():
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))
    print(get_recipe_price({}))


if __name__ == '__main__' :
    main()
