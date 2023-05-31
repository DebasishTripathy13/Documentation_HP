import spacy
from textblob import TextBlob

nlp = spacy.load("en_core_web_sm")

# Example social media post
post = "Just bought an HP LaserJet Pro MFP M281fdw and it's been a nightmare. The wifi keeps disconnecting and I can't get any work done. #hpsucks #printerproblems"

# Named entity recognition
doc = nlp(post)
for ent in doc.ents:
    if ent.label_ == "PRODUCT":
        printer = ent.text
        break
else:
    printer = None

# Keyword extraction
keywords = ["wifi", "disconnecting", "work"]

# Sentiment analysis
blob = TextBlob(post)
polarity = blob.sentiment.polarity

# Store extracted information in a knowledge graph
graph.add_node("Post", text=post, printer=printer, keywords=keywords, polarity=polarity)
