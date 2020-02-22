import check50
import check50.c

@check50.check()
def exists():
    """username.c exists."""
    check50.exists("username.c")

@check50.check(exists)
def compiles():
    """username.c compiles."""
    check50.c.compile("username.c", lcs50=True)

@check50.check(compiles)
def gina_jones():
    """'Gina Jones' --> <gjones>"""
    check50.run("./username").stdin("Gina Jones").stdout("<gjones>").exit(0)

@check50.check(compiles)
def judith_longname():
    """'Judith Longname' --> <jlongnam>"""
    check50.run("./username").stdin("Judith Longname").stdout("<jlongnam>").exit(0)

@check50.check(compiles)
def buford():
    """'Buford McGillicuddy' --> <bmcgilli>"""
    check50.run("./username").stdin("Buford McGillicuddy").stdout("<bmcgilli>").exit(0)

@check50.check(compiles)
def handles_leading_spaces():
    """'   Brad Lee' --> <blee>"""
    check50.run("./username").stdin("   Brad Lee").stdout("<blee>").exit(0)

@check50.check(compiles)
def handles_middle_spaces():
    """'Brad        Lee' --> <blee>"""
    check50.run("./username").stdin("Brad        Lee").stdout("<blee>").exit(0)

@check50.check(compiles)
def handles_trailing_spaces():
    """'Brad Lee   ' --> <blee>"""
    check50.run("./username").stdin("Brad Lee   ").stdout("<blee>").exit(0)

@check50.check(compiles)
def handles_all_spaces():
    """'   Immanuel    Kant   ' --> <ikant>"""
    check50.run("./username").stdin("   Immanuel   Kant   ").stdout("<ikant>").exit(0)

@check50.check(compiles)
def handles_all_spaces_and_long_last():
    """'   Judith    Longname   ' --> <jlongnam>"""
    check50.run("./username").stdin("   Judith   Longname   ").stdout("<jlongnam>").exit(0)

