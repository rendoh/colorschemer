import cv2
from sklearn.cluster import KMeans


class ImageColorizer:
    def __init__(self, filepath: str):
        self.__colors = None
        self.__hexes = None
        image = cv2.cvtColor(
            cv2.imread(filepath),
            cv2.COLOR_BGR2RGB,
        )

        two_d_image = image.reshape((image.shape[0] * image.shape[1], 3))
        self.__cluster = KMeans(n_clusters=5)
        self.__cluster.fit(X=two_d_image)

    def get_colors(self):
        if not self.__colors:
            colors = self.__cluster.cluster_centers_.astype(
                int,
                copy=False
            )
            self.__colors = map(lambda rgb: tuple(rgb), colors)
        return self.__colors

    def get_hexes(self):
        if not self.__hexes:
            self.__hexes = list(
                map(lambda rgb: '#%02x%02x%02x' % rgb, self.get_hexes())
            )
        return self.__hexes
