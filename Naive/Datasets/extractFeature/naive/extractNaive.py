import re
from os import sys

class NaiveDataset:

    def __init__(self,readFileName,writeFileName):
        self.readFile = open(readFileName)
        self.writeFile = open(writeFileName,'w')

    def closeFile(self):
        self.readFile.close()
        self.writeFile.close()

    """
        return if it is a standard packet
    """
    def checkForMethod(self,load):
        regex=re.compile(r'^GET|^POST|^HEAD|^PUT|^TRACE|^CONNECT',re.M)
        return 1 if regex.search(load) else 0

    def checkForGet(self,load):
        regex=re.compile(r'GET',re.M)
        return 1 if regex.search(load) else 0

    #extract payload from request
    def filter(self,load):
        p=re.compile('\+|\&|\=')

        if (self.checkForMethod(load)==0):
            print(str(p.sub(" ",load)),file=self.writeFile)

        if (self.checkForGet(load)):
            try:
                start=load.index('?')
                end=load.index(' HTTP/')
                print(str(p.sub(' ',load[start+1:end])),file=self.writeFile)
            except ValueError:
                return ""

    def extractPayload(self):
        fstr = self.readFile.read()
        packets = fstr.split('\n\n')
        print(len(packets))
        for packet in packets:
            self.filter(packet)
        self.closeFile()

naiveDataset = NaiveDataset(sys.argv[1],sys.argv[2])
naiveDataset.extractPayload()









