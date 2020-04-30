cLevel = 'alpha one' # Command Level Authority
normal = ['beta two', 'charlie three', 'delta four'] # General Level Authority

def verify(cmd):
    if cmd in normal:
        return 1
    else:
        return 0