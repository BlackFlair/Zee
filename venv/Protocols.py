import Authorization

# --------------- PROTOCOLS ---------------

def addAuth():
    newAuth = '' # Input from Audio.py
    Authorization.normal.append(newAuth)

def protocols(x):
    switcher = {
        'addAuth' : addAuth()
    }
    return switcher.get(x, "protocol does not exist.")


# --------------- OVERRIDES ---------------

def cmdLevel():
    Authorization.normal = Authorization.cLevel
    return 'command level override successful.'

def override(x):
    switcher = {
        'cmdLevel' : cmdLevel()
    }
    return switcher.get(x, "override does not exist.")
