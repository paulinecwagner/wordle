from sys import argv

if "debug" not in argv:
    print_ = lambda *_, **__: None
else:
    print_ = print