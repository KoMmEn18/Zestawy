def getStringOfFirstChars(string):
    return ''.join(word[0] for word in string.split())

def getStringOfLastChars(string):
    return ''.join(word[-1] for word in string.split())

if __name__ == "__main__":
    line = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n\
        \tNulla dui risus, laoreet eget viverra sit amet, interdum ac ex.\n\
        \tNulla commodo dui placerat rutrum accumsan. Sed at facilisis\n\
        metus. Suspendisse scelerisque vestibulum GvR ut vulputate.\n'
    print(getStringOfFirstChars(line))
    print(getStringOfLastChars(line))