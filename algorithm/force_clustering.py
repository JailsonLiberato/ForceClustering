from sklearn.datasets import make_blobs
from model.point import Point
import math
import numpy as np


class ForceClustering:
    """Force Clustering Algorithm"""

    def __init__(self, number_points=100, number_dimensions=2, number_clusters=3, min_range=-10, max_range=10,
                 alpha=0.5, max_iterations=300, eta1=0, eta2=0, fj_magnitude=1):
        self.__points = []
        self.__number_points = number_points
        self.__number_dimensions = number_dimensions
        self.__number_clusters = number_clusters
        self.__min_range = min_range
        self.__max_range = max_range
        self.__min_point_distance = math.inf
        self.__min_point: Point = None
        self.__alpha = alpha
        self.__max_iterations = max_iterations
        self.__eta1 = eta1
        self.__eta2 = eta2
        self.__q = np.random.rand(self.__number_clusters, self.__number_dimensions)  # O que seria q?
        self.__fj_magnitude = fj_magnitude

    def execute(self):
        self.__initialize_points()
        self.__calculate_force()

    def __initialize_points(self):
        print("Initializing points...")
        positions, labels = make_blobs(n_samples=self.__number_points, centers=self.__number_clusters,
                                       center_box=(self.__min_range, self.__max_range),
                                       n_features=self.__number_dimensions, random_state=0)
        print("Positions: ")
        print(positions)
        print("Labels: ")
        print(labels)
        for position in positions:
            point = Point(position)
            self.__points.append(point)

    def __find_minimum_distance_point(self):
        """distance = ((x1 - x2)**2 + (y1 - y2)**2)**0.5 // calculate_Ro"""
        print("Searching minimum distance point...")
        for point in self.__points:
            for point2 in self.__points:
                distance = 0
                for dim in range(self.__number_dimensions):
                    distance += (point.position[dim] - point2.position[dim])**2
                distance = distance ** 0.5
                point.distance.append(distance)
                if point != point2 and self.__min_point_distance > distance:
                    self.__min_point_distance = distance
                    self.__min_point = point

    def __calculate_force(self):
        """__calculate_canonical_algorithm"""
        self.__find_minimum_distance_point()
        self.__charging_q_points()
        for tau in range(self.__max_iterations):
            moves_magnitude = np.full_like(self.__q, np.inf)
            counter = 0;
            for qj in self.__q:
                resultant_points_force = self.__calculate_incident_force_point(qj)
                resultant_cluster_force = self.__calculate_incident_force_cluster(qj)
                force = resultant_points_force + resultant_cluster_force
                force_magnitude = np.linalg.norm(force)
                move_qj = ((self.__eta1 / self.__fj_magnitude) + (self.__eta2 / (self.__fj_magnitude ** 2))) * force
                qj = qj + move_qj
                moves_magnitude[counter] = np.linalg.norm(move_qj)
                counter += 1
            self.__charging_q_points()

    def __calculate_incident_force_point(self, qj):
        """For each Q, calculating the incident force"""
        for point in self.__points:
            dij = np.linalg.norm(point.position - qj)  # O que seria qj
            rij = min(self.__min_point.position, dij)
            denominator = dij * (rij ** 2)
            fj = fj + (-1.0 / denominator) * (qj - point.position)  # I need to change the charge!!!!
        return fj

    def __calculate_incident_force_cluster(self, qj):
        """For each Q, calculating the incident force"""
        fj = np.zeros(self.__number_dimensions)
        for ql in self.__q:
            dlj = np.linalg.norm(qj - ql)
            if dlj != 0:
                rlj = min(self.__min_point.position, dlj)
                denominator = dlj * (rlj ** 2) # Não está sendo utilizado
                fj = fj + (1.0 / rlj ** 2) * (qj - ql)  # I need to change the charge!!!!
        return fj

    def __charging_q_points(self):
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
