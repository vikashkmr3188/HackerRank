dict_mag = dict()
dict_ran = dict()

def checkMagazine(magazine, note):
    for i in note:
        if i in magazine:
            magazine.remove(i)
        else:
            return ("No")
    return ("Yes")

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
print (ransom_note(magazine, ransom))

    
