# The Atbash cipher is an encryption method in which each letter of
# a word is replaced with its "mirror" letter in the alphabet: A <=> Z; B <=> Y; C <=> X; etc.
# Create a function that takes a string and applies the Atbash cipher to it.

# My dictionary that stores the alphabet
MyDictionary = {'A': 'Z', 'B': 'Y', 'C': 'X', 'D': 'W', 'E': 'V',
                'F': 'U', 'G': 'T', 'H': 'S', 'I': 'R', 'J': 'Q',
                'K': 'P', 'L': 'O', 'M': 'N', 'N': 'M', 'O': 'L',
                'P': 'K', 'Q': 'J', 'R': 'I', 'S': 'H', 'T': 'G',
                'U': 'F', 'V': 'E', 'W': 'D', 'X': 'C', 'Y': 'B', 'Z': 'A',
                '0': '0', '1': '1', '2': '2', '3': '3', '4': '4',
                '5': '5', '6': '6', '7': '7', '8': '8', '9': '9',
                '!': '!', '@': '@', '#': '#', '$': '$', '%': '%',
                '^': '^', '&': '&', '*': '*', '(': '(', ')': ')',
                '-': '-', '=': '=', '_': '_', '+': '+', '{': '{', '}': '}',
                "\\": "\\", '|': '|', ',': ',', '<': '<', ' . ': ' . ',
                '>': '>', '?': '?', '/': '/', '"': '"', '`': '`', ";": ";", ":": ":",
                '~': '~', "'": "'", "[": "[", "]": "]", ".": "."}


# the encryption  function
def encryptionFunction(input):
    encrypt = ''
    for alphabet in input:
        if (alphabet != ' '):
            encrypt += MyDictionary[alphabet]
        else:
            encrypt += ' '

    return encrypt


# a function that print out results
def main():
    # user input to cypher
    userData = raw_input("Enter your string/word(s) to be encrypted: ")
    print(encryptionFunction(userData.upper()))


# main
if __name__ == '__main__':
    main()
