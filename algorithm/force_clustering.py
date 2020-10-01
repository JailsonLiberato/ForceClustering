from sklearn.datasets import make_blobs


class ForceClustering:
    """Force Clustering Algorithm"""

    def __init__(self):
        self.__number_points = 100
        self.__number_dimensions = 2
        self.__number_clusters = 3
        self.__min_range = -10
        self.__max_range = 10

    def execute(self):
        self.__initialize_points()

    def __initialize_points(self):
        X, y = make_blobs(n_samples=self.__number_points, centers=self.__number_clusters,
                          n_features=self.__number_dimensions, random_state=0)
        print(X.shape)
        print(len(y))

    def __calculate_force(self):
        pass

    def __update_position(self):
        pass

    def __update_charge(self):
        pass

    def __check_stop(self):
        pass


