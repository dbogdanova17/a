#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QMessageBox, QRadioButton, QLabel, QGroupBox, QButtonGroup
from random import shuffle
app = QApplication([])
window = QWidget()
print('hello')
class Question ():
    def __init__(self,question, right_ans, wrong1, wrong2, wrong3):
        self.question = question
        self.right_ans = right_ans
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

line2 = QVBoxLayout()
qu = QLabel('Какой национальности не существует?')
line2.addWidget(qu)

line1 = QHBoxLayout()
button = QPushButton('Ответить')
line1.addWidget(button)

group = QGroupBox('Варианты ответов')
btn1 = QRadioButton('Энцы')
btn2 = QRadioButton('Смурфы')
btn3 = QRadioButton('Чулымцы')
btn4 = QRadioButton('Алеуты')
ans1 = QHBoxLayout()
ans2 = QVBoxLayout()
ans3 = QVBoxLayout()

ans2.addWidget(btn1)
ans2.addWidget(btn2)
ans3.addWidget(btn3)
ans3.addWidget(btn4)

ans1.addLayout(ans2)
ans1.addLayout(ans3)
group.setLayout(ans1)

line3 = QVBoxLayout()
line3.addLayout(line2)
line3.addWidget(group)
ansgroup = QGroupBox('Результат теста')
t = QLabel('правильно/неправильно')
tans = QLabel('Правильный ответ')


line4 = QVBoxLayout()
line4.addWidget(t)
line4.addWidget(tans)
ansgroup.setLayout(line4)


RadioGroup = QButtonGroup()
RadioGroup.addButton(btn1)
RadioGroup.addButton(btn2)
RadioGroup.addButton(btn3)
RadioGroup.addButton(btn4)

line3.addWidget(ansgroup)
ansgroup.hide()
line3.addLayout(line1)



def show_question():
    group.show()
    ansgroup.hide()
    button.setText('Ответить')
    RadioGroup.setExclusive(False)
    btn1.setChecked(False)
    btn2.setChecked(False)
    btn3.setChecked(False)
    btn4.setChecked(False)
    RadioGroup.setExclusive(True)

def start_test():
    if button.text() == 'Ответить':
        check_answer()
    elif button.text() == 'Следующий вопрос':
        next_question()

def show_result():
    group.hide()
    ansgroup.show()
    button.setText('Следующий вопрос')

answers = [btn1, btn2, btn3, btn4,]

questions_list = []
questions_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Испанский', 'Бразильский', 'Итальянский'))

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_ans)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    qu.setText(q.question)
    tans.setText(q.right_ans)
    show_question()

def show_corect(res):
    t.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_corect('Правильно!')
    else:
        if answers[1].isChecked or answers[2].isChecked or answers[3].isChecked:
            show_corect('Неверно!')

def next_question():
    window.cur_q += 1
    if window.cur_q == len(questions_list):
        window.cur_q = 0
    ask(questions_list[window.cur_q])


button.clicked.connect(start_test)

window.cur_q = -1
next_question()
window.setLayout(line3)
window.show()
app.exec_()

