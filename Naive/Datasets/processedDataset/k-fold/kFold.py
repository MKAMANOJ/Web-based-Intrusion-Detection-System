from os import sys

class Kfold:

    def __init__(self, filename):
        self.file = open(filename)
        self.trainFile = open("train/" + filename.split('/')[-1], 'w')
        self.testFile = open("test/" + filename.split('/')[-1], 'w')

    def close_files(self):
        self.file.close()
        self.trainFile.close()
        self.testFile.close()

    def run_kfold(self):
        k = int(input("Enter value of k: "))
        n = int(input("Enter the nth part for test set(quadrant): "))

        data = self.file.read()
        new_lines = data.count('\n')
        parts = int(new_lines / k)
        part_count = 1
        line_count = 0

        sentences = data.split('\n')
        lines = []

        for sentence in sentences:
            line_count = line_count + 1
            print(parts, line_count,line_count % parts,part_count)
            lines.append(sentence)

            if (line_count % parts) == 0:
                print(type(part_count),type(n))
                print("\n".join(line for line in lines),
                      file=self.testFile if (part_count == n) else self.trainFile)
                lines = []
                part_count = part_count + 1

        self.close_files()

kfold = Kfold(sys.argv[1])
kfold.run_kfold()
