import csv


with open('vacancy.csv', encoding='utf-8') as file: # Открываем файл
    reader = list(csv.DictReader(file, delimiter=';'))  # Считываем
    reader.sort(key=lambda x: x['\ufeffSalary'], reverse=True)  # Сортируем

    was = 0
    for row in reader:  # Проходимся по строкам списка
        if was < 3:
            sal = row['\ufeffSalary']
            print(f"{row['Company']} - {row['Role']} - {sal}")  # Выводим
            was += 1


with open("vacancy_new.csv", "w", encoding="utf-8") as file:    # Открываем на запись
    writer = csv.DictWriter(file, fieldnames=['Work_Type', '\ufeffSalary', 'Company', 'Role', 'Company_Size'], delimiter=";")   # Заголовки
    writer.writeheader()
    writer.writerows(reader)
