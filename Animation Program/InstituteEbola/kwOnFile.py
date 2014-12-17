import sys

def noRepeat():
    lines = open('ebola.txt', 'r').readlines()

    lines_set = set(lines)

    out = open('noRepeat.txt', 'w')

    for line in lines_set:
        out.write(line)

def getKW():
    #init keyword
    keyword = "ebola"
    newFile = "ebola.txt"
    # store lines of text and dates
    lines = []

    with open('tweetsAll.txt', 'r') as f:
        lines = f.read()

    # separate each entry
    text = lines.split("\n")

    # give new file a name and write all desired entries
    i = 1
    with open(newFile, 'w') as fout:
        for line in text:
            if keyword not in line.lower():
                i = i + 1
            else:
                fout.write(line)
                fout.write("\n")
            i = i + 1

if __name__ == '__main__':
    getKW()
    noRepeat()