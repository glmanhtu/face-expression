from keras import Input, Model
from keras.layers import Conv2D, MaxPooling2D, concatenate, Dropout
from keras.layers import Dense, Activation, Flatten, BatchNormalization


def featex_block(input_layers):
    """
    @see https://arxiv.org/abs/1509.05371
    :param input_layers: previous layers
    :return:
    """
    conv_2a = Activation('relu')((Conv2D(96, 1)(input_layers)))
    max_pool_2a = MaxPooling2D(pool_size=(3, 3), strides=1)(input_layers)
    conv_2b = Activation('relu')((Conv2D(208, 3))(conv_2a))
    conv_2c = Activation('relu')((Conv2D(64, 1))(max_pool_2a))
    return concatenate([conv_2b, conv_2c], axis=1)


def generate_model(n_classes, img_width, img_height):
    """
    Generate a deep learning model for face emotion's recognition
    :param n_classes: number of class to be classified
    :param img_width: width of the input image
    :param img_height: height of the input image
    :return:
    """
    inputs = Input(shape=(1, img_width, img_height))
    model = Conv2D(64, (3, 3), padding='same', input_shape=(1, img_width, img_height))(inputs)

    model = BatchNormalization()(model)
    model = Activation('relu')(model)
    model = MaxPooling2D(pool_size=(2, 2))(model)
    model = Dropout(0.25)(model)
    model = featex_block(model)
    model = featex_block(model)
    model = Dropout(0.25)(model)

    model = Flatten()(model)

    # Output Fully connected layer
    model = Dense(n_classes)(model)
    model = Activation('sigmoid')(model)

    model = Model(inputs=inputs, outputs=model)

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model
