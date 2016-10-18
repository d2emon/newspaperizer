#! /usr/bin/python
def install(requirements):
    import pip
    pip.main(['install', '-r', requirements])


if __name__ == "__main__":
    import os
    path = os.path.dirname(os.path.abspath(__file__))
    install(os.path.join(path, 'requirements.txt'))
