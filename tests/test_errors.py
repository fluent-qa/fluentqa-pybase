from qpybase.errors import GeneralError

from rich import print
def test_generic_error():

    e = GeneralError()
    e.log()
    print(e.message)
