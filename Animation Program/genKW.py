import sys

"""
Use a generator expression to evaluate lines of text for
a select keyword.
"""
def genKW(text_list):
    keyword = "ebola"
    return( list(line for line in text_list if keyword not in line.lower()) )

"""
Main driver
"""
def main():
    newFile = "ebola.txt"
    # store lines of text and dates
    lines = ()

    with open('tweetsAll.txt', 'r') as f:
        lines = f.read()

    # separate each entry
    text = lines.split("\n")
    # call generator function
    x = genKW(text)
    x = x.split("\n")
    with open('ebola.txt', 'w') as f:
        for kw in x:
            f.write(kw)

if __name__ == '__main__':
    main()