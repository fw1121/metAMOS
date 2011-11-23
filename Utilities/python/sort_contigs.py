#!/usr/bin/python

import sys
import os

contigs_by_class = { }
id_class = { }
id_class["0"] = "UNKNOWN"

class_file = open(sys.argv[1])
#pass class_key as argument
class_key = open(sys.argv[2])
#pass outdir as argument
out_dir = sys.argv[3]
#pass AMOS bank as argument
amos_bnk = sys.argv[4]
# parse in key file
for line in class_key:
    line = line.strip()
    fields = line.split()
    # f1 is id, f2 is class name

    if len(fields) != 2:
        print "Error in file format\n"
    else:
        id_class[fields[0]] = fields[1]



# parse contig class file
for line in class_file:
    line = line.strip()
    fields = line.split()
    # f1 is contig, f2 is class

    if len(fields) != 2:
        print "Error in file format\n"

    elif contigs_by_class.has_key(fields[1]):
        contigs_by_class[fields[1]].append(fields[0])
        
    else:
        contigs_by_class[fields[1]] = [fields[0]]
        contigs_by_class[fields[1]].append(fields[0])


for key in contigs_by_class:
    class_name = id_class[key]
    path = out_dir + class_name + "/"
    if not os.path.exists(path):
        os.mkdir(path)

    f = open(path + class_name + ".iid", 'w')
    f.write("\n".join(contigs_by_class[key]))
    f.close()
    ret = os.system("bank2fasta -b %s -i "%(amos_bnk) + path + class_name + ".iid > " + path + class_name + ".fasta")
    
    





    