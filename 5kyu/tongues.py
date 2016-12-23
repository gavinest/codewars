'''
Tongues

Gandalf's writings have long been available for study, but no one has yet figured out what language they are written in. Recently, due to programming work by a hacker known only by the code name ROT13, it has been discovered that Gandalf used nothing but a simple letter substitution scheme, and further, that it is its own inverse|the same operation scrambles the message as unscrambles it.

This operation is performed by replacing vowels in the sequence 'a' 'i' 'y' 'e' 'o' 'u' with the vowel three advanced, cyclicly, while preserving case (i.e., lower or upper).

Similarly, consonants are replaced from the sequence 'b' 'k' 'x' 'z' 'n' 'h' 'd' 'c' 'w' 'g' 'p' 'v' 'j' 'q' 't' 's' 'r' 'l' 'm' 'f' by advancing ten letters.

So for instance the phrase 'One ring to rule them all.' translates to 'Ita dotf ni dyca nsaw ecc.'

The fascinating thing about this transformation is that the resulting language yields pronounceable words. For this problem, you will write code to translate Gandalf's manuscripts into plain text.

Your job is to write a function that decodes Gandalf's writings.

Input

The function will be passed a string for the function to decode. Each string will contain up to 100 characters, representing some text written by Gandalf. All characters will be plain ASCII, in the range space (32) to tilde (126).

Output

For each string passed to the decode function return its translation.

'''

def tongues(code):
    #make dictionaries with values equal to index of letter transform
    consonants = 'bkxznhdcwgpvjqtsrlmf'
    vowels = 'aiyeou'
    vwl_dct = dict((_, (vowels.index(_) + 3)%len(vowels)) for _ in vowels)
    cons_dct = dict((_, (consonants.index(_) + 10)%len(consonants)) for _ in consonants)

    #decode galdolf's speach letter by letter adding to decode string which is returned
    decode = ''
    for l in code:
        if l.lower() in vowels:
          idx = vwl_dct[l.lower()]
          transform = vowels[idx]
        elif l.lower() in consonants:
          idx = cons_dct[l.lower()]
          transform = consonants[idx]
        else:
          transform = l

        #logic to maintain case of the letter.
        if l.isupper():
            decode += transform.upper()
        else:
            decode += transform
    return decode

#from other's solutions importing the string.maketrans() module
# def tongues(code):
#     import string
#     gandalf = string.maketrans(
#         'aiyeoubkxznhdcwgpvjqtsrlmfAIYEOUBKXZNHDCWGPVJQTSRLMF',
#         'eouaiypvjqtsrlmfbkxznhdcwgEOUAIYPVJQTSRLMFBKXZNHDCWG')
#     return string.translate(code, gandalf)

if __name__ == '__main__':
    message = 'Ita dotf ni dyca nsaw ecc.'
    print tongues(message)
