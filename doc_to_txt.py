import os
def convert(filename):
    x = os.popen('antiword ' + filename).read()
    return x