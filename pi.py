# Choose N many points to put inside a square (0-1, 0-1) coordinates.
# Count how many where put out vs how many fit x^2 + y^2 <= 1 inside circle
# That ratio is pie

from random import randint
import matplotlib.pyplot as plt
import numpy as np


class Coordinates:
    """Estimate area with random sampling."""

    def get_cords(self, points: int) -> tuple[list[int], list[int]]:
        """Helper function to count_points.
        Return a random list of <points> many coordinates (x, y)
        within [0,1]x[0,1]."""

        x, y = [], []
        for i in range(points):
            x.append(randint(0, 1))
            y.append(randint(0, 1))
        return x, y

    def count_cords(self, points: int) -> tuple[int, int]:
        """Return a tuple of how many points there are,
        versus how many satisfy x^2 + y^2 <= 1."""

        count, cords = 0, self.get_cords(points)
        for i in range(len(cords[0])):
            if (cords[0][i] ** 2) + (cords[1][i] ** 2) <= 1:
                count += 1
        return count, points


class Scatterplot:
    """Create a scatterplot for the random samples."""

    def plot_circle(self, cords: tuple[list[int], list[int]]) -> None:
        """Plot a scatterplot with a circle outline."""

        x1, y1 = cords[0], cords[1]
        x = [0, 1, 1, 0, 0]
        y = [0, 0, 1, 1, 0]

        plt.plot(x, y)
        plt.scatter(x1, y1)
        plt.gca().set_aspect('equal')

        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()


c = Coordinates()
s = Scatterplot()

cords = c.get_cords(2000)
s.plot_circle(cords)
