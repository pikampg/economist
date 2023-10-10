import csv
import tkinter as tk
from tkinter import messagebox

font = ('Times New Roman', 14) # шрифт


def four_dep():
    def four_dep_1():
        filename = entry_four_dep_1.get()
        filename = filename + '.csv'
        with open(filename, newline='') as csv_file_read:
            csv_reader = csv.reader(csv_file_read, delimiter=';')
            with open('Отчет_four_dep_1.csv', 'a', newline='') as csv_file_write:
                csv_writer = csv.writer(csv_file_write, delimiter=';')
                for row in csv_reader:
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11] = \
                        row[2], row[7], row[8], row[9], row[5], row[14], row[30], row[31], row[33], row[34], row[35], row[36]
                    a = []
                    for i in range(len(row)):
                        a.append(row[i])
                        if i == 11:
                            break

                    csv_writer.writerow(a)
        messagebox.showinfo('Внимание!', 'Файл отчета по four_dep_1 создан')

    root = tk.Tk()
    root.title('four_dep')
    root.geometry('350x200')

    label_four_dep = tk.Label(root, text='Имя файла отчета по four_dep', font=font)
    label_four_dep.pack()

    entry_four_dep = tk.Entry(root)
    entry_four_dep.pack()

    btn_four_dep = tk.Button(root, text='Создать', command=four_dep_1, font=font)
    btn_four_dep.pack()

    return root.mainloop()


if __name__ == '__main__':
    four_dep()
