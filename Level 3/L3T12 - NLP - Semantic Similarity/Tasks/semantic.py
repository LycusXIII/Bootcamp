import spacy

# nlp = spacy.load('en_core_web_md')
nlp = spacy.load('en_core_web_sm')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
# The similarities between cat monkey banana the model picks up that
# monkey and banana has similarities because monkey's eats bananas
# the model shows a signification lower score between cat and banana
# then monkey and banana.
print('-')

example1 = nlp("keyboard")
example2 = nlp("speakers")
example3 = nlp("phone")

print(example1.similarity(example2))
print(example3.similarity(example2))
print(example3.similarity(example1))
print(example2.similarity(example3))
print('-')

tokens = nlp('cat apple monkey banana ')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

print('-')

sentence_to_compare = "Why is my cat on the car"

sentences = [
    "where did my dog go",
    "Hello, there is my car",
    "I\'ve lost my car in my car",
    "I\'d like my boat back",
    "I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(f"{sentence} - {similarity}")


"""
Output of model - en_core_web_md
0.5929930274321619
0.40415016164997786
0.22358825939615987
-
0.4062122073652054
0.31543791607331545
0.35641602411089346
0.31543791607331545
-
cat cat 1.0
cat apple 0.2036806046962738
cat monkey 0.5929930210113525
cat banana 0.2235882580280304
apple cat 0.2036806046962738
apple apple 1.0
apple monkey 0.2342509925365448
apple banana 0.6646699905395508
monkey cat 0.5929930210113525
monkey apple 0.2342509925365448
monkey monkey 1.0
monkey banana 0.4041501581668854
banana cat 0.2235882580280304
banana apple 0.6646699905395508
banana monkey 0.4041501581668854
banana banana 1.0
-
where did my dog go - 0.630065230699739
Hello, there is my car - 0.8033180111627156
I've lost my car in my car - 0.6787541571030323
I'd like my boat back - 0.5624940517078084
I will name my dog Diana - 0.6491444739190607
"""
