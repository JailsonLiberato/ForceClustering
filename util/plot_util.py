from matplotlib import pyplot


class PlotUtil:
    """Plotting Util"""

    def plot_graphic(self, positions, labels, dimensions):
        if dimensions == 2:
            self.plot_2d(positions, labels)

    @staticmethod
    def plot_2d(positions, labels):
        for index in range(len(labels)):
            pyplot.scatter(positions[index][0], positions[index][1], facecolor='blue')
        pyplot.show()
