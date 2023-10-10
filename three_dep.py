import csv
import tkinter as tk
from tkinter import messagebox

font = ('Times New Roman', 14) # шрифт


def three_dep():
    def three_dep_1():
        filename = entry_three_dep_1.get()
        filename = filename + '.csv'
        with open(filename, newline='') as csv_file_read:
            csv_reader = csv.reader(csv_file_read, delimiter=';')
            with open('Отчет_three_dep_1.csv', 'a', newline='') as csv_file_write:
                csv_writer = csv.writer(csv_file_write, delimiter=';')
                for row in csv_reader:
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11] = \
                        row[1], row[2], row[5], row[3], row[4], row[7], row[13], row[15], row[16], row[17], row[18], \
                        row[19]
                    a = []
                    for i in range(len(row)):
                        a.append(row[i])
                        if i == 11:
                            break

                    csv_writer.writerow(a)
        messagebox.showinfo('Внимание!', 'Файл отчета по three_dep_1')

    root = tk.Tk()
    root.title('three_dep')
    root.geometry('350x200')

    label_three_dep_1 = tk.Label(root, text='Имя файла отчета по three_dep_1', font=font)
    label_three_dep_1.pack()

    entry_three_dep_1 = tk.Entry(root)
    entry_three_dep_1.pack()

    btn_three_dep_1 = tk.Button(root, text='Создать', command=three_dep_1, font=font)
    btn_three_dep_1.pack()

    def three_dep_2():
        filename = entry_three_dep_2.get()
        filename = filename + '.csv'
        with open(filename, newline='') as csv_file_read:
            csv_reader = csv.reader(csv_file_read, delimiter=';')
            with open('Отчет_three_dep_2.csv', 'a', newline='') as csv_file_write:
                csv_writer = csv.writer(csv_file_write, delimiter=';')
                for row in csv_reader:
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7] = \
                        row[1], row[2], '', row[3], row[4], row[6], row[10], row[11]
                    a = []
                    for i in range(len(row)):
                        a.append(row[i])
                        if i == 7:
                            break

                    csv_writer.writerow(a)
        messagebox.showinfo('Внимание!', 'Файл отчета по three_dep_2 создан')

    label_three_dep_2 = tk.Label(root, text='Имя файла отчета по three_dep_2', font=font)
    label_three_dep_2.pack()

    entry_three_dep_2 = tk.Entry(root)
    entry_three_dep_2.pack()

    btn_three_dep_2 = tk.Button(root, text='Создать', command=three_dep_2, font=font)
    btn_three_dep_2.pack()

    return root.mainloop()


if __name__ == '__main__':
    three_dep()


