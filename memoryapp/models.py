from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Category:
    category_id: int
    name: str


@dataclass_json
@dataclass
class Card:
    card_id: int  # deklarowanie pól jako właściwości danej klasy
    category_id: int
    word: str
    translation: str


