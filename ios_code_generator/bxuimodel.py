# -*- coding: utf-8 -*-
__author__ = 'banxi'
from ios_code_generator.generators import generate


def main():
    text = generate('uimodel')
    print(text)


if __name__ == '__main__':
    main()
