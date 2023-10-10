import csv
import tkinter as tk
from tkinter import messagebox

font = ('Times New Roman', 14) # шрифт


def seven_dep():
    root = tk.Tk()
    root.title('seven_dep')
    root.geometry('350x250')

    def seven_dep_1():
        filename = entry_seven_dep_1.get()
        filename = filename + '.csv'
        with open(filename, newline='') as csv_file_read:
            csv_reader = csv.reader(csv_file_read, delimiter=';')
            with open('Отчет_seven_dep_1.csv', 'a', newline='') as csv_file_write:
                csv_writer = csv.writer(csv_file_write, delimiter=';')
                for row in csv_reader:
                    a = []
                    row[2], row[3], row[4] = row[4], row[2], row[3]
                    for i in range(len(row)):
                        a.append(row[i])
                        if i == 6:
                            break
                    csv_writer.writerow(a)

        messagebox.showinfo('Внимание!', 'Файл отчета по seven_dep_1')

    label_seven_dep_1 = tk.Label(root, text='Имя файла отчета seven_dep_1', font=font)
    label_seven_dep_1.pack()

    entry_seven_dep_1 = tk.Entry(root)
    entry_seven_dep_1.pack()

    btn_seven_dep_1 = tk.Button(root, text='Создать', command=seven_dep_1, font=font)
    btn_seven_dep_1.pack()

    return root.mainloop()


if __name__ == '__main__':
    seven_dep()
