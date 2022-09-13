from os.path import exists, isdir, join
from os import mkdir, getcwd
def DB_Existance():
    return (exists(join(getcwd(), "DB", "all.dbtmp")) and exists(join(getcwd(), "DB", "out.dbtmp")))

def read_DB():
    if not DB_Existance():
        if not isdir(join(getcwd(), "DB")):
            mkdir(join(getcwd(), "DB"))
        f = open(join(getcwd(), "DB","all.dbtmp"), "w")
        f.close()
        f = open(join(getcwd(), "DB","out.dbtmp"), "w")
        f.close()
    all_read = list()
    out_read = list()
    f = open(join(getcwd(), "DB","all.dbtmp"), "r")
    for i in f:
        sub = i.split(':')
        sub[0] = sub[0].replace('\n','')
        sub[1] = sub[1].replace('\n','')
        sub[2] = sub[2].replace('\n','')
        all_read.append(sub)
    f = open(join(getcwd(), "DB","out.dbtmp"), "r")
    for i in f:
        sub = i.split(':')
        if len(sub) == 3:
            sub[0] = sub[0].replace('\n','')
            sub[1] = sub[1].replace('\n','')
            sub[2] = sub[2].replace('\n','')
            out_read.append(sub)
    return (all_read, out_read)

def search_DB(parm_type, parm_data):
    # Search if book exist in the library
    lib = read_DB()[0]
    return_li = list()
    for i in lib:
        if parm_type == 'title':
            if i[1] == parm_data:
                return_li.append(i)
        elif parm_type == 'author':
            if i[0] == parm_data:
                return_li.append(i)
        elif parm_type == 'code':
            if i[2] == parm_data:
                return_li.append(i)
    return return_li

def borrowable_DB(parm_type, parm_data):
    # Search if book is borrowable
    lib = read_DB()[1]
    return_li = list()
    for i in lib:
        if parm_type == 'title':
            if i[1] == parm_data:
                return_li.append(i)
        elif parm_type == 'author':
            if i[0] == parm_data:
                return_li.append(i)
        elif parm_type == 'code':
            if i[2] == parm_data:
                return_li.append(i)
    return return_li

def borrow_from(book_code):
    if len(borrowable_DB('code', book_code)) > 0:
        return 0
    elif len(search_DB('code', book_code)) == 0:
        return 1
    else:
        f = read_DB()[0]
        new_f = read_DB()[1]
        for i in f:
            if i[2] == book_code:
                new_f.append(i)
                break
        f = open(join(getcwd(), "DB","out.dbtmp"), "w")
        for i in new_f:
            line = i[0] + ":" + i[1] + ":" + i[2] + "\n"
            f.write(line)
        f.close()
        return 2

def return_to(book_code):
    if len(borrowable_DB('code', book_code)) > 0:
        f = read_DB()[1]
        new_f = list()
        for i in f:
            if i[2] != book_code:
                new_f.append(i)
        f = open(join(getcwd(), "DB","out.dbtmp"), "w")
        for i in new_f:
            line = i[0] + ":" + i[1] + ":" + i[2] + "\n"
            f.write(line)
        f.close()
        return 1
    if len(search_DB('code', book_code)) == 0:
        return 0
    elif len(borrowable_DB('code', book_code)) == 0:
        return 2

def new_Book(auth, title, code):
    lib_f = read_DB()[0]
    for i in lib_f:
        if i[2] == code:
            return False
    lib_f.append([auth, title, code])
    f = open(join(getcwd(), "DB","all.dbtmp"), "w")
    for i in lib_f:
        line = i[0] + ":" + i[1] + ":" + i[2] + "\n"
        f.write(line)
    f.close()
    return True
    
def remove_Book(code):
    lib_f = read_DB()[0]
    out_f = read_DB()[1]
    new_f = list()
    for i in lib_f:
        if i[2] != code:
            new_f.append(i)
    if len(new_f) == len(lib_f):
        return False
    for i in out_f:
        if i[2] == code:
            return False
    f = open(join(getcwd(), "DB","all.dbtmp"), "w")
    for i in new_f:
        line = i[0] + ":" + i[1] + ":" + i[2] + "\n"
        f.write(line)
    f.close()
    return True