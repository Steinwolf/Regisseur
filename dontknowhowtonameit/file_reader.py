# Read the token --- made to hide the token in Github --- Hi Git-user 😀
f = open("config/token.txt", "r")
TOKEN = f.read()
f.close()

# Read file permission
f = open('config/command_permission.txt', 'r', encoding='utf-8 ')
permission_file = f.readlines()
f.close()

# Read file help
f = open('config/help.txt', 'r', encoding='utf-8')
help_file = f.read()
f.close()

permission = {}

for l in permission_file:
    if l.endswith('\\n'):
        l = l[0:-2]
    l = l.split('.')
    permission.update({l[0]: l[1]})
