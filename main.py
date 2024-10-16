import json

def read_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Файл не знайдено!")
        return None

def write_json(file_path, data):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"Дані успішно записано у файл {file_path}")
    except Exception as e:
        print(f"Помилка запису файлу: {e}")

def display_json(data):
    for team in data.get("teams", []):
        print(f"Команда: {team['name']}, Очки: {team['points']}")

def add_team(data):
    name = input("Введіть назву команди: ")
    points = int(input("Введіть кількість очок команди: "))
    data['teams'].append({"name": name, "points": points})
    print(f"Команда {name} успішно додана.")

def remove_team(data):
    name = input("Введіть назву команди для видалення: ")
    data['teams'] = [team for team in data['teams'] if team['name'] != name]
    print(f"Команда {name} успішно видалена.")

def search_team(data):
    name = input("Введіть назву команди для пошуку: ")
    team = next((team for team in data['teams'] if team['name'] == name), None)
    if team:
        print(f"Команда: {team['name']}, Очки: {team['points']}")
    else:
        print(f"Команда {name} не знайдена.")

def find_top_teams(data):
    teams = sorted(data['teams'], key=lambda x: x['points'], reverse=True)
    if len(teams) >= 3:
        print(f"Чемпіон: {teams[0]['name']} з {teams[0]['points']} очками.")
        print(f"Друге місце: {teams[1]['name']} з {teams[1]['points']} очками.")
        print(f"Третє місце: {teams[2]['name']} з {teams[2]['points']} очками.")
        write_json('top_teams.json', {"champion": teams[0], "second_place": teams[1], "third_place": teams[2]})
    else:
        print("Недостатньо команд для визначення трьох кращих.")

def main():
    file_path = 'teams.json'
    data = read_json(file_path)

    if data is None:
        return

    actions = {
        '1': lambda: display_json(data),
        '2': lambda: (add_team(data), write_json(file_path, data)),
        '3': lambda: (remove_team(data), write_json(file_path, data)),
        '4': lambda: search_team(data),
        '5': lambda: find_top_teams(data),
        '6': lambda: print("Завершення програми...")
    }

    while True:
        print("\nОберіть дію:")
        print("1. Вивести вміст JSON файлу")
        print("2. Додати нову команду")
        print("3. Видалити команду")
        print("4. Пошук команди за назвою")
        print("5. Визначити чемпіона та команди на 2 і 3 місцях")
        print("6. Вийти")

        choice = input("Введіть номер дії: ")

        action = actions.get(choice)
        if action:
            action()
            if choice == '6':
                break
        else:
            print("Некоректний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    main()
