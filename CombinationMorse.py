def all_morse(name_file,word):
    """ This funtion obtain a word a return all words than share the same morse code. 
    Limit the result to the words in name_file
    """
    
    #Firt check if all character all letter:
    if not word.isalpha():
        raise Exception('All character must be letters!')

    #Convert all letter in lowercase
    word = word.lower()
    #Morse code by position, letter "a" in index 0, "b" in index 1 ...
    MORSE = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--",
    "-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    
    #Convert word to Morse, by index.
    # word_morse = "".join( [MORSE[ord(ch)-ord("a")] for ch in word ]) #Implicit solution, more difficult to understand.
    word_morse = ""
    for ch in word:
        word_morse += MORSE[ord(ch)-ord("a")]
    

    def dfs(word_morse,possible_word):
        # Recursive function, add values to lists
        if word_morse == "":
            if possible_word in mostCommon:
                commom.append(possible_word)
            else:
                out.append(possible_word)
            return
        for i,ch in enumerate(MORSE):
            if word_morse.startswith(ch):
                dfs(word_morse[len(ch):],possible_word+(chr(97+i)))


    def mostCommonWords(namefile):
        # Create a set with the words in namefile
        mostCommon= set()
        with open (namefile) as f:
            for line in f.readlines():
                mostCommon.add(line.strip())
        return mostCommon


    def wordToMorse(words):
        # Convert words to Morse and return returns a dictionary with them.
        dMorse = {}
        for word in words:
            morsecode = []
            for ch in word:
                morsecode.append(MORSE[ord(ch)-ord("a")])
            dMorse[word] = "'".join(morsecode)
        return dMorse

    
    mostCommon = mostCommonWords(name_file)

    commom = []
    out = []
    dfs(word_morse,"")

    dMorse = wordToMorse([word]+commom)

    print("The morse code [{}] '{}'".format(word,dMorse[word]))
    if commom:
        print("Can be one of the following words in English:")
        for word in commom:
            print("{}: '{}'".format(word, dMorse[word]))

        print("And {} other combinations...".format(len(out)))
    else:
        print("There are {} combinations, none within the 10000 most used words in English.".format(len(out)))
    return


if __name__ == "__main__":
    # File with the list of words, one in each line.
    name_file = "10000-english.txt"
    word = input()
    all_morse(name_file,word)
