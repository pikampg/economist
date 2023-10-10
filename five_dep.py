import csv
import tkinter as tk
from tkinter import messagebox

font = ('Times New Roman', 14) # шрифт


def five_dep():
    def five_dep_1():
        filename = entry_five_dep_1.get()
        filename = filename + '.csv'
        with open(filename, newline='') as csv_file_read:
            csv_reader = csv.reader(csv_file_read, delimiter=';')
            with open('Отчет_five_dep_1.csv', 'a', newline='') as csv_file_write:
                csv_writer = csv.writer(csv_file_write, delimiter=';')
                for row in csv_reader:
                    row[0], row[2], row[3], row[4], row[6], row[7] = row[9], row[6], row[2], row[3], row[7], row[8]
                    a = []
                    for i in range(len(row)):
                        if i == 8:
                            break
                        a.append(row[i])
                    csv_writer.writerow(a)

        messagebox.showinfo('Внимание!', 'Файл отчета по five_dep_1 создан')

    root = tk.Tk()
    root.title('five_dep')
    root.geometry('350x250')

    label_five_dep_1 = tk.Label(root, text='Имя файла отчета по five_dep_1', font=font)
    label_five_dep_1.pack()

    entry_five_dep_1 = tk.Entry(root)
    entry_five_dep_1.pack()

    btn_five_dep_1 = tk.Button(root, text='Создать', command=five_dep_1, font=font)
    btn_five_dep_1.pack()

    return root.mainloop()


if __name__ == '__main__':
    five_dep()
