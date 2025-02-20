import math
import stdio
import sys
from blob_finder import BlobFinder
from picture import Picture


# Entry point
def main():
    # Accept command-line arguments p(int), tau(float), delta(float),
    # and a sequence of JPEG filenames.
    pixels = int(sys.argv[1])
    tau = float(sys.argv[2])
    delta = float(sys.argv[3])
    frames = sys.argv[4:]
    # Construct a BlobFinder object for the frame sys.argv[4]
    # and from it get a list of beads prevBeads that have at least x pixels
    blob_finder = BlobFinder(Picture(frames[0]), tau)
    prevBeads = blob_finder.getBeads(pixels)
    # For each frame starting at sys.argv[5]...
    for i in range(1, len(frames)):
        # Construct a BlobFinder object and from it get a list
        # of beads currBeads that have at least x pixels.
        blob_finder = BlobFinder(Picture(frames[i]), tau)
        currBeads = blob_finder.getBeads(pixels)
        # For each bead currBead in currBeads, find a bead prevBead
        # from prevBeads that is no further than delta and is closest to currBead,
        # and if such a bead is found, write its distance using format string ’%.4f\n’ to
        # currBead.
        for currbead in currBeads:
            closest = math.inf
            for prevBead in prevBeads:
                x = currbead.distanceTo(prevBead)
                if x <= delta and x < closest:
                    closest = x
            if closest != math.inf:
                stdio.writef("%.4f\n", closest)
        stdio.writeln()
        prevBeads = currBeads


if __name__ == '__main__':
    main()
