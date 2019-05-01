from AssignmentNumPredict import *


def calculateData():
    
    fmeasure = 'F-Measure'
    wlblog = 'Web Science and Digital Libraries Research Group'
    bnames = {}
    mesf = []
    cesf = []
    with open("blogdata.txt", 'r', encoding='utf-8') as f:
        doctext = f.readlines()
        for i, line in enumerate(doctext):
            if i == 0:
                # skip header
                continue
            tuples = line.strip().split('\t')
            if tuples[0] == fmeasure:
                for i in range(1, len(tuples)):
                    mesf.append(float(tuples[i]))
            elif tuples[0] == wlblog:
                for i in range(1, len(tuples)):
                    cesf.append(float(tuples[i]))
            else:
                bnames[tuples[0]] = []
                for i in range(1, len(tuples)):
                    bnames[tuples[0]].append(float(tuples[i]))

    return bnames, mesf, cesf


def knnest(calval, mesvec, gpvec):
    nn = knnestimate(bnames.values(), mesvec)
    print("====================================" * 2)
    print("F-Measure")
    print("====================================" * 2)
    kvals = [1, 2, 5, 10, 20]
    for k in kvals:
        print('k =', k)
        for j in range(k):
            print('%s\t%.6f' % (list(bnames.keys())[nn[j][1]], nn[j][0]))

        print("------------------------------------" * 2)
    print()

    print("====================================" * 2)
    print("Web Science and Digital Libraries Research Group")
    print("====================================" * 2)
    nn = knnestimate(bnames.values(), gpvec)
    for k in kvals:
        print('k =', k)
        for j in range(k):
            print('%s\t%.6f' % (list(bnames.keys())[nn[j][1]], nn[j][0]))

        print("------------------------------------" * 2)





if __name__ == "__main__":
    bnames, dvec, worvec = calculateData()
    knnest(bnames.values(), dvec, worvec)