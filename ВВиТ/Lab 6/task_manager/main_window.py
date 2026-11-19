from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Менеджер задач")
        self.resize(500, 400)
        self.init_ui()
        self.connect_signals()
        self.update_counter()

    def init_ui(self):
        self.task_label = QLabel("Новая задача")
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Название задачи")
        self.add_button = QPushButton("Добавить")
        self.task_list = QListWidget()
        self.delete_button = QPushButton("Удалить")
        self.clear_button = QPushButton("Очистить всё")
        self.done_button = QPushButton("Выполнено / Не выполнено")
        self.delete_done_button = QPushButton("Удалить выполненные")
        self.counter_label = QLabel()
        self.done_label = QLabel()

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        input_layout = QHBoxLayout()
        input_layout.addWidget(self.task_input)
        input_layout.addWidget(self.add_button)

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.delete_button)
        buttons_layout.addWidget(self.clear_button)

        extra_layout = QHBoxLayout()
        extra_layout.addWidget(self.done_button)
        extra_layout.addWidget(self.delete_done_button)

        counters_layout = QHBoxLayout()
        counters_layout.addWidget(self.counter_label)
        counters_layout.addWidget(self.done_label)

        main_layout.addWidget(self.task_label)
        main_layout.addLayout(input_layout)
        main_layout.addWidget(self.task_list)
        main_layout.addLayout(buttons_layout)
        main_layout.addLayout(extra_layout)
        main_layout.addLayout(counters_layout)

    def connect_signals(self):
        self.add_button.clicked.connect(self.add_task)
        self.task_input.returnPressed.connect(self.add_task)
        self.delete_button.clicked.connect(self.delete_task)
        self.clear_button.clicked.connect(self.clear_tasks)
        self.done_button.clicked.connect(self.toggle_done)
        self.delete_done_button.clicked.connect(self.delete_done_tasks)

    def add_task(self):
        text = self.task_input.text().strip()

        if not text:
            QMessageBox.warning(self, "Ошибка", "Введите название задачи")
            return

        self.task_list.addItem(text)
        self.task_input.clear()
        self.update_counter()
        self.statusBar().showMessage(f"Задача добавлена: {text}", 3000)

    def delete_task(self):
        row = self.task_list.currentRow()

        if row < 0:
            QMessageBox.warning(self, "Ошибка", "Выберите задачу для удаления")
            return

        answer = QMessageBox.question(
            self, "Удаление", "Удалить выбранную задачу?"
        )

        if answer == QMessageBox.StandardButton.Yes:
            self.task_list.takeItem(row)
            self.update_counter()
            self.statusBar().showMessage("Задача удалена", 3000)

    def clear_tasks(self):
        if self.task_list.count() == 0:
            QMessageBox.information(self, "Очистка", "Список задач уже пуст")
            return

        answer = QMessageBox.question(
            self, "Очистка", "Удалить все задачи?"
        )

        if answer == QMessageBox.StandardButton.Yes:
            self.task_list.clear()
            self.update_counter()
            self.statusBar().showMessage("Список очищен", 3000)

    def update_counter(self):
        count = self.task_list.count()
        self.counter_label.setText(f"Количество задач: {count}")
        self.done_label.setText(f"Выполнено: {self.count_done()}")

    def is_done(self, item):
        return bool(item.data(Qt.ItemDataRole.UserRole))

    def set_done(self, item, done):
        item.setData(Qt.ItemDataRole.UserRole, done)
        font = item.font()
        font.setStrikeOut(done)
        item.setFont(font)

    def count_done(self):
        return sum(
            1
            for row in range(self.task_list.count())
            if self.is_done(self.task_list.item(row))
        )

    def toggle_done(self):
        item = self.task_list.currentItem()

        if item is None:
            QMessageBox.warning(self, "Ошибка", "Выберите задачу")
            return

        done = not self.is_done(item)
        self.set_done(item, done)
        self.update_counter()

        if done:
            self.statusBar().showMessage("Задача выполнена", 3000)
        else:
            self.statusBar().showMessage("Задача снова активна", 3000)

    def delete_done_tasks(self):
        if self.count_done() == 0:
            QMessageBox.information(
                self, "Удаление", "Нет выполненных задач"
            )
            return

        answer = QMessageBox.question(
            self, "Удаление", "Удалить все выполненные задачи?"
        )

        if answer == QMessageBox.StandardButton.Yes:
            for row in reversed(range(self.task_list.count())):
                if self.is_done(self.task_list.item(row)):
                    self.task_list.takeItem(row)

            self.update_counter()
            self.statusBar().showMessage("Выполненные задачи удалены", 3000)
