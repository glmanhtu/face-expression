import argparse
import csv
import re

parser = argparse.ArgumentParser(description="Analysing the training log file")

parser.add_argument('-f', '--file', type=str, required=True, dest='log_file',
                    help='Path of the log file')
parser.add_argument('-o', '--out-file', type=str, default='output.csv', dest='out_file',
                    help='Path of the analysed file')

args = parser.parse_args()


def get_n_epoch(log_line):
    epochs = re.search(r'Epoch\s(\d+)/(\d+)', log_line)
    if epochs:
        return epochs.group(1), epochs.group(2)
    return None, None


def get_epoch_result(log_line):
    val = re.search(r'loss:\s([\d.]+)\s-\sacc:\s([\d.\d]+)\s-\sval_loss:\s([\d.]+)\s-\sval_acc:\s([\d.\d]+)', log_line)
    if val:
        return val.group(1), val.group(2), val.group(3), val.group(4)
    return None, None, None, None


val_result = []
with open(args.log_file) as f:
    epoch = 0
    for line in f:
        ep, total = get_n_epoch(line)
        if ep is not None:
            epoch = ep
        loss, acc, val_loss, val_acc = get_epoch_result(line)
        if val_acc is not None:
            val_result.append({'epoch': epoch, 'loss': loss, 'acc': acc, 'val_loss': val_loss, 'val_acc': val_acc})

with open(args.out_file, 'w') as f:  # Just use 'w' mode in 3.x
    w = csv.DictWriter(f, val_result[0].keys())
    w.writeheader()
    w.writerows(val_result)

