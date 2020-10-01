from algorithm.force_clustering import ForceClustering


class Main:
    """Main Class"""

    def __init__(self):
        self.__force_clustering = ForceClustering()

    def execute(self):
        self.__force_clustering.execute()


main = Main()
main.execute()
