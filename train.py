import argparse

from common.services import deep_learning_service

parser = argparse.ArgumentParser(description="Face Expression's recognition")

parser.add_argument('-f', '--file-checkpoint', type=str, default="checkpoint.saved.hdf5", dest='checkpoint',
                    help='Path of the file to save the checkpoint')
parser.add_argument('-b', '--batch-size', type=int, default=128, dest='batch_size',
                    help='The number of images to be processed per time')
parser.add_argument('-e', '--epochs', type=int, default=100, dest='epochs',
                    help='The number of times we will repeat our train dataset')
parser.add_argument('-ds', '--dataset', type=str, default='fer2013/fer2013.csv', dest='dataset',
                    help='Path to the Fer2013\'s dataset file (*.csv)')

args = parser.parse_args()
deep_learning_service.train_model(args.dataset, args.batch_size, args.epochs, args.checkpoint)
