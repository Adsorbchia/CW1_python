import datetime
import json
from pprint import pprint


def input_n(n_data, filename):
    print("1 - создать заметку")
    print("2 - удалить заметку")
    print("3 - отредактировать заметку")
    print("4 - просмотреть список заметок")
    num = (int(input("Выберите число от 1 до 4 ")))
    if num == 1:
        with open(filename, encoding='utf-8') as file:
            n_data = json.load(file)
            if len(n_data['notes']) == 0:
                write(n_data, filename)
                print("Заметка создана")
            else:
                add_note(n_data, filename)
                print("Заметка создана")
    elif num == 2:
        delete_note(n_data, filename)
        print("Заметка удалена")

    elif num == 3:
        correct_note(n_data, filename)
        print("Заметка успешно отредактирована")

    elif num == 4:
        pprint(read(filename))

    elif num <= 0 & num >= 5:
        print("Неправильно набрана цифра. Повторите ввод")


def write(n_data, filename):
    note = Note()
    note.set_id(1)
    note.set_note_name(str(input("Введите название заметки")))
    note.set_text(str(input("Введите текст")))
    note.set_d(datetime.datetime.now().strftime('%d.%m.%y'))
    n_data['notes'].append(note.__dict__)
    n_data = json.dumps(n_data)
    n_data = json.loads(str(n_data))
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(n_data, file, indent=4)


def read(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


def add_note(n_data, filename):
    with open(filename, encoding='utf-8') as file:
        n_data = json.load(file)
        note = Note()
        note.set_id(len(n_data['notes']) + 1)
        note.set_note_name(str(input("Введите название заметки")))
        note.set_text(str(input("Введите текст")))
        note.set_d(datetime.datetime.now().strftime('%d.%m.%y'))
        n_data['notes'].append(note.__dict__)
        n_data = json.dumps(n_data)
        n_data = json.loads(str(n_data))
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(n_data, f, indent=4)


def correct_note(n_data, filename):
    with open(filename, encoding='utf-8') as file:
        n_data = json.load(file)
        note = Note()
        n_id = (int(input("Введите номер заметки,которую хотите отредактировать ")))
        note.set_text(str(input("Введите новый текст")))
        n_data['notes'][n_id - 1]["text_note"] = note.get_text()
        n_data = json.dumps(n_data)
        n_data = json.loads(str(n_data))
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(n_data, f, indent=4)


def delete_note(n_data, filename):
    with open(filename, encoding='utf-8') as file:
        n_data = json.load(file)
        n_id = (int(input("Введите номер заметки,которую хотите удалить ")))
        del n_data['notes'][n_id - 1]
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(n_data, f, indent=4)


class Note:

    def __init__(self):
        self.note_id = None
        self.note_name = None
        self.text_note = None
        self.dt_now = datetime.datetime.now().strftime('%d.%m.%y')

    def get_id(self):
        return self.note_id

    def get_note_name(self):
        return self.note_name

    def get_text(self):
        return self.text_note

    def get_d(self):
        return self.dt_now

    def set_id(self, note_id):
        self.note_id = note_id

    def set_note_name(self, note_name):
        self.note_name = note_name

    def set_text(self, text_note):
        self.text_note = text_note

    def set_d(self, dt_now):
        self.dt_now = dt_now


data = {
    "notes": []
}

correct_note(data,'my_note.json')
