from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout, QButtonGroup, QVBoxLayout, QApplication, QWidget, QRadioButton, QPushButton, QLabel, QGroupBox
from random import shuffle, randint
#class, handling inf for every qstn
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
     self.question = question
     self.right_answer = right_answer
     self.wrong1 = wrong1
     self.wrong2 = wrong2
     self.wrong3 = wrong3

# окно
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("My Memo Card 📇 (Valve Edition)")
main_window.resize(600, 300)

#counter
main_window.cur_question = - 1

# main widgets
GroupBox = QGroupBox("Варианты ответов")
lb_question = QLabel("placeholder")
rbtn_1 = QRadioButton("1")
rbtn_2 = QRadioButton("2")
rbtn_3 = QRadioButton("3")
rbtn_4 = QRadioButton("4")
btn_ok = QPushButton('Ответить')

# put btn in group
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

# layouts
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

# setLayout for btn
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)  # Use addLayout, not addWidget
layout_ans1.addLayout(layout_ans3)

# setLayout for GroupBox
GroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Результаты теста')
lb_result = QLabel('ЗДЕСЬ БУДЕТ РЕЗУЛЬТАТ')  # Fixed: lb_result instead of lb_answer twice
lb_correct = QLabel('Здесь будет верный ответ') #  A separate label for correct answer

layout_res = QVBoxLayout()
layout_res.addWidget(lb_result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_correct, alignment=Qt.AlignHCenter) # Added lb_correct
AnsGroupBox.setLayout(layout_res) # Crucial: set layout for AnsGroupBox

# setLayout for everything
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

layout_line2.addWidget(GroupBox)
# добавляем другую группу
layout_line2.addWidget(AnsGroupBox)
# hiding group w/ qstn
AnsGroupBox.hide()  # No need to hide GroupBox initially

layout_line3.addStretch(1)
layout_line3.addWidget(btn_ok, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout() # Fixed typo: layout_card, not layout.card
layout_card.addLayout(layout_line1)
layout_card.addLayout(layout_line2)
layout_card.addLayout(layout_line3)
layout_card.setSpacing(5)


main_window.setLayout(layout_card)


# ans
def show_result():
    GroupBox.hide()
    AnsGroupBox.show()
    btn_ok.setText("Следующий вопрос")

# show em the dayum correct result 
def show_question():    
    GroupBox.show()
    AnsGroupBox.hide()
    btn_ok.setText("Ответить")

    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
#fn for choosing correct fn
def click_OK():
    if btn_ok.text() == "Ответить":
        check_answer()
    else:
        next_question()

answer = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
def ask(q):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)

    lb_question.setText(q.question)
    lb_correct.setText(q.right_answer)

    show_question()
main_window.total = 0
main_window.score = 0
#right ans?
def check_answer():
    if answer[0].isChecked():
        lb_result.setText("Правильно ✔️ ")
        main_window.score += 1
        print("Статистика")
        print("- Всего вопросов ", main_window.total)
        print("- Правильных вопросов", main_window.score)
        print('- Рейтинг', main_window.score / main_window.total * 100)
    else:
        lb_result.setText("Неправильно ❌ ")
    show_result()
    
question_list = [] #q list
def next_question():
    main_window.total += 1
    print("Статистика")
    print("- Всего вопросов ", main_window.total)
    print("- Правильных вопросов", main_window.score)
    len_list = len(question_list) - 1
    cur_question = randint(0, len_list)
    q = question_list[  cur_question]
    ask(q)

#вопрос, правильный и неправильные 3
q = Question('Какой культовый шутер от первого лица стал дебютной игрой компании?', "Half-Life" ,"Counter-Strike", "Team Fortress 2", "Quake")
question_list.append(q)
q = Question("В каком году была основана компания Valve?", "1996" ,"2002", "2010", "1980")
question_list.append(q)
q = Question('Как называется цифровая платформа для игр, разработанная Valve?', "Steam" ,"Origin", "Battle.net", "GOG.com")
question_list.append(q)
q = Question('Какая игра Valve впервые ввела "боевой пропуск" как часть игровой монетизации?', "Dota 2" ,"Portal", "Team Fortress Classic", "Half-Life 2")
question_list.append(q)
q = Question('Какая технология или устройство, связанное с виртуальной реальностью, было разработано Valve?', "Index" ,"Oculus Rift", "HTC Vive", "PSVR")
question_list.append(q)

next_question()

    
btn_ok.clicked.connect(click_OK)

main_window.show()
app.exec_()