from sklearn.datasets import make_blobs
from model.point import Point
import math
from util.plot_util import PlotUtil


class ForceClustering:
    """Force Clustering Algorithm"""

    def __init__(self):
        self.__points = []
        self.__number_points = 100
        self.__number_dimensions = 2
        self.__number_clusters = 3
        self.__min_range = -10
        self.__max_range = 10
        self.__min_point_distance = math.inf

    def execute(self):
        self.__initialize_points()
        self.__find_minimum_distance_point()
        print("Minimum distance: ", self.__min_point_distance)

    def __initialize_points(self):
        print("Initializing points...")
        positions, labels = make_blobs(n_samples=self.__number_points, centers=self.__number_clusters,
                                       center_box=(self.__min_range, self.__max_range),
                                       n_features=self.__number_dimensions, random_state=0)
        #PlotUtil.plot_graphic(positions, labels, self.__number_dimensions)
        print("Positions: ")
        print(positions)
        print("Labels: ")
        print(labels)
        for position in positions:
            point = Point(position)
            self.__points.append(point)

    def __find_minimum_distance_point(self):
        """distance = ((x1 - x2)**2 + (y1 - y2)**2)**0.5"""
        for point in self.__points:
            for point2 in self.__points:
                distance = 0
                for dim in range(self.__number_dimensions):
                    distance += (point.position[dim] - point2.position[dim])**2
                distance = distance ** 0.5
                point.distance.append(distance)
                if point != point2 and self.__min_point_distance > distance:
                    self.__min_point_distance = distance


    def __calculate_force(self):
        pass

    def __update_position(self):
        pass

    def __update_charge(self):
        pass

    def __check_stop(self):
        pass

    @property
    def points(self):
        return self.__points
