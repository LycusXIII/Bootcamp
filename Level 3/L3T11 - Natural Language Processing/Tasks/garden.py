'''This program shows the basics of spacy and how its used for NLP'''
import spacy

nlp = spacy.load('en_core_web_sm')
gardenpathSentences = [
    "The flight to New York at 8 PM canceled.",
    "The horse raced past the barn fell.",
    "Mary gave the child a Band-Aid.",
    "That Jill is never here hurts.",
    "The cotton clothing is made of grows in Mississippi."
]

for sentence in gardenpathSentences:
    doc = nlp(sentence)
    tokens = [token.text for token in doc]
    print("Tokens:", tokens)

    for entity in doc.ents:
        print("NER:", entity.text, entity.label_)
    print("-")

# https://shorturl.at/ZP11v
# https://shorturl.at/aiVW3
print("Explain GPR:", spacy.explain("GPE"))
print("Explain ORG:", spacy.explain("ORG"))

# Entity: "GPE" - Geopolitical Entity
# No, linking GPE to geopolitical entity doesn't really make sense.

# Entity: "ORG" - ORG = Organization
# Yes, ORG is a shorter way of saying organization like i belong to
# that ORG.
