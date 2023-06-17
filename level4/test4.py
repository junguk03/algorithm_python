def solution(word):
    length = len(word)
    for i in range(length//2):
        if word[i] != word[-i]:
            return False
    return True