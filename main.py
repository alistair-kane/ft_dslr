from data import Data

if __name__ == '__main__':
	csv_path = 'datasets/dataset_train.csv'
	data = Data(csv_path)
	# data.get_counts()
	# data.get_means()
	data.get_standard_deviation()