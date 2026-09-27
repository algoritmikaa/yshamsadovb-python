from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QHBoxLayout, QVBoxLayout, QPushButton,
                             QListWidget, QLineEdit, QFrame,
                             QTextEdit, QInputDialog, QMessageBox)
import json
import os

# ------------------------------------------------------------
# Загрузка заметок из файла или создание начальной заметки
# ------------------------------------------------------------
NOTES_FILE = 'notes_data.json'
if os.path.exists(NOTES_FILE):
    with open(NOTES_FILE, 'r', encoding='UTF-8') as file:
        notes = json.load(file)
else:
    notes = {
        "Алгоритмика": {
            "текст": "Алгоритмика - международная школа программирования для детей.",
            "теги": ["школа", "программирование", "грозный"]
        }
    }
    with open(NOTES_FILE, 'w', encoding='UTF-8') as file:
        json.dump(notes, file, ensure_ascii=False, indent=4)

app = QApplication([])

# ------------------------------------------------------------
# Главное окно с общими стилями
# ------------------------------------------------------------
main_win = QWidget()
main_win.setWindowTitle('📌 Умные заметки')
main_win.resize(950, 650)
main_win.setStyleSheet("""
    QWidget {
        background-color: #F5F7FA;
        font-family: 'Segoe UI', Arial, sans-serif;
    }
    QLabel {
        font-size: 14px;
        color: #2c3e50;
        padding: 2px;
    }
    QListWidget {
        border: 2px solid #cfd8dc;
        border-radius: 12px;
        background: white;
        padding: 6px;
        font-size: 13px;
        outline: none;
    }
    QListWidget::item:selected {
        background-color: #42a5f5;
        color: white;
        border-radius: 6px;
    }
    QLineEdit {
        border: 2px solid #cfd8dc;
        border-radius: 10px;
        padding: 8px;
        background: white;
        font-size: 13px;
    }
    QTextEdit {
        border: 2px solid #cfd8dc;
        border-radius: 12px;
        background: white;
        padding: 10px;
        font-size: 14px;
    }
    QPushButton {
        border-radius: 10px;
        padding: 10px 16px;
        font-size: 13px;
        font-weight: bold;
        color: white;
        border: none;
    }
    QPushButton:hover {
        opacity: 0.9;
    }
    QPushButton:pressed {
        opacity: 0.7;
    }
""")

# ------------------------------------------------------------
# Виджеты с эмодзи-стикерами
# ------------------------------------------------------------
# Декоративный заголовок
title_label = QLabel('📌 Мои умные заметки ✨')
title_label.setAlignment(Qt.AlignCenter)
title_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #1E88E5; margin-bottom: 8px;")

# Стикеры-эмодзи (просто красивые метки)
sticker_row = QHBoxLayout()
sticker1 = QLabel('📒')
sticker2 = QLabel('⭐')
sticker3 = QLabel('📎')
for s in (sticker1, sticker2, sticker3):
    s.setStyleSheet("font-size: 28px;")
    s.setAlignment(Qt.AlignCenter)
    sticker_row.addWidget(s)

# Основные элементы
list_notes_label = QLabel('📋 Список заметок')
list_notes = QListWidget()

button_note_add = QPushButton('➕ Создать заметку')
button_note_del = QPushButton('🗑️ Удалить заметку')
button_note_save = QPushButton('💾 Сохранить заметку')

list_tag_label = QLabel('🏷️ Список тегов')
list_tag = QListWidget()

button_tag_add = QPushButton('🔖 Прикрепить тег')
button_tag_del = QPushButton('❌ Открепить тег')
button_tag_search = QPushButton('🔍 Искать по тегу')

field_text = QTextEdit()
field_text.setPlaceholderText('✍️ Введите текст заметки...')

field_tag = QLineEdit()
field_tag.setPlaceholderText('🏷️ Введите тег...')

# Рамка для блока тегов (как стикер-панель)
tag_frame = QFrame()
tag_frame.setFrameShape(QFrame.StyledPanel)
tag_frame.setStyleSheet("background: #E8F0FE; border-radius: 14px; padding: 8px; margin-top: 6px;")
tag_layout = QVBoxLayout()
tag_layout.addWidget(list_tag_label)
tag_layout.addWidget(list_tag)
tag_layout.addWidget(field_tag)
tag_frame.setLayout(tag_layout)

# ------------------------------------------------------------
# Цвета кнопок
# ------------------------------------------------------------
button_note_add.setStyleSheet("background-color: #4CAF50;")
button_note_del.setStyleSheet("background-color: #f44336;")
button_note_save.setStyleSheet("background-color: #2196F3;")
button_tag_add.setStyleSheet("background-color: #FF9800;")
button_tag_del.setStyleSheet("background-color: #9C27B0;")
button_tag_search.setStyleSheet("background-color: #607D8B;")

# ------------------------------------------------------------
# Размещение (Layouts)
# ------------------------------------------------------------
main_line = QHBoxLayout()

