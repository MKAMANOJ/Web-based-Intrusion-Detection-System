from nltk.probability import FreqDist
from nltk import classify
from nltk.classify.naivebayes import NaiveBayesClassifier
import joblib

class NaiveModel:

    training = []
    word_collection = []

    def closeFile(self):
        self.file.close()

    def read_in_chunks(self,chunk_size=1024):
        while True:
            data = self.file.read(chunk_size)
            if not data:
                break
            yield data

    def assign_class(self,filename,category):
        try:
            self.file = open(filename)
        except Exception as e:
            print(e)
        self._class = category

        for piece in self.read_in_chunks():
            sentences = piece.split('\n')
            # self.training.append(([word for word in sentence.lower().split() for sentence in sentences],self._class))
            for sentence in sentences:
                self.training.append(([word for word in sentence.lower().split()],self._class))

        #print(self.training)

    def get_word_features(self):
        for (words,sentiment) in self.training:
            self.word_collection.extend(words)

        self.wordList = FreqDist(self.word_collection)
        joblib.dump(self.wordList, 'word_features.pkl', 3)

        print(self.wordList.keys())

    '''
        checks if the passed list of words
        is contained in the list 'word_features'
    '''
    def extract_features(self, document):
        document_words = set(document)
        features = {}
        for word in self.wordList:
            features['contains(%s)' % word] = (word in document_words)
        return features

    def train(self):
        training_set = classify.apply_features(self.extract_features,self.training)
        classifier = NaiveBayesClassifier.train(training_set)
        joblib.dump(classifier, 'naive_classifier.pkl', 3)


naiveModel = NaiveModel()
naiveModel.assign_class('../Datasets/processedDataset/k-fold/train/normalCombined.txt','normal')
naiveModel.assign_class('../Datasets/processedDataset/k-fold/train/anomalousTrafficTest.txt','anomalous')
naiveModel.get_word_features()
naiveModel.train()
