import os
from settings import APP_STATIC
with open(os.path.join(APP_STATIC, 'hello.txt')) as f:
    s = f.read()
    f.close()
    return str(s)
