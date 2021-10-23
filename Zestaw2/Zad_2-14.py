def getLongestWord(string):
    return max(string.split(), key=len)

def getLongestWordLength(string):
    return len(max(string.split(), key=len))

if __name__ == "__main__":
    line = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n\
        \tNulla dui risus, laoreet eget viverra sit amet, interdum ac ex.\n\
        \tNulla commodo dui placerat rutrum accumsan. Sed at facilisis\n\
        metus. Suspendisse scelerisque vestibulum GvR ut vulputate.\n'
    print(getLongestWord(line))
    print(getLongestWordLength(line))
    