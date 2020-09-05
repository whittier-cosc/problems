import check50
import check50.py

@check50.check()
def exists():
    """alterego.py exists."""
    check50.exists("alterego.py")

@check50.check(exists)
def syntax_ok():
    """alterego.py has no syntax errors"""
    check50.py.compile("alterego.py")

@check50.check(syntax_ok)
def ScamperElmwood():
    """Scamper Elmwood"""
    check50.run("python3 alterego.py").stdout("first pet.", regex=True).stdout("** ", regex=False).stdin("Scamper", prompt=False).stdout("street you lived on.", regex=True).stdout("** ", regex=False).stdin("Elmwood", prompt=False).stdout("Thank you.").stdout("alter ego is Scamper Elmwood").exit()

@check50.check(syntax_ok)
def ZiggyDingman():
    """Ziggy Dingman"""
    check50.run("python3 alterego.py").stdout("first pet.", regex=True).stdout("** ", regex=False).stdin("Ziggy", prompt=False).stdout("street you lived on.", regex=True).stdout("** ", regex=False).stdin("Dingman", prompt=False).stdout("Thank you.").stdout("alter ego is Ziggy Dingman").exit()
