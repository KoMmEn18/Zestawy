def splitWithUndercourse(string):
    return '_'.join(string[i] for i in range(0, len(string)))

if __name__ == "__main__":
    word = 'word'
    print(splitWithUndercourse(word))