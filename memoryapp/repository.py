from memoryapp.exceptions import NotFoundException
from memoryapp.models import Category, Card

categories_list = [
    Category(1, 'Dom'),
    Category(2, 'Rodzina')
]
cards_list = [
    Card(1, 1, 'Drzwi', 'Door'),
    Card(2, 1, 'Okno', 'Window'),
]

id_categories = 2
id_cards = 2


def get_categories():
    return categories_list


def create_category(category_name):
    category = Category(__next_category_id(), category_name)
    categories_list.append(category)

    return category


def get_category(category_id):
    results = [category for category in categories_list if category.category_id == category_id]

    if results:  # pozytywny przypadek
        return results[0]
    else:
        raise NotFoundException('Category')


def delete_category(category_id):
    results = [category for category in categories_list if category.category_id == category_id]

    if results:
        categories_list[:] = [category for category in categories_list if category.category_id != category_id]
        cards_list[:] = [card for card in cards_list if card.category_id != category_id]
    else:
        raise NotFoundException('Category')


def get_cards(category_id):
    print(cards_list)
    categories_results = [category for category in categories_list if category.category_id == category_id]

    if not categories_results:  # jezeli jest pusta not categories
        raise NotFoundException('Category')

    cards_results = [card for card in cards_list if card.category_id == category_id]

    return cards_results


def create_card(category_id, word, translation):
    categories_results = [category for category in categories_list if category.category_id == category_id]

    if not categories_results:  # jezeli jest pusta not categories
        raise NotFoundException('Category')

    card = Card(__next_card_id(), category_id, word, translation)
    cards_list.append(card)

    return card


def delete_card(category_id, card_id):
    categories_results = [category for category in categories_list if category.category_id == category_id]

    if not categories_results:  # jezeli jest pusta not categories
        raise NotFoundException('Category')

    cards_results = [card for card in cards_list if card.category_id == category_id and card.card_id == card_id]

    if cards_results:
        cards_list[:] = [card for card in cards_list if card.category_id != category_id or card.card_id != card_id]
    else:
        raise NotFoundException('Card')


def __next_category_id():
    global id_categories
    id_categories += 1
    return id_categories


def __next_card_id():
    global id_cards
    id_cards += 1
    return id_cards
