import csv
import re
import sys

log_file = sys.argv[1]


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
with open(log_file) as f:
    epoch = 0
    for line in f:
        ep, total = get_n_epoch(line)
        if ep is not None:
            epoch = ep
        loss, acc, val_loss, val_acc = get_epoch_result(line)
        if val_acc is not None:
            val_result.append({'epoch': epoch, 'loss': loss, 'acc': acc, 'val_loss': val_loss, 'val_acc': val_acc})

with open('output.csv', 'w') as f:  # Just use 'w' mode in 3.x
    w = csv.DictWriter(f, val_result[0].keys())
    w.writeheader()
    w.writerows(val_result)

