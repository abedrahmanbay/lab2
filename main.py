import csv
import random
from xml.dom import minidom

# Пути к файлам (измените названия, если они отличаются)
CSV_FILE = 'books.csv'  
XML_FILE = 'currency.xml'

def solve_csv_tasks():
    print("--- ЗАДАНИЯ ПО CSV ---")
    
    # 1. Считаем количество записей с названием длиннее 30 символов
    # 2. Поиск по автору с ценой до 200 рублей
    # 3. Список всех издательств без повторений (Допзадание)
    # 4. Топ-20 популярных книг (Допзадание)
    
    count_long_titles = 0
    search_results = []
    all_books = []
    publishers = set()
    
    author_to_search = input("Введите имя автора для поиска: ").strip().lower()
    
    try:
        # Обычно файлы этого задания в кодировке cp1251 (Windows-1251)
        with open(CSV_FILE, 'r', encoding='cp1251') as f:
            # Разделитель в этих файлах обычно ';'
            reader = csv.DictReader(f, delimiter=';')
            
            for row in reader:
                all_books.append(row)
                
                # Задание 1: Длина названия > 30
                title = row.get('Название', '')
                if len(title) > 30:
                    count_long_titles += 1
                
                # Задание 2: Поиск автора + цена до 200 руб (Вариант 4)
                # Важно: заменяем запятую на точку для перевода в число, если есть
                try:
                    price = float(row.get('Цена', '0').replace(',', '.'))
                    author = row.get('Автор', '').lower()
                    if author_to_search in author and price <= 200:
                        search_results.append(row.get('Название'))
                except ValueError:
                    pass
                
                # Допзадание 1: Издательства без повторений
                pub = row.get('Издательство', '')
                if pub:
                    publishers.add(pub)

        # Вывод результатов задания 1
        print(f"1. Книг с названием длиннее 30 символов: {count_long_titles}")

        # Вывод результатов задания 2
        print(f"2. Результаты поиска автора '{author_to_search}' (до 200 руб):")
        if search_results:
            for title in search_results:
                print(f"   - {title}")
        else:
            print("   Ничего не найдено.")

        # Задание 3: Библиографические ссылки (20 случайных)
        # Формат: <автор>. <название> - <год>
        if len(all_books) >= 20:
            random_books = random.sample(all_books, 20)
            with open('bibliography.txt', 'w', encoding='utf-8') as bib_file:
                for i, book in enumerate(random_books, 1):
                    line = f"{i}. {book.get('Автор')}. {book.get('Название')} - {book.get('Год')}\n"
                    bib_file.write(line)
            print("3. Файл bibliography.txt успешно создан.")

        # Допзадание 1: Издательства
        print(f"4. Всего уникальных издательств: {len(publishers)}")

        # Допзадание 2: Самые популярные 20 книг (по полю 'Кол-во выдач')
        print("5. Топ-20 популярных книг:")
        # Сортируем по убыванию выдач
        top_20 = sorted(all_books, key=lambda x: int(x.get('Кол-во выдач', 0)), reverse=True)[:20]
        for i, book in enumerate(top_20, 1):
            print(f"   {i}. {book.get('Название')} (Выдач: {book.get('Кол-во выдач')})")

    except FileNotFoundError:
        print(f"Ошибка: Файл {CSV_FILE} не найден.")

def solve_xml_task():
    print("\n--- ЗАДАНИЕ ПО XML (Вариант 4) ---")
    # Вариант 4: Словарь "NumCode - CharCode"
    
    try:
        doc = minidom.parse(XML_FILE)
        valutes = doc.getElementsByTagName("Valute")
        
        currency_dict = {}
        
        for valute in valutes:
            num_code = valute.getElementsByTagName("NumCode")[0].firstChild.data
            char_code = valute.getElementsByTagName("CharCode")[0].firstChild.data
            currency_dict[num_code] = char_code
            
        print("Словарь NumCode - CharCode:")
        print(currency_dict)
        
    except Exception as e:
        print(f"Ошибка при обработке XML: {e}")

if __name__ == "__main__":
    solve_csv_tasks()
    solve_xml_task()