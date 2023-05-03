import sys
import typing as t
import subprocess as sp

def runner() -> t.NoReturn:
    argstr = " ".join(sys.argv)
    cmd = "python task files"

    cp = sp.run(f"{cmd} --- {argstr}", shell=True)

    exit(cp.returncode)
