#!/usr/bin/python3
""" Copy and format file form arg 1 and name it with arg 2 value """
from sys import argv, stderr


if __name__ == "__main__":
    """ Copy files or exit and error to stderr """
    if len(argv) < 3:
        stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)
    try:
        with open(argv[1], "r") as f1, open(argv[2], "w") as f2:
            f1_l = f1.readlines()
            for line in f1_l:
                if line[0] == "#":
                    hlvl = len(line) - len(line.lstrip("#"))
                    l = line.strip(" #\n")
                    f2.write("<h{}>".format(hlvl) + l + "</h{}>".format(hlvl) + "\n")
                else:
                    f2.write(line)
        exit(0)
    except IOError:
        stderr.write("Missing {}\n".format(argv[1]))
        exit(1)
