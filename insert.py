import csv
import random
f = open('Grade.csv','w',encoding='utf-8-sig',newline='' )
csv_writer = csv.writer(f)
def funA(a,b,c,d, e,f,g,h,i,j,*args):#得分点4, 使用不定长参数的函数
    csv_writer.writerow([a,b,c,d])
    n=args
    ssub=e,f,g,h,i,j
    for i in range(1,1000):#随机写入1000条数据
        X=random.choice(n)
        num=random.randint(0,100000)
        sub=random.choice(ssub)
        gr=random.randint(0,100)
        csv_writer.writerow([X,num,sub,gr])
funA('Name','Number','Subject','Grade','English','Math','Chinese','Physics', 'Chemistry', 'Computer','Aalto','Aaron','Abbet','Aaron','Abbott','Abel','Abner','Abraham','Adair','Adam','Addison','Adolph''Baird','Baldwin','Bancroft','Bard','Barlow','Barnett','Baron','Barret','Barry','Bartholomew','Bart')
f.close()
