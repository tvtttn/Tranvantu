print('Trần Văn Tú MSV 235752021610056')
input_file=open('D:/a.txt','r',encoding='utf-8')
for line in input_file:
    l=len(line)
    s=' '
    while(l>=1):
        s=s+line[l-1]
        l=l-1
    print(s)
input_file.close()