import preprocessing as prep
import en_core_web_lg
import spacy
import operator
import random
import wikipedia




def preprocess(sentence): # preprocess the sentence using preprocessing model
    clean=prep.cleanPunctuationAndLower(sentence)
    stemm=prep.StemmingAndLemmatization(clean)
    spell=prep.cleanStopWordsAndSpelling(stemm)
    return spell

def wordEmbedding(question): #change all questions in the corpora to vectors and store in a list
    embeddingList=[]
    nlp = en_core_web_lg.load()

    for x in range(len(question)):
        doc=nlp(preprocess(question[x]))
        pre=[doc]
        pre.append(prep.findsenti(question[x]))#also include the sentiment 
        embeddingList.append(pre)
    return embeddingList



def generate(intputSen,doc2,answer):
    index=0
    nlp = en_core_web_lg.load()
    doc1=nlp(preprocess(intputSen))
    inputsenti=prep.findsenti(intputSen)
    similarity=0
    bestlist=[]

    for x in range(len(doc2)):
        if doc2[x][0].vector_norm and doc1.vector_norm:
            similarity=doc1.similarity(doc2[x][0]) #compare the input sentence and questions stored in the list

        if similarity>0.78:         
        # this is the threshold, so if this value is too high, then your input must
        #have a higher degree of similarity to the questions in the corpora
            index=x
            bestlist.append([similarity,index,doc2[x][1]])
    
    if len(bestlist)==0:
        # at least 5 different  reasonable responses when the user enters something outside the two topics
        try:#if the answer is not found in the database, search on wikipedia
            answer=wikipedia.summary(preprocess(intputSen))
            return "Sorry your question is not included in my database, here is the answer from wikipedia:"+'\n\n'+answer
        except Exception as e:
            listReply = ['Sorry your question is not included in my database','Sorry, I do not know how to reply that',
            'Whoops! my brain is dead, may be next question','Pass that bro, I cannot remember', 
            'This question is too difficult, next question please','Your question is hard for me, sorry about that']
            replyOutsideTopic = random.choice(listReply)
            return replyOutsideTopic# if error return answer is not found        
       
    sortedanswer=sorted(bestlist,key=operator.itemgetter(0))

    if len(sortedanswer)==1: 
        print(answer[sortedanswer[0][1]])
        return answer[sortedanswer[0][1]]
    else:
        if sortedanswer[-1][0]!=sortedanswer[-2][0]:
            print(answer[sortedanswer[-1][1]])
            return answer[sortedanswer[-1][1]]
        else:
            if abs(sortedanswer[-1][2]-inputsenti)>abs(sortedanswer[-2][2]-inputsenti):#if top 2 answer have same similarity, then check the sentiment.
                print(answer[sortedanswer[-2][1]])
                return answer[sortedanswer[-2][1]]
            else:
                print(answer[sortedanswer[-1][1]])
                return answer[sortedanswer[-1][1]]

