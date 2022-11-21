#!/usr/bin/python3
# -*- coding: UTF-8 -*-
with open("loremipsum.txt") as f:
    lines = f.readlines()
    print("".join(lines))
