import tkinter as tk
from one_dep import one_dep
from two_dep import two_dep
from three_dep import three_dep
from four_dep import four_dep
from five_dep import five_dep
from six_dep import six_dep
from seven_dep import seven_dep
from final_report import create_report


font = ('Times New Roman', 14) # шрифт

root = tk.Tk()
root.title('Отчеты')
root.geometry('250x520')


def one_dep_():
    one_dep()


btn_one_dep = tk.Button(root, text='one_dep', command=one_dep_, width=10, height=2, font=font)


def two_dep_():
    two_dep()


btn_two_dep = tk.Button(root, text='two_dep', command=two_dep_, width=10, height=2, font=font)


def three_dep_():
    three_dep()


btn_three_dep = tk.Button(root, text='three_dep', command=three_dep_, width=10, height=2, font=font)


def four_dep_():
    four_dep()


btn_four_dep = tk.Button(root, text='four_dep', command=four_dep_, width=10, height=2, font=font)


def five_dep_():
    five_dep()


btn_five_dep = tk.Button(root, text='five_dep', command=five_dep_, width=10, height=2, font=font)


def six_dep_():
    six_dep()


btn_six_dep = tk.Button(root, text='six_dep', command=six_dep_, width=10, height=2, font=font)


def seven_dep_():
    seven_dep()


btn_seven_dep = tk.Button(root, text='seven_dep', command=seven_dep_, width=10, height=2, font=font)


def report():
    create_report()


btn_create_report = tk.Button(root, text='Отчет', command=report, width=10, height=2, font=font)

btn_list = [btn_one_dep, btn_two_dep, btn_three_dep, btn_four_dep, btn_five_dep, btn_six_dep, btn_seven_dep, btn_create_report]
for btn in btn_list:
    btn.pack()

if __name__ == '__main__':
    root.mainloop()
