from test_naive_classifier import classifier, word_features, extract_features

class NaiveAccuracy:
    _TP = _FN = _TN = _FP = 0

    def __init__(self, normal_test_file, anomalous_test_file):
        self.nor = open(normal_test_file)
        self.anomalous = open(anomalous_test_file)

    def close_files(self):
        self.nor.close()
        self.anomalous.close()

    def read_in_chunks(self,file_object, chunk_size=1024):
        while True:
            data = file_object.read(chunk_size)
            if not data:
                break
            yield data

    def classify_files(self, file_object, category):
        correct = wrong = 0
        for piece in self.read_in_chunks(file_object):
            piece = piece.lower()
            lines = piece.split('\n')
            for line in lines:
                classed = classifier.classify(extract_features(line.split()))
                if classed == category:
                    correct = correct + 1
                else:
                    wrong = wrong + 1

        return correct,wrong

    def calculate_accuracy(self):
        _TP,_FN = self.classify_files(self.nor,"normal")
        _TN,_FP = self.classify_files(self.anomalous,"anomalous")
        self.close_files()
        results = dict()
        results['TP'] = _TP
        results['FN'] = _FN
        results['TN'] = _TN
        results['FP'] = _FP
        results['Accuracy'] = (_TP+_TN)/(_TP+_TN+_FP+_FN)
        results['Sensitivity'] = (_TP)/(_TP+_FN)
        results['Specificity'] = (_TN)/(_TN+_FP)
        results['Precision'] = (_TP)/(_TP+_FP)

        return results


naiveAccuracy = NaiveAccuracy('../Datasets/processedDataset/k-fold/test/anomalousTrafficTest.txt',
                              '../Datasets/processedDataset/k-fold/test/normalCombined.txt')
print(naiveAccuracy.calculate_accuracy())

