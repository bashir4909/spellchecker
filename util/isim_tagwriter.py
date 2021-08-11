# script that goes through given dic file
# and writes appropriate tag

with open("../dictionaries/az.dic.OLD") as infile:
    taggedword = []
    for l in infile.readlines()[1:]:
        try:
            if l.split("/")[1][0]=="N":
                word = l.split("/")[0]
                if "-" in word:
                    raise NameError("DUH")
                try:
                    lastvowel = [c for c in word.lower() if c in "aıoueəiöü"][-1]
                    if lastvowel in "aı":
                        taggedword.append( (word, "MAM1H1X1HX") )
                    elif lastvowel in "ou":
                        taggedword.append( (word, "MAM3H3X3HZ") )
                    elif lastvowel in "eəi":
                        taggedword.append( (word, "MBM2H2X2HY") )
                    elif lastvowel in "öü":
                        taggedword.append( (word, "MBM4H4X4HW") )
                except IndexError:
                    print(word)
        except:
            print(l)


with open("../dictionaries/az.dic.new", "w") as outfile:
    for w in taggedword:
        outfile.write("/".join(w) + "\n")
