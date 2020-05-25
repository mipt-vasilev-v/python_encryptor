from enum import Enum 
import string

ru_lowercase = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"


class Language(Enum):
    ENG = 'eng'
    RUS = 'rus'

lang_len = {Language.ENG : len(string.ascii_lowercase), \
            Language.RUS : len(ru_lowercase)}
