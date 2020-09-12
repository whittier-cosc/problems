import check50
import check50.py

@check50.check()
def exists():
    """credit.py exists."""
    check50.exists("credit.py")

@check50.check(exists)
def syntax_ok(exists):
    """credit.py has no syntax errors"""
    check50.py.compile("credit.py")

@check50.check(syntax_ok)
def test1():
    """identifies 31406215 as OK"""
    check50.run("python3 credit.py").stdin("31406215", prompt=True).stdout("OK").exit()

@check50.check(syntax_ok)
def test2():
    """identifies 00000000 as OK"""
    check50.run("python3 credit.py").stdin("00000000", prompt=True).stdout("OK").exit()

@check50.check(syntax_ok)
def test3():
    """identifies 12345678 as INVALID"""
    check50.run("python3 credit.py").stdin("12345678", prompt=True).stdout("INVALID").exit(0)

@check50.check(syntax_ok)
def test4():
    """identifies 12341234 as INVALID"""
    check50.run("python3 credit.py").stdin("12341234", prompt=True).stdout("INVALID").exit()

@check50.check(syntax_ok)
def test5():
    """identifies 12341214 as OK"""
    check50.run("python3 credit.py").stdin("12341214", prompt=True).stdout("OK").exit()

@check50.check(syntax_ok)
def test6():
    """identifies 56785678 as OK"""
    check50.run("python3 credit.py").stdin("56785678", prompt=True).stdout("OK").exit()

@check50.check(syntax_ok)
def test7():
    """identifies 51785678 as OK"""
    check50.run("python3 credit.py").stdin("51785678", prompt=True).stdout("OK").exit()

@check50.check(syntax_ok)
def test8():
    """identifies 53785678 as INVALID"""
    check50.run("python3 credit.py").stdin("53785678", prompt=True).stdout("INVALID").exit()

