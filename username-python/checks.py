import check50
import check50.py

@check50.check()
def exists():
    """username.py exists."""
    check50.exists("username.py")
    
@check50.check(exists)
def syntax_ok():
    """username.py has no syntax errors"""
    check50.py.compile("username.py")
    
@check50.check(syntax_ok)
def Gina_Jones():
    """Gina Jones"""
    check50.run("python3 username.py").stdin("Gina Jones").stdout("<gjones>", regex=False).exit(0)
    
@check50.check(syntax_ok)
def judith_longname():
    """'Judith Longname' --> <jlongnam>"""
    check50.run("python3 username.py").stdin("Judith Longname").stdout("<jlongnam>", regex=False).exit(0)

@check50.check(syntax_ok)
def buford():
    """'Buford McGillicuddy' --> <bmcgilli>"""
    check50.run("python3 username.py").stdin("Buford McGillicuddy").stdout("<bmcgilli>", regex=False).exit(0)

@check50.check(syntax_ok)
def handles_leading_spaces():
    """'   Brad Lee' --> <blee>"""
    check50.run("python3 username.py").stdin("   Brad Lee").stdout("<blee>", regex=False).exit(0)

@check50.check(syntax_ok)
def handles_middle_spaces():
    """'Brad        Lee' --> <blee>"""
    check50.run("python3 username.py").stdin("Brad        Lee").stdout("<blee>", regex=False).exit(0)

@check50.check(syntax_ok)
def handles_trailing_spaces():
    """'Brad Lee   ' --> <blee>"""
    check50.run("python3 username.py").stdin("Brad Lee   ").stdout("<blee>", regex=False).exit(0)

@check50.check(syntax_ok)
def handles_all_spaces():
    """'   Immanuel    Kant   ' --> <ikant>"""
    check50.run("python3 username.py").stdin("   Immanuel   Kant   ").stdout("<ikant>", regex=False).exit(0)

@check50.check(syntax_ok)
def handles_all_spaces_and_long_last():
    """'   Judith    Longname   ' --> <jlongnam>"""
    check50.run("python3 username.py").stdin("   Judith   Longname   ").stdout("<jlongnam>", regex=False).exit(0)