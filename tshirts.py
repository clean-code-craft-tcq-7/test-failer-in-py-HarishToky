
def size(cms):
    if cms < 38:
        return 'S'
    if 38 <= cms < 42:
        return 'M'
    return 'L'


assert(size(37) == 'S')
assert(size(40) == 'M')
assert(size(43) == 'L')
print("All is well (maybe!)")
