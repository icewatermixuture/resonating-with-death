import csv
import random
f = open('Grade.csv','w',encoding='utf-8-sig',newline='' ) 
csv_writer = csv.writer(f)
csv_writer.writerow(['Name','Number','Subject','Grade'])
n='Aalto','Aaron','Abbet','Aaron','Abbott','Abel','Abner','Abraham','Adair','Adam','Addison','Adolph''Baird','Baldwin','Bancroft','Bard','Barlow','Barnett','Baron','Barret','Barry','Bartholomew','Bart'
ssub='English','Math','Chinese ',' Physics', 'Chemistry', 'Computer'
for i in range(0,1000):
    X=random.choice(n)
    num=random.randint(0,100000)
    sub=random.choice(ssub)
    gr=random.randint(0,100)
    csv_writer.writerow([X,num,sub,gr])
f.close()
