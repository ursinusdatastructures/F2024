import numpy as np
import matplotlib.pyplot as plt
import pandas
from matplotlib.offsetbox import OffsetImage, AnnotationBbox, DrawingArea

def hashFn(people, idx):
    return people['Year'][idx]

if __name__ == '__main__':
    NPerRow = 10
    people = pandas.read_csv("../data/HarryPotter/HarryPotter.csv")
    N = len(people)
    h = 0.3

    idxs = np.arange(N)
    bins = np.array([hashFn(people, idx) for idx in idxs])
    bmin = np.min(bins)
    bmax = np.max(bins)
    NRows = int(np.ceil(float(bmax-bmin+1)/NPerRow))
    res = 5
    plt.figure(figsize=(res, res*NRows))
    ax = plt.gca()
    for b in range(bmin, bmax+1):
        row, col = np.unravel_index(b-bmin, (NRows, NPerRow))
        bidxs = idxs[bins == b]
        if len(bidxs) > 0:
            dh = h/float(len(bidxs))
            for i, idx in enumerate(bidxs):
                img = plt.imread("../data/HarryPotter/%i.png"%(idx+1))
                im = OffsetImage(img)
                x = float(col)/NPerRow
                y = row
                #print("b = %i, (x, y) = (%.3g, %.3g)"%(b, x, y))
                ab = AnnotationBbox(im, (0, 0), xycoords='data', frameon=False)
                da = DrawingArea(x, y, 1.0/NRows, 1.0/NRows)
                da.add_artist(ab)
                ax.add_artist(da)
    plt.xlim([0, 1])
    plt.ylim([0, NRows])
    plt.show()