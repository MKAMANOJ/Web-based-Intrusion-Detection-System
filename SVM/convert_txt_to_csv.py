from os import sys	
import csv

def convert(filepath):
    csvpath = filepath.split('.')[0]+'.csv'

    list_lines = []
    keys_to_obtain = ['Host', 'Payload', 'Content-Type', 'Content-Length', 'Method']
    with open(filepath, 'r') as outfile:
        d = dict()
        for line in outfile:
            if line in ['\n', '\r\n','\n\n']:
                if d:
                    for k in keys_to_obtain:
                        if not d.get(k):
                            d.update({
                                k: 0
                            })
                    list_lines.append(d)
                d = dict()
                continue
            listt = [x.strip() for x in line.split(':')]
            value = listt[1]
            value.replace(' ', '')
            value.replace('\r', '')
            value.replace('\n', '')
            d[listt[0]] = value

    keys = list_lines[0].keys()

    with open(csvpath, 'w') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(list_lines)

if __name__ == "__main__":
    convert(sys.argv[1])