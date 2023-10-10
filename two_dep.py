import csv
import tkinter as tk
from tkinter import messagebox

font = ('Times New Roman', 14) # шрифт


def two_dep():
    def two_dep_1():
        filename = entry_two_dep_1.get()
        filename = filename + '.csv'
        with open(filename, newline='') as csv_file_read:
            csv_reader = csv.reader(csv_file_read, delimiter=';')
            with open('Отчет_two_dep_1.csv', 'a', newline='') as csv_file_write:
                csv_writer = csv.writer(csv_file_write, delimiter=';')
                for row in csv_reader:
                    row[0], row[2], row[3], row[4], row[5], row[6], row[7] = row[2], row[4], '', row[3], '', '', row[5]
                    a = []
                    for i in range(len(row)):
                        a.append(row[i])
                    csv_writer.writerow(a)

        messagebox.showinfo('Внимание!', 'Файл отчета two_dep_1 создан')

    root = tk.Tk()
    root.title('two_dep')
    root.geometry('350x250')

    label_two_dep_1 = tk.Label(root, text='Имя файла отчета two_dep_1', font=font)
    label_two_dep_1.pack()

    entry_two_dep_1 = tk.Entry(root)
    entry_two_dep_1.pack()

    btn_two_dep_1 = tk.Button(root, text='Создать', command=two_dep_1, font=font)
    btn_two_dep_1.pack()

    def two_dep_2():
        filename = entry_two_dep_2.get()
        filename = filename + '.csv'
        with open(filename, newline='') as csv_file_read:
            csv_reader = csv.reader(csv_file_read, delimiter=';')
            with open('Отчет_two_dep_2.csv', 'a', newline='') as csv_file_write:
                csv_writer = csv.writer(csv_file_write, delimiter=';')
                for row in csv_reader:
                    row[0], row[1], row[5], row[6] = row[1], row[5], row[6], row[7]
                    a = []
                    for i in range(len(row)):
                        if i == 7:
                            break
                        a.append(row[i])
                    csv_writer.writerow(a)

        messagebox.showinfo('Внимание!', 'Файл отчета по two_dep_2 создан')

    label_two_dep_2 = tk.Label(root, text='Имя файла отчета по two_dep_2', font=font)
    label_two_dep_2.pack()

    entry_two_dep_2 = tk.Entry(root)
    entry_two_dep_2.pack()

    btn_two_dep_2 = tk.Button(root, text='Создать', command=two_dep_2, font=font)
    btn_two_dep_2.pack()

    return root.mainloop()


if __name__ == '__main__':
    two_dep()
