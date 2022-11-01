import os
import platform
import socket

system = os.environ
so = platform.system()
txt = open('informations.txt', 'w+')

if so == 'Windows':
    print(so, file=txt)
    print(f'Name: {system["USERNAME"]}', file=txt)
    print(f'Language: {system["LANG"]}', file=txt)
elif so == 'Linux':
    print(so, file=txt)
    print(f'Name: {system["LOGNAME"]}', file=txt)
    print(f'Language: {system["LANGUAGE"]}', file=txt)
    print(f'Distribution: {system["ORIGINAL_XDG_CURRENT_DESKTOP"]}', file=txt)
else:
    print('Not recognized.')

print(f'IP: {socket.gethostbyname(socket.gethostname())}', file=txt)

local = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
local.connect(("8.8.8.8", 80))
print(f'Local: {local.getsockname()[0]}', file=txt)