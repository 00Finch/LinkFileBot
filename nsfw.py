import sys

def DetectNSFW(word):
    nsfw = open("nsfw.txt", "r").readlines()
    word = word.lower()
    base = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    final= ['k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    newWord = ''
    for c in range(len(word)):
        try:
            newWord += final[base.index(word[c])]
        except:
            continue
    for w in nsfw:
        if w.strip() == newWord: return True
    return False

def DetectSentance(sentance):
    for word in sentance.split(' '):
        if DetectNSFW(word):
            return True
    else:
        return False

if __name__ == "__main__":
    print(DetectNSFW(sys.argv[1]))
