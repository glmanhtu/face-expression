from common.services import deep_learning_service

batch_size = 128
epochs = 100

# checkpoint
filepath = "checkpoint.saved.hdf5"

deep_learning_service.train_model("fer2013/fer2013.csv", batch_size, epochs, filepath)