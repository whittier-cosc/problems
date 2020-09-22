import check50
import check50.c

@check50.check()
def exists():
    """encrypt.c exists."""
    check50.exists("encrypt.c")

@check50.check(exists)
def compiles():
    """encrypt.c compiles."""
    check50.c.compile("encrypt.c", lcs50=True)

@check50.check(compiles)
def encrypts_a_as_b():
    """encrypts "a" as "b" using 1 as key"""
    check50.run("./encrypt 1").stdin("a").stdout("ciphertext:\s*b\n", "ciphertext: b\n").exit(0)

@check50.check(compiles)
def encrypts_barfoo_as_yxocll():
    """encrypts "barfoo" as "yxocll" using 23 as key"""
    check50.run("./encrypt 23").stdin("barfoo").stdout("ciphertext:\s*yxocll\n", "ciphertext: yxocll\n").exit(0)

@check50.check(compiles)
def encrypts_BARFOO_as_EDUIRR():
    """encrypts "BARFOO" as "EDUIRR" using 3 as key"""
    check50.run("./encrypt 3").stdin("BARFOO").stdout("ciphertext:\s*EDUIRR\n", "ciphertext: EDUIRR\n").exit(0)

@check50.check(compiles)
def encrypts_BaRFoo_FeVJss():
    """encrypts "BaRFoo" as "FeVJss" using 4 as key"""
    check50.run("./encrypt 4").stdin("BaRFoo").stdout("ciphertext:\s*FeVJss\n", "ciphertext: FeVJss\n").exit(0)

@check50.check(compiles)
def checks_for_handling_non_alpha():
    """encrypts "world, say hello!" as "iadxp, emk tqxxa!" using 12 as key"""
    check50.run("./encrypt 12").stdin("world, say hello!").stdout("ciphertext:\s*iadxp, emk tqxxa!\n", "ciphertext: iadxp, emk tqxxa!\n").exit(0)

@check50.check(compiles)
def handles_no_arg():
    """handles lack of argv[1]"""
    check50.run("./encrypt").exit(1)

@check50.check(compiles)
def handles_negative_arg():
    """handles negative key"""
    check50.run("./encrypt -1").exit(1)

@check50.check(compiles)
def handles_arg_too_big():
    """handles key greater than 25"""
    check50.run("./encrypt 26").exit(1)

@check50.check(compiles)
def handles_too_many_argv():
    """handles too many command-line args"""
    check50.run("./encrypt 1 2").exit(1)
