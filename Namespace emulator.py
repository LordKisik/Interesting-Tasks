'''Программа, которая эмулирует работу с пространствами имен. Реализована
     поддержка создания пространств имен и добавление в них переменных.'''

# В программе на вход подаются следующие запросы:
# 1) create <namespace> <parent> –  создать новое пространство имен
#    с именем <namespace> внутри пространства <parent>

# 2) add <namespace> <var> – добавить в пространство <namespace>
#    переменную <var>

# 3) get <namespace> <var> – получить имя пространства, из которого будет взята
#    переменная <var> при запросе из пространства <namespace>, или None,
#    если такого пространства не существует

scopes = {'global': {'parent': None, 'variables': []}}


def create(a, b):
    scopes[a] = {'parent': None, 'variables': []}
    scopes[a]['parent'] = b


def add(a, b):
    scopes[a]['variables'] += [b]


def get(a, b, c):
    if a == 'global' and b not in c[a]['variables']:
        return None
    if b in c[a]['variables']:
        return a
    else:
        a = c[a]['parent']
        return get(a, b, c)


GET = []
n = int(input())
for i in range(n):
    cmd, namesp, arg = input().split()
    if cmd == 'create':
        create(namesp, arg)
    elif cmd == 'add':
        add(namesp, arg)
    elif cmd == 'get':
        GET += [get(namesp, arg, scopes)]
for i in range(len(GET)):
    print(GET[i])
