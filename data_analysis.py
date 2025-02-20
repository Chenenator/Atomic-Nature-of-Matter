import math
import stdio


# Entry point.
def main():
    # Initialize ETA, RHO, T and R to appropriate values.
    ETA = 9.135 * (10 ** (-4))
    RHO = 0.5 * (10 ** (-6))
    T = 297
    R = 8.31457
    # Convert pixels to meters.
    Pixel_Meters = 1.75e-7
    n = 0
    # Accepts the displacement from the outputs of bead_tracker.py.

    # Calculate var as the sum of the squares of the n displacement read from standard input.
    # Then divided var by 2 * n displacement.
    while not stdio.isEmpty():
        displacement = stdio.readAllFloats()
        var = sum(map(lambda r: math.pow(Pixel_Meters * r, 2), displacement))
        var = var/(2 * len(displacement))
        n += 1

    # Estimate Boltzmann's constant.
        Boltzmann = (6 * math.pi * var * ETA * RHO) / T
    # Estimate Avogadro's constant.
        Avogadro = R / Boltzmann

    # Write to standard output the two constants in scientific notation and separated by a space.
        stdio.writef("%e %e\n", Boltzmann, Avogadro)


if __name__ == '__main__':
    main()
