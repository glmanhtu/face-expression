import numpy as np
import pandas as pd

label_map = ['Anger', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']
num_class = len(label_map)
img_width, img_height = 48, 48


class Fer2013:

    def __init__(self, input_file) -> None:
        super().__init__()
        file = pd.read_csv(input_file)

        n_images = file.shape[0]
        image_data = np.zeros((n_images, img_width, img_height))

        for i in range(n_images):
            image_data[i] = np.fromstring(file['pixels'][i], dtype=float, sep=' ').reshape(img_width, img_height)

        # Flattening data for normalization
        image_data = image_data.reshape(n_images, -1)

        # Normalization
        image_data = image_data / 255.0
        image_data = image_data.reshape((n_images, 1, img_width, img_height))

        # Train dataset
        train = file[file['Usage'] == "Training"]
        self.label_train = train.emotion
        self.data_train = image_data[:train.shape[0]]

        # Test dataset
        test = file[file['Usage'] == "PublicTest"]
        self.label_test = test.emotion
        index_from = test.index.values.min()
        index_to = test.index.values.max()
        self.data_test = image_data[index_from:index_to + 1]

        # Validation dataset
        val = file[file['Usage'] == "PrivateTest"]
        self.label_val = val.emotion
        self.data_val = image_data[val.index.values.min():]

        # Creating one hot labels
        self.label_train_oh = (np.arange(num_class) == self.label_train[:, None]).astype(np.float32)
        self.label_test_oh = (np.arange(num_class) == self.label_test[:, None]).astype(np.float32)
        self.label_val_oh = (np.arange(num_class) == self.label_val[:, None]).astype(np.float32)
