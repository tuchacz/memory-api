from memoryapp.models import Category

categories_list = [
    Category(1, 'Dom'),
    Category(2, 'Rodzina')
]


def get_categories():
    return categories_list
