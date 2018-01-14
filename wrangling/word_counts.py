from collections import Counter
from zipfile import ZipFile
import re
import glob

kWORDS = re.compile("[a-z]{4,}")

def text_from_zipfile(zip_file):
    """
    Given a zip file, yield an iterator over the text in each file in the
    zip file.
    """
    #extract the zip file
    zip_ref = ZipFile(zip_file, 'r')
    zip_ref.extractall("../data")
    #zip_ref.close()
    
    
    #concatenate all file's text into 1 new file
    fileContents = []
    if(zip_file == "../data/state_union.zip"):
        for files in glob.glob("../data/state_union/*.txt"):
            openFile = open(files, "r", encoding="Latin-1")
            fileText = openFile.read()
            fileContents.append(fileText)
    else:
        for files in glob.glob("../data/*.txt"):
            openFile = open(files, "r", encoding="Latin-1")
            fileText = openFile.read()
            fileContents.append(fileText)
    
   # print(fileContents[0])
    #zip_ref.close()
    return fileContents

def words(text):
    """
    Return all words in a string, where a word is four or more contiguous
    characters in the range a-z or A-Z.  The resulting words should be
    lower case.
    """
    validWords = []
    words = text.lower().split()
    for word in words:
        if(re.search("[a-z]{4,}", word)):
            if("." in word):
                tmpword = word.replace(".","")
                validWords.append(tmpword)
            elif("," in word):
                tmpword = word.replace(",","")
                validWords.append(tmpword)
            elif(";" in word):
                tmpword = word.replace(";","")
                validWords.append(tmpword)
            elif("--" in word):
                tmpword = word.split("--")
                validWords.append(tmpword[0])
                validWords.append(tmpword[1])
            elif("!" in word):
                tmpword = word.replace("!","")
                validWords.append(tmpword)
            elif(":" in word):
                tmpword = word.replace(":","")
                validWords.append(tmpword)
            else:
                validWords.append(word)
    
    return validWords

def accumulate_counts(words, total=Counter()):
    """
    Take an iterator over words, add the sum to the total, and return the
    total.

    @words An iterable object that contains the words in a document
    @total The total counter we should add the counts to
    """
    assert isinstance(total, Counter)
    
    #for word in words:
    total.update(words)
        #print(word)

        
    return total

if __name__ == "__main__":
    # You should not need to modify this part of the code
    total = Counter()
    
    for tt in text_from_zipfile("../data/state_union.zip"):
        #print(tt)
        total = accumulate_counts(words(tt), total)
    
    for ii, cc in total.most_common(100):
        print("%s\t%i" % (ii, cc))
    
