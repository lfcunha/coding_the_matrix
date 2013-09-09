from random import randint


## Task 1
def movie_review(name):
    """
    Input: the name of a movie
    Output: a string (one of the review options), selected at random using randint
    """
    review_options = ["See it!", "A gem!", "Ideological claptrap!"]
    return review_options[randint(0,len(review_options)-1)]

## Tasks 2 and 3 are in dictutil.py

## Task 4    
def makeInverseIndex(strlist):
    """
    Input: a list of documents as strings
    Output: a dictionary that maps each word in any document to the set consisting of the
            document ids (ie, the index in the strlist) for all documents containing the word.

    Note that to test your function, you are welcome to use the files stories_small.txt
      or stories_big.txt included in the download.
    """
    f=open(strlist);

    lines=f.readlines()
    f.close()
    wordlist=[]
    for line in lines:
        wordlist.append(set(line.split()))

    #return [ c for c in ([b for b in a] for (a,b) in ((y,z) for (z, y) in (x for x in list(enumerate(wordlist)))))]
    dic={}
    a= [ [a for a in a for a in (a,b)] for (a,b) in ((y,z) for (z, y) in (x for x in list(enumerate(wordlist))))]
    i=0;
    for i in range(len(a)):
        for j in range(len(a[i])):
            if j%2==0:
                if a[i][j] not in dic:
                    dic[a[i][j]]=[str(i)]
                else:


                    dic[a[i][j]].append(str(i))

    a= [ set(values) for values in dic.values()]
    b=[keys for keys in dic.keys()]
    return [{b:c} for (b,c) in (a for a in zip(b, a))]





## Task 5
def orSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of document ids that contain _any_ of the specified words
    """
    return ...

## Task 6
def andSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of all document ids that contain _all_ of the specified words
    """
    return ... 
