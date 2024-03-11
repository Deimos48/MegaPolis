import csv
import random

def quicksort(n):
    if len(n) <= 1:
        return n
    else:
        l_list = []
        m_list = []
        r_list = []
        q = random.choice([x for x in n])
        for a in n:
            if a["Company_Size"] < q["Company_Size"]:
                l_list.append(a)
            elif a["Company_Size"] > q["Company_Size"]:
                r_list.append(a)
            else:
                m_list.append(a)
        return quicksort(l_list) + m_list + quicksort(r_list)


with open('vacancy.csv', encoding='utf-8') as file: # Открываем файл
    reader = list(csv.DictReader(file, delimiter=';'))  # Считываем
    reader = quicksort(reader)  # Сортируем

    for row in reader:
        if row["Role"] == "классный руководитель":  # Если нашлось
            sal = row['\ufeffSalary']
            print(f"В омпании {row['Company']} есть заданная профессия: {row['Role']}. З/п в такой компании составит: {sal}")
            break


with open("vacancy_2.csv", "w", encoding="utf-8") as file:    # Открываем на запись
    writer = csv.DictWriter(file, fieldnames=['\ufeffSalary', 'Work_Type', 'Company_Size', 'Role', 'Company'], delimiter=";")   # Заголовки
    writer.writeheader()
    writer.writerows(reader)