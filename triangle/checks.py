import check50
import check50.py

@check50.check()
def exists():
    """triangle.py exists."""
    check50.exists("triangle.py")
    check50.include("1.txt", "2.txt", "8.txt")

@check50.check(exists)
def syntax_ok(exists):
    """triangle.py has no syntax errors"""
    check50.py.compile("triangle.py")

@check50.check(syntax_ok)
def test_reject_negative():
    """rejects a height of -1"""
    check50.run("python3 triangle.py").stdin("-1", prompt=True).reject()

@check50.check(syntax_ok)
def test0():
    """rejects a height of 0"""
    check50.run("python3 triangle.py").stdin("0", prompt=True).reject()

@check50.check(syntax_ok)
def test1():
    """handles a height of 1 correctly"""
    out = check50.run("python3 triangle.py").stdin("1", prompt=True).stdout()
    check_pyramid(out, open("1.txt").read())

@check50.check(syntax_ok)
def test2():
    """handles a height of 2 correctly"""
    out = check50.run("python3 triangle.py").stdin("2", prompt=True).stdout()
    check_pyramid(out, open("2.txt").read())

@check50.check(syntax_ok)
def test23():
    """handles a height of 8 correctly"""
    out = check50.run("python3 triangle.py").stdin("8", prompt=True).stdout()
    check_pyramid(out, open("8.txt").read())

@check50.check(syntax_ok)
def test24():
    """rejects a height of 11, and then accepts a height of 2"""
    (check50.run("python3 triangle.py").stdin("11", prompt=True).reject()
            .stdin("2", prompt=True).stdout(open("2.txt")).exit(0))

def check_pyramid(output, correct):
    if output == correct:
        return

    output = output.splitlines()
    correct = correct.splitlines()

    help = None
    if len(output) == len(correct):
        if all(ol.rstrip() == cl for ol, cl in zip(output, correct)):
            help = "did you add too much trailing whitespace to the end of your pyramid?"
        elif all(ol[1:] == cl for ol, cl in zip(output, correct)):
            help = "are you printing an additional character at the beginning of each line?"

    raise check50.Mismatch(correct, output, help=help)
