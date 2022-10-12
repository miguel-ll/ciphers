import numpy as np
import matplotlib.pyplot as plt

def count_letters(txt):
    res = [0 for _ in range(26)]
    ltt = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in range(26):
        a = 0
        for j in txt:
            if j == ltt[i]:
                a+=1
        res[i]=a
    return res

def letters_dist(txt):
    x = [i for i in range(26)]
    y = count_letters(txt)
    labels = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    plt.bar(x,y,align='center',color='gray',edgecolor='black')
    plt.xticks(x, labels, rotation ='horizontal')
    #plt.margins(0.2)
    # Tweak spacing to prevent clipping of tick-labels
    plt.subplots_adjust(bottom = 0.15)
    plt.show()

def letters_dist2(sentence):
    numbers = np.array([ord(c) for c in sentence])
    u = np.unique(numbers)
    ind = [np.where(u==n)[0][0] for n in numbers]
    bins = range(0,len(u)+1)
    hist, bins = np.histogram(ind,bins)
    plt.bar(bins[:-1], hist, align='center', color='gray', edgecolor='black')
    plt.xticks(np.unique(ind), [str(chr(n)) for n in set(numbers)])
    plt.margins(0.1)
    plt.show()

#letters_dist("hello world")
