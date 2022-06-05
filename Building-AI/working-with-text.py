import numpy as np
import math

text = '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again'''

def main(text):
    # tasks your code should perform:

    # 1. split the text into words, and get a list of unique words that appear in it
    # a short one-liner to separate the text into sentences (with words lower-cased to make words equal 
    # despite casing) can be done with 
    docs = [line.lower().split() for line in text.split('\n')]
    vocabulary = list(set(text.lower().split()))
    # 2. go over each unique word and calculate its term frequency, and its document frequency
    TF, DF = {}, {}
    for word in vocabulary:
        TF[word] = [line.count(word)/len(line) for line in docs]
        DF[word] = sum([word in line for line in docs])/len(docs)

    # 3. after you have your term frequencies and document frequencies, go over each line in the text and 
    # calculate its TF-IDF representation, which will be a vector

    data = [[TF[word][i] * math.log(1/DF[word],10) for word in line] for i,line in enumerate(docs)]

    # 4. after you have calculated the TF-IDF representations for each line in the text, you need to
    # calculate the distances between each line to find which are the closest.

    N = len(data)
    dist = np.empty((N, N), dtype=np.float)
    for i in range(N):
        for j in range(N):
            if i == j: sum1 = np.inf
            else:
                sum1 = 0.0
                for char in range(len(data[i])):
                    sum1 += abs(data[i][char] - data[j][char])
            dist[i][j] = sum1
            dist[j][i] = sum1

    print(np.unravel_index(np.argmin(dist), dist.shape))

main(text)
