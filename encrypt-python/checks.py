import check50
import check50.py

@check50.check()
def exists():
    """encrypt.py exists."""
    check50.exists("encrypt.py")

@check50.check(exists)
def syntax_ok(exists):
    """encrypt.py has no syntax errors"""
    check50.py.compile("encrypt.py")

@check50.check(syntax_ok)
def encrypts_a_as_b():
    """encrypts "a" as "b" using 1 as key"""
    check50.run("python3 encrypt.py 1").stdin("a").stdout("ciphertext:\s*b\n", "ciphertext: b\n").exit(0)

@check50.check(syntax_ok)
def encrypts_barfoo_as_yxocll():
    """encrypts "barfoo" as "yxocll" using 23 as key"""
    check50.run("python3 encrypt.py 23").stdin("barfoo").stdout("ciphertext:\s*yxocll\n", "ciphertext: yxocll\n").exit(0)

@check50.check(syntax_ok)
def encrypts_BARFOO_as_EDUIRR():
    """encrypts "BARFOO" as "EDUIRR" using 3 as key"""
    check50.run("python3 encrypt.py 3").stdin("BARFOO").stdout("ciphertext:\s*EDUIRR\n", "ciphertext: EDUIRR\n").exit(0)

@check50.check(syntax_ok)
def encrypts_BaRFoo_FeVJss():
    """encrypts "BaRFoo" as "FeVJss" using 4 as key"""
    check50.run("python3 encrypt.py 4").stdin("BaRFoo").stdout("ciphertext:\s*FeVJss\n", "ciphertext: FeVJss\n").exit(0)

@check50.check(syntax_ok)
def checks_for_handling_non_alpha():
    """encrypts "world, say hello!" as "iadxp, emk tqxxa!" using 12 as key"""
    check50.run("python3 encrypt.py 12").stdin("world, say hello!").stdout("ciphertext:\s*iadxp, emk tqxxa!\n", "ciphertext: iadxp, emk tqxxa!\n").exit(0)

@check50.check(syntax_ok)
def handles_no_arg():
    """handles lack of sys.argv[1]"""
    check50.run("python3 encrypt.py").exit(1)

@check50.check(syntax_ok)
def handles_negative_arg():
    """handles negative key"""
    check50.run("python3 encrypt.py -1").exit(1)

@check50.check(syntax_ok)
def handles_arg_too_big():
    """handles key greater than 25"""
    check50.run("python3 encrypt.py 26").exit(1)

@check50.check(syntax_ok)
def handles_too_many_argv():
    """handles too many command-line args"""
    check50.run("python3 encrypt.py 1 2").exit(1)
