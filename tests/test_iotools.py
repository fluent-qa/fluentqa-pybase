#!/usr/bin/env python
from qpybase.builtins import iotools


def test_write_lines():
    iotools.write_lines(["test", "test", "test"], "temp_java.txt")


def test_copy_file():
    result = iotools.copy_files("temp_java.txt")
    iotools.write_lines(result, "temp-1.txt")
