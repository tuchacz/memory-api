from memoryapp.exceptions import NotFoundException
from memoryapp.models import Category

categories_list = [
    Category(1, 'Dom'),
    Category(2, 'Rodzina')
]
id_categories = 2


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
    else:
        raise NotFoundException('Category')


def __next_category_id():
    global id_categories
    id_categories += 1
    return id_categories
