class NotFoundException(Exception):

    def __init__(self, item):  # item parametr przekazywany
        self.item = item
