import csv
import tkinter as tk
from tkinter import messagebox

font = ('Times New Roman', 14) # шрифт


def six_dep():
    def six_dep_1():
        filename = entry_six_dep_1.get()
        filename = filename + '.csv'
        with open(filename, newline='') as csv_file_read:
            csv_reader = csv.reader(csv_file_read, delimiter=';')
            with open('Отчет_six_dep_1.csv', 'a', newline='') as csv_file_write:
                csv_writer = csv.writer(csv_file_write, delimiter=';')
                for row in csv_reader:
                    a = []
                    row[2], row[3], row[4] = row[4], row[2], row[3]
                    for i in range(len(row)):
                        a.append(row[i])
                    csv_writer.writerow(a)

        messagebox.showinfo('Внимание!', 'Файл отчета six_dep_1')

    root = tk.Tk()
    root.title('six_dep')
    root.geometry('350x250')

    label_six_dep_1 = tk.Label(root, text='Имя файла отчета six_dep_1', font=font)
    label_six_dep_1.pack()

    entry_six_dep_1 = tk.Entry(root)
    entry_six_dep_1.pack()

    btn_six_dep_1 = tk.Button(root, text='Создать', command=six_dep_1, font=font)
    btn_six_dep_1.pack()

    def six_dep_2():
        filename = entry_six_dep_2.get()
        filename = filename + '.csv'
        with open(filename, newline='') as csv_file_read:
            csv_reader = csv.reader(csv_file_read, delimiter=';')
            with open('Отчет_six_dep_2.csv', 'a', newline='') as csv_file_write:
                csv_writer = csv.writer(csv_file_write, delimiter=';')
                for row in csv_reader:
                    a = []
                    row[1], row[2], row[3], row[4], row[5], row[6], row[7] = row[3], '', row[1], row[2], row[4], '', row[5]
                    for i in range(len(row)):
                        a.append(row[i])
                    csv_writer.writerow(a)

        messagebox.showinfo('Внимание!', 'Файл отчета six_dep')

    label_six_dep_2 = tk.Label(root, text='Имя файла отчета six_dep_2', font=font)
    label_six_dep_2.pack()

    entry_six_dep_2 = tk.Entry(root)
    entry_six_dep_2.pack()

    btn_six_dep_2 = tk.Button(root, text='Создать', command=six_dep_2, font=font)
    btn_six_dep_2.pack()

    def six_dep_3():
        filename = entry_six_dep_3.get()
        filename = filename + '.csv'
        with open(filename, newline='') as csv_file_read:
            csv_reader = csv.reader(csv_file_read, delimiter=';')
            with open('Отчет_six_dep_3.csv', 'a', newline='') as csv_file_write:
                csv_writer = csv.writer(csv_file_write, delimiter=';')
                for row in csv_reader:
                    a = []
                    row[2], row[3], row[4] = row[4], row[2], row[3]
                    for i in range(len(row)):
                        a.append(row[i])
                    csv_writer.writerow(a)

        messagebox.showinfo('Внимание!', 'Файл отчета six_dep_3')

    label_six_dep_3 = tk.Label(root, text='Имя файла отчета six_dep_3', font=font)
    label_six_dep_3.pack()

    entry_six_dep_3 = tk.Entry(root)
    entry_six_dep_3.pack()

    btn_six_dep_3 = tk.Button(root, text='Создать', command=six_dep_3, font=font)
    btn_six_dep_3.pack()

    return root.mainloop()


if __name__ == '__main__':
    six_dep()
