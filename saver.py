import pickle
import os

import global_names


class saver:

    def __init__(self):
        self.temp_maps = []

    def load(self):
        """
        Загружает из файла уже созданные карты
        """
        if os.path.exists(global_names.MY_PATH) and os.path.getsize(
                global_names.MY_PATH) > global_names.EMPTY:
            with open(global_names.MY_PATH, "rb") as f:
                global_names.MAPS_COLLECTION = pickle.load(f)

    def convert(self, dictionary, map):
        """
        Переводит карту под номером TEMP_ID из массива карт из формата массива чисел,
        в котором они сохраняются в массив картинок
        :return: массив картинок, отображающий карту
        """
        data = []
        for temp_y in range(map.width):
            temp_data = []
            for temp_x in range(map.length):
                temp_data.append(dictionary[
                                     global_names.MAPS_COLLECTION[
                                         global_names.TEMP_ID][temp_y][temp_x]])
            data.append(temp_data)
        return data

    def save_after_editor(self, dictionary, map):
        """
        Добавляет только что созданную карту к тем, что уже были и сохраняет их все в файл
        """
        with open("maps/maps.pickle", "wb") as f:
            for temp_y in range(map.width):
                temp_data = []
                for temp_x in range(map.length):
                    temp_data.append(dictionary[
                                         map.scheme[temp_y][temp_x]])
                self.temp_maps.append(temp_data)
            global_names.MAPS_COLLECTION.append(self.temp_maps)
            pickle.dump(global_names.MAPS_COLLECTION, f)

    def save(self):
        """
        Сохраняет карты в файл
        """
        with open("maps/maps.pickle", "wb") as f:
            pickle.dump(global_names.MAPS_COLLECTION, f)
