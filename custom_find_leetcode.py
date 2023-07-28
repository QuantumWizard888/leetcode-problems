
def custom_find(word: str, subword: str) -> int:
    
    if subword not in word:
        return -1
    
    else:
        for i in range(len(word)):
            if subword[0] == word[i]:
                if subword == word[i:i + len(subword)]:
                    return i


print(custom_find('echroichro', 'chrom'))
print(custom_find('echroinchrom', 'chrom'))
print(custom_find('echroinchromchrom', 'chrom'))





