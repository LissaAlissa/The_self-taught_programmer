import csv

s = [["Звездные войны", "Терминатор", "Искусственный интелект"], ["Дурак", "Матильда", "Левиафан"], ["Люди в черном", "Я - робот", "Эволюция"]]

with open('movie.csv', 'w') as f:
    w =  csv.writer(f, delimiter=',')
    w.writerow(s[0])
    w.writerow(s[1])
    w.writerow(s[2])