# Левая колонка с текстом и стикерами
col_1 = QVBoxLayout()
col_1.addWidget(title_label)
col_1.addLayout(sticker_row)  # строка стикеров
col_1.addWidget(field_text)

# Правая колонка
col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)

row_1 = QHBoxLayout()  # горизонтально, а не вертикально
row_1.addWidget(button_note_add)
row_1.addWidget(button_note_del)

row_2 = QHBoxLayout()
row_2.addWidget(button_note_save)

col_2.addLayout(row_1)
col_2.addLayout(row_2)

col_2.addWidget(tag_frame)

row_3 = QHBoxLayout()
row_3.addWidget(button_tag_add)
row_3.addWidget(button_tag_del)

row_4 = QHBoxLayout()
row_4.addWidget(button_tag_search)

col_2.addLayout(row_3)
col_2.addLayout(row_4)

main_line.addLayout(col_1)
main_line.addLayout(col_2)
main_win.setLayout(main_line)

# ------------------------------------------------------------
# Функции приложения
# ------------------------------------------------------------
def save_to_file():
    """Сохраняет текущий словарь notes в JSON-файл."""
    with open(NOTES_FILE, 'w', encoding='UTF-8') as file:
        json.dump(notes, file, ensure_ascii=False, indent=4)

def show_note():
    """Отображает текст и теги выбранной заметки."""
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        field_text.setText(notes[key]["текст"])
        list_tag.clear()
        list_tag.addItems(notes[key]["теги"])

def add_note():
    """Создаёт новую заметку с заданным именем."""
    note_name, ok = QInputDialog.getText(main_win, "➕ Новая заметка", "Введите название:")
    if ok and note_name.strip() != '':
        note_name = note_name.strip()
        if note_name in notes:
            QMessageBox.warning(main_win, "Ошибка", "Заметка с таким именем уже существует!")
            return
        notes[note_name] = {"текст": "", "теги": []}
        list_notes.addItem(note_name)
        list_notes.setCurrentRow(list_notes.count() - 1)
        show_note()
        save_to_file()

def delete_note():
    """Удаляет выбранную заметку."""
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        reply = QMessageBox.question(main_win, "🗑️ Удаление", f"Удалить заметку '{key}'?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            del notes[key]
            list_notes.clear()
            list_notes.addItems(notes.keys())
            field_text.clear()
            list_tag.clear()
            save_to_file()

def save_note():
    """Сохраняет изменения текста текущей заметки."""
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        notes[key]["текст"] = field_text.toPlainText()
        save_to_file()
        QMessageBox.information(main_win, "💾 Сохранено", f"Заметка '{key}' сохранена!")

def add_tag():
    """Прикрепляет тег к заметке."""
    if not list_notes.selectedItems():
        QMessageBox.warning(main_win, "Ошибка", "Выберите заметку для добавления тега.")
        return
    tag_text = field_tag.text().strip()
    if tag_text == '':
        QMessageBox.warning(main_win, "Ошибка", "Введите тег!")
        return
    key = list_notes.selectedItems()[0].text()
    if tag_text not in notes[key]["теги"]:
        notes[key]["теги"].append(tag_text)
        list_tag.addItem(tag_text)
        field_tag.clear()
        save_to_file()
    else:
        QMessageBox.warning(main_win, "Ошибка", "Такой тег уже прикреплён!")

def delete_tag():
    """Открепляет выбранный тег от заметки."""
    if not list_notes.selectedItems():
        QMessageBox.warning(main_win, "Ошибка", "Выберите заметку.")
        return
    if not list_tag.selectedItems():
        QMessageBox.warning(main_win, "Ошибка", "Выберите тег для удаления.")
        return
    key = list_notes.selectedItems()[0].text()
    tag_text = list_tag.selectedItems()[0].text()
    notes[key]["теги"].remove(tag_text)
    list_tag.clear()
    list_tag.addItems(notes[key]["теги"])
    save_to_file()

def search_by_tag():
    """Ищет заметки по введённому тегу."""
    tag_text = field_tag.text().strip()
    if tag_text == '':
        list_notes.clear()
        list_notes.addItems(notes.keys())
        list_tag.clear()
        return
    filtered = [name for name, data in notes.items() if tag_text in data["теги"]]
    list_notes.clear()
    list_notes.addItems(filtered)
    if not filtered:
        QMessageBox.information(main_win, "🔍 Результат", "Заметок с таким тегом не найдено.")
    else:
        list_notes.setCurrentRow(0)
        show_note()

# ------------------------------------------------------------
# Подключение сигналов
# ------------------------------------------------------------
list_notes.itemClicked.connect(show_note)
button_note_add.clicked.connect(add_note)
button_note_del.clicked.connect(delete_note)
button_note_save.clicked.connect(save_note)
button_tag_add.clicked.connect(add_tag)
button_tag_del.clicked.connect(delete_tag)
button_tag_search.clicked.connect(search_by_tag)

# ------------------------------------------------------------
# Начальное наполнение интерфейса
# ------------------------------------------------------------
list_notes.addItems(notes.keys())
if notes:
    list_notes.setCurrentRow(0)
    show_note()

main_win.show()
app.exec()