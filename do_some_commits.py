import subprocess

orig_book = list(open('Sherlock Holmes.txt', encoding='utf8').readlines())
my_book = 'my_book.txt'
my_writing_today = 'writing_today.txt'

def extend_book(nb_commit=2):
    with open(my_book, encoding='utf8') as f:
        current_content = f.read()
        
    idx = len(current_content.split('\n'))
    
    for _ in range(nb_commit):
        content = '\n'.join( orig_book[idx:idx+30] )

        f2 = open(my_writing_today, 'w', encoding='utf8')
        f2.write(content)
        f2.close()

        f3 = open(my_book, 'a', encoding='utf8')
        f3.write(content)
        f3.close()

        print('Commit for lines %d-%d' % (idx, idx+30))
        subprocess.call(['git', 'add', my_book, my_writing_today])
        subprocess.call(['git', 'commit', '-m', 'writing lines %d to %d' % (idx, idx+29)])

        idx += 30


extend_book(100)