# Шифратор
Приложение без внешнего интерфейса для шифрования/дешифрования текстов, поддерживаются кириллица и латиница.

---

# Требования
Python 3, библиотека argparse

---

# Использование
* Шифрование:

    ./encryptor.py encode --cipher {caesar|vigenere} --key {<number>|<word>} [--input-file input.txt] [--output-file output.txt]

* Дешифрование:

    ./encryptor.py decode --cipher {caesar|vigenere} --key {<number>|<word>} [--input-file input.txt] [--output-file output.txt]

* Взлом:

    ./encryptor.py hack [--input-file input.txt] [--output-file output.txt] --model-file {model}

* Тренировка модели для *--model-file*:

    ./encryptor.py train --text-file {input.txt} --model-file {model}

Где: 

1. *caesar|vigenere* - тип шифра
1. *key* - ключ шифра
1. *--input-file* - файл для чтения
1. *--output-file* - файл для вывода
1. *--model-file* - путь к файлу модели, которая будет использоваться. 
