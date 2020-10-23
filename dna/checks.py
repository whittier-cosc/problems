import check50
import check50.py

@check50.check()
def exists():
    """dna.py exists."""
    check50.exists("dna.py")

@check50.check(exists)
def syntax_ok(exists):
    """dna.py has no syntax errors"""
    check50.py.compile("dna.py")

@check50.check(syntax_ok)
def seq01():
    """small.csv 1.txt -> Bob"""
    check50.run("python3 dna.py databases/small.csv sequences/1.txt").stdout("Bob").exit()

@check50.check(syntax_ok)
def seq02():
    """small.csv 2.txt -> No match"""
    check50.run("python3 dna.py databases/small.csv sequences/2.txt").stdout("[Nn]o [Mm]atch").exit()

@check50.check(syntax_ok)
def seq03():
    """small.csv 3.txt -> No match"""
    check50.run("python3 dna.py databases/small.csv sequences/3.txt").stdout("[Nn]o [Mm]atch").exit()

@check50.check(syntax_ok)
def seq04():
    """small.csv 4.txt -> Alice"""
    check50.run("python3 dna.py databases/small.csv sequences/4.txt").stdout("Alice").exit()

@check50.check(syntax_ok)
def seq05():
    """large.csv 5.txt -> Lavender"""
    check50.run("python3 dna.py databases/large.csv sequences/5.txt").stdout("Lavender").exit()

@check50.check(syntax_ok)
def seq06():
    """large.csv 6.txt -> Luna"""
    check50.run("python3 dna.py databases/large.csv sequences/6.txt").stdout("Luna").exit()

@check50.check(syntax_ok)
def seq07():
    """large.csv 7.txt -> Ron"""
    check50.run("python3 dna.py databases/large.csv sequences/7.txt").stdout("Ron").exit()

@check50.check(syntax_ok)
def seq08():
    """large.csv 8.txt -> Ginny"""
    check50.run("python3 dna.py databases/large.csv sequences/8.txt").stdout("Ginny").exit()

@check50.check(syntax_ok)
def seq09():
    """large.csv 9.txt -> Draco"""
    check50.run("python3 dna.py databases/large.csv sequences/9.txt").stdout("Draco").exit()

@check50.check(syntax_ok)
def seq10():
    """large.csv 10.txt -> Albus"""
    check50.run("python3 dna.py databases/large.csv sequences/10.txt").stdout("Albus").exit()

@check50.check(syntax_ok)
def seq11():
    """large.csv 11.txt -> Hermione"""
    check50.run("python3 dna.py databases/large.csv sequences/11.txt").stdout("Hermione").exit()

@check50.check(syntax_ok)
def seq12():
    """large.csv 12.txt -> Lily"""
    check50.run("python3 dna.py databases/large.csv sequences/12.txt").stdout("Lily").exit()

@check50.check(syntax_ok)
def seq13():
    """large.csv 13.txt -> No match"""
    check50.run("python3 dna.py databases/large.csv sequences/13.txt").stdout("[Nn]o [Mm]atch").exit()

@check50.check(syntax_ok)
def seq14():
    """large.csv 14.txt -> Severus"""
    check50.run("python3 dna.py databases/large.csv sequences/14.txt").stdout("Severus").exit()

@check50.check(syntax_ok)
def seq15():
    """large.csv 15.txt -> Sirius"""
    check50.run("python3 dna.py databases/large.csv sequences/15.txt").stdout("Sirius").exit()

@check50.check(syntax_ok)
def seq16():
    """large.csv 16.txt -> No match"""
    check50.run("python3 dna.py databases/large.csv sequences/16.txt").stdout("[Nn]o [Mm]atch").exit()

@check50.check(syntax_ok)
def seq17():
    """large.csv 17.txt -> Harry"""
    check50.run("python3 dna.py databases/large.csv sequences/17.txt").stdout("Harry").exit()

@check50.check(syntax_ok)
def seq18():
    """large.csv 18.txt -> No match"""
    check50.run("python3 dna.py databases/large.csv sequences/18.txt").stdout("[Nn]o [Mm]atch").exit()

@check50.check(syntax_ok)
def seq19():
    """large.csv 19.txt -> Fred"""
    check50.run("python3 dna.py databases/large.csv sequences/19.txt").stdout("Fred").exit()

@check50.check(syntax_ok)
def seq20():
    """large.csv 20.txt -> No match"""
    check50.run("python3 dna.py databases/large.csv sequences/20.txt").stdout("[Nn]o [Mm]atch").exit()


