import csv
import tkinter as tk
from tkinter import messagebox
import datetime

font = ('Times New Roman', 14) # шрифт


def create_report():
    name_report = []

    def get_filename(): # делает список из файлов, которые нужно объединить
        filename = entry_get_filename.get()
        filename = filename + '.csv'
        name_report.append(filename)
        lbl = tk.Label(root, text=filename)
        lbl.pack()
        messagebox.showinfo('Внимание!', 'Файл добавлен')

    def create_report():
        name_department = []
        for name_rep in name_report:
            with open(name_rep, newline='') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=';')
                for row in csv_reader:
                    if row[0] == '':
                        continue
                    elif row[0] in '0123456789':
                        continue
                    else:
                        name_department.append(row[0])

        name_department = sorted(list(set(name_department)))

        date_now = (str(datetime.date.today()).replace('-', '_') + '_отчет' + '.csv')  # date_now - Имя файла отчета с сегодняшней датой

        with open(date_now, 'a', newline='') as csv_file_w:
            csv_writer = csv.writer(csv_file_w, delimiter=';')
            csv_writer.writerow(['1', '2', '3', '4', '5', '6',
                                 '7', '8', '9', '10', '11', '12'])

        for name_dep in name_department:
            true_list = []
            for name_rep in name_report:
                with open(name_rep, newline='') as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=';')
                    for i in csv_reader:
                        if name_dep in i and name_dep == i[0]:
                            true_list.append(i)

            with open(date_now, 'a', newline='') as csv_file_w:
                csv_writer = csv.writer(csv_file_w, delimiter=';')
                for j in true_list:
                    csv_writer.writerow(j)

        messagebox.showinfo('Внимание!', 'Отчет создан')

    root = tk.Tk()
    root.title('final_report')
    root.geometry('250x400')

    filename_var = tk.StringVar()

    label = tk.Label(root, text='Название файла отчета', font=font)
    label.pack()

    entry_get_filename = tk.Entry(root, textvariable=filename_var)
    entry_get_filename.pack()

    btn_get_filename = tk.Button(root, text='   OK   ', command=get_filename, font=font)
    btn_get_filename.pack()

    btn_report = tk.Button(root, text='Create report', command=create_report, font=font)
    btn_report.pack()

    return root.mainloop()


if __name__ == '__main__':
    create_report()
