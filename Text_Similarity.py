import sys

def match(text1,text2):
    
    numerator = 0
    den1 = 0
    den2 = 0
    score = 0
    d1, d2 = {}, {}
    vector1 = []
    vector2 = []
    
    stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't", ""]
    special_chars = ['.' , ',', '!', ':', ';', '@', '$', '#', '&', '*', '(', ')', '{', '}', '[', ']', '?', '/']
    
    for c in special_chars:
        text1 = text1.replace(c, "")
        text2 = text2.replace(c, "")
    
    list1 = text1.lower().split(' ')
    list2 = text2.lower().split(' ')
    
    for i in list1:
        if i not in stopwords: d1[i] = d1.get(i,0) + 1
    
    for j in list2:
        if j not in stopwords: d2[j] = d2.get(j,0) + 1
            
    set_words = set(d1).union(set(d2))
        
    for i in set_words:
        vector1.append(d1.get(i,0))
        vector2.append(d2.get(i,0))
    
    for i in range(len(vector1)):
        numerator += vector1[i]*vector2[i]
        den1 += vector1[i]**2
        den2 += vector2[i]**2
    
    denominator = den1**0.5 * den2**0.5
    
    if denominator == 0: return 0
    else: return round((numerator / denominator),2)

t1 = sys.argv[1]
t2 = sys.argv[2]
score = match(t1,t2)
print('**Text 1 is** : ' + t1)
print('**Text 2 is** : ' + t2)
print('**The similarity score of the texts is** : ' + str(score))
