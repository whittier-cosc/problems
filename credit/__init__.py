import check50
import check50.c

@check50.check()
def exists():
    """credit.c exists."""
    check50.exists("credit.c")

@check50.check(exists)
def compiles():
    """credit.c compiles."""
    check50.c.compile("credit.c", lcs50=True)

@check50.check(compiles)
def test1():
    """identifies 31406215 as VALID"""
    check50.run("./credit").stdin("31406215").stdout("VALID\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test2():
    """identifies 00000000 as VALID"""
    check50.run("./credit").stdin("00000000").stdout("VALID\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test3():
    """identifies 12345678 as INVALID"""
    check50.run("./credit").stdin("12345678").stdout("INVALID\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test4():
    """identifies 12341234 as INVALID"""
    check50.run("./credit").stdin("12341234").stdout("INVALID\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test5():
    """identifies 12341214 as VALID"""
    check50.run("./credit").stdin("12341214").stdout("VALID\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test6():
    """identifies 56785678 as VALID"""
    check50.run("./credit").stdin("56785678").stdout("VALID\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test7():
    """identifies 51785678 as VALID"""
    check50.run("./credit").stdin("51785678").stdout("VALID\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test8():
    """identifies 53785678 as INVALID"""
    check50.run("./credit").stdin("53785678").stdout("INVALID\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test_reject_foo():
    """rejects a non-numeric input of "foo" """
    check50.run("./credit").stdin("foo").reject()

@check50.check(compiles)
def test_reject_empty():
    """rejects a non-numeric input of "" """
    check50.run("./credit").stdin("").reject()
