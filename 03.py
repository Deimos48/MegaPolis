import csv


with open("vacancy.csv", encoding="utf-8") as file: # Открываем файл
    reader = csv.DictReader(file, delimiter=";")    # Считываем
    reader = list(reader)

    request = input()
    while request != "None":    # Пока запрос не равен None
        was = False
        for row in reader:
            if row["Role"] == request:  # Если нашлось
                sal = row['\ufeffSalary']
                print(f"В {row['Company']} найдена вакансия: {row['Role']}. З/п составит: {sal}")
                was = True
        if not was: # Проверка на нахождение
            print("К сожалению, ничего не удалось найти")
        request = input()
