import keras.backend as ks
from common.type import deep_model
from keras.callbacks import ModelCheckpoint
from common.type.fer2013 import num_class, img_width, img_height, Fer2013

# Set default shape of image: channel, width, height
ks.set_image_data_format('channels_first')

# Set default type float32
ks.set_floatx('float32')

dl_model = deep_model.generate_model(num_class, img_width, img_height)


def train_model(dataset_path, batch_size, epochs, checkpoint_path):
    checkpoint = ModelCheckpoint(checkpoint_path, monitor='val_loss', verbose=1, save_best_only=True, mode='min')

    # Load the given dataset
    dataset = Fer2013(dataset_path)

    # Starting to train
    dl_model.fit(dataset.data_train,
                 dataset.label_train_oh,
                 batch_size=batch_size,
                 validation_data=(dataset.data_val, dataset.label_val_oh),
                 epochs=epochs,
                 callbacks=[checkpoint],
                 shuffle=True,
                 verbose=1)
    loss, accuracy = dl_model.evaluate(dataset.data_test, dataset.label_test_oh, batch_size=batch_size)
    print("Accuracy on the test data set: {:.2f}%, loss: [{:.3f}]".format(accuracy * 100, loss))


def load_model(checkpoint_path):
    dl_model.load_weights(checkpoint_path)

