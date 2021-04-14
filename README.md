# Friend-Chatbot-Individual-Project
![ChatbotImage](https://s3-eu-west-1.amazonaws.com/userlike-cdn-blog/do-i-need-a-chatbot/header-chat-box.png)

## About the project
This repository contains a programming project code for a chatbot that simulates a conversation between friends. 
A specific topic about soccer, basketball and some scattered topics are covered.

## Prepare stage
before we start running this code we need to download several libraries
```bash
pip install nltk
pip install -U spacy
python -m spacy download en_core_web_lg
pip install pyspellchecker
pip install -U textblob
pip install wikipedia
pip install google-trans-new
```

## How to run the code
run server first at the meantime run client

## Program features
### Original version:
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

### Updated:
1.	the system work with Google Translate API to enable the chatbot to understand input in any language.

2.	the system work with Wikipedia API extracts knowledge from definitions for your conversation use when the conversation does not include in the database.


## Sample output
```bash
Input:what is chemistry??  
the science of mixing chemicals.
```
```bash
Input:tell me about chemistry  
the science of mixing chemicals.
```
```bash
Input:what is chemitry
the science of mixing chemicals.
```
```bash
Input:WHAT IS CHEMISTRY
the science of mixing chemicals.
```
```bash
Input:什么是化学
the science of mixing chemicals.
```
```bash
Input: what is physics
Sorry your question is not included in my database, here is the answer from wikipedia:
Physics (from Ancient Greek: φυσική (ἐπιστήμη), romanized: physikḗ (epistḗmē), lit. 'knowledge of nature', from φύσις phýsis 'nature') is the natural science that studies matter, its motion and behavior through space and time, and the related entities of energy and force. 
```
```bash
...
```
## GUI and Examples
### Google Translate
<img src="https://raw.githubusercontent.com/siyuccchen/Friend-Chatbot-Individual-Project/main/Google%20Translate.png" width="400" height="500">
### Wikipedia
<img src="https://raw.githubusercontent.com/siyuccchen/Friend-Chatbot-Individual-Project/main/Wikipedia.png" width="1700" height="300">
