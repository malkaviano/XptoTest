# coding=utf-8

from app import pipeline
import sys
from values import DB_PATH


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else DB_PATH

    pipeline(path)


if __name__ == '__main__':
    main()
