import utils
import scipy
import tensorflow as tf
from gcn.utils import *
from gcn.models import GCN, MLP

# adj, features, y_train, y_val, y_test, train_mask, test_mask = utils.load_data("cora")
#adj, features, y_train, y_val, y_test, train_mask, val_mask, test_mask = utils.load_data("mydata")

item_list = []
for item in utils.load_data("mydata"):
	item_list.append(item)

logging = False
if logging == True:
	for item in item_list:
		print(type(item))
	print("=" * 40)

	for item in item_list:
		print(item)
		print("=" * 40)
