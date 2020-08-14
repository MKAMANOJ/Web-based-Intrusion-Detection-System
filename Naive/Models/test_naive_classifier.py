from joblib import load
from os import sys

classifier = load('naive_classifier.pkl')
word_features = load('word_features.pkl')

def extract_features(document):
    """
        checks if the passed list of words
        is contained in the list 'word_features'
    """
    document_words = set(document)
    features = {}
    global word_features
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features


if __name__ == "__main__":
    print(classifier.show_most_informative_features())
    print(classifier)

    test_word = str(sys.argv[1:])
    print(classifier.classify(extract_features(test_word.lower().split())))
