import luminance
import stdarray
import stdio
import sys
from blob import Blob
from picture import Picture


# A data type to identify blobs in a picture.
class BlobFinder:
    # Constructs a blob finder to find blobs in the picture pic, using a luminance threshold tau.
    def __init__(self, pic, tau):
        # Initialize an empty list for the blobs in pic.
        self._blobs = []

        # Create a 2D list of booleans called marked, having the same dimensions as pic.
        marked = stdarray.create2D(pic.width(), pic.height(), False)

        # Enumerate the pixels of pic, and for each pixel (i, j):
        # 1. Create a Blob object called blob.
        # 2. Call self._findBlob() with the right arguments.
        # 3. Add blob to self.blobs if it has a non-zero mass.
        for row in range(pic.width()):
            for col in range(pic.height()):
                blob = Blob()
                self._findBlob(pic, tau, row, col, marked, blob)
                if blob.mass() > 0:
                    self._blobs += [blob]

    # Returns a list of all beads (blobs with mass >= pixels).
    def getBeads(self, pixels):
        a = []
        for i in self._blobs:
            if i.mass() >= pixels:
                a.append(i)
        return a

    # Identifies a blob using depth-first search. The parameters are the picture (pic), luminance
    # threshold (tau), pixel column (i), pixel row (j), 2D boolean matrix (marked), and the blob
    # being identified (blob).
    def _findBlob(self, pic, tau, row, col, marked, blob):
        # Base case: return if pixel (i, j) is out of bounds, or if it is marked, or if its
        # luminance is less than tau.
        if row < 0 or row >= pic.width():
            return
        elif col < 0 or col >= pic.height():
            return
        elif marked[row][col]:
            return
        elif luminance.luminance(pic.get(row, col)) < tau:
            return

        # Mark the pixel.
        marked[row][col] = True

        # Add the pixel to blob.
        blob.add(row, col)

        # Recursively call self._findBlob() on the N, E, W, S pixels.
        # South
        self._findBlob(pic, tau, row + 1, col, marked, blob)
        # North
        self._findBlob(pic, tau, row - 1, col, marked, blob)
        # East
        self._findBlob(pic, tau, row, col + 1, marked, blob)
        # West
        self._findBlob(pic, tau, row, col - 1, marked, blob)


# Unit tests the data type (DO NOT EDIT).
def _main():
    pixels = int(sys.argv[1])
    tau = float(sys.argv[2])
    pic = Picture(sys.argv[3])
    bf = BlobFinder(pic, tau)
    beads = bf.getBeads(pixels)
    stdio.writef('%d Beads:\n', len(beads))
    for blob in beads:
        stdio.writeln(str(blob))
    blobs = bf.getBeads(1)
    stdio.writef('%d Blobs:\n', len(blobs))
    for blob in blobs:
        stdio.writeln(str(blob))


if __name__ == '__main__':
    _main()
