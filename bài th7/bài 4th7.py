print('Trần Văn Tú MSV 235752021610056')
def file_read_from_head(fname, nlines):
    from itertools import islice
    with open(fname, encoding='utf-8') as f:
        for line in islice(f, nlines):
            print(line)
file_read_from_head('D:/a.txt',2)