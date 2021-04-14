Download following libraries before running the code

pip install nltk
pip install -U spacy
python -m spacy download en_core_web_lg
pip install pyspellchecker
pip install -U textblob
pip install wikipedia
pip install google-trans-new


How to run the code: run server first at the meantime run client

Data flow: Preprocessing.py => generate.py => main.py

some features:
1. the system includes two special topics on basketball and soccer and some casual conversations.

2. the system can clean all punctuations in the sentence and convert sentence to lower case.

3. the system can remove suffixes (e.g., playing and play) and 
convert all the words back to root form (e.g. apples and apple).

4. the system can handle spelling mistakes (e.g., correct “chemitry" to “chemistry”)

5. the system can clean all the words with not much meaning in the sentence (e.g., 'a', 'is').

6. the system includes a feature that enables the chatbot to detect the user’s sentiment.

7. the system provides at least five different reasonable responses 
when the user enters something beyond the two topics.

8. the system provides a simple GUI so that the user is typing into a nicer interface and can view a recent history of the conversation.

9. the system can make a conversation with the user or agent (built by another group in this class) via sockets.


examples:
Input:what is chemistry??  
the science of mixing chemicals.

Input:tell me about chemistry  
the science of mixing chemicals.

Input:what is chemitry
the science of mixing chemicals.

Input:WHAT IS CHEMISTRY
the science of mixing chemicals.

Input:什么是化学
the science of mixing chemicals.

Input: what is physics
Sorry your question is not included in my database, here is the answer from wikipedia:
Physics (from Ancient Greek: φυσική (ἐπιστήμη), romanized: physikḗ (epistḗmē), lit. 'knowledge of nature', from φύσις phýsis 'nature') is the natural science that studies matter, its motion and behavior through space and time, and the related entities of energy and force. 
...