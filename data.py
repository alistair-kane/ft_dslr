import csv
import math
import re

class Data:
	def __init__(self, path):
		self.data = []
		self.fieldnames = None
		with open(path) as file:
			dict_reader = csv.DictReader(file)
			if dict_reader is None or dict_reader.fieldnames is None:
				raise ValueError("CSV file is empty or has no header.")
			for row in dict_reader:
				self.data.append(row)
			self.fieldnames = dict_reader.fieldnames
			self.fieldnames.remove('Index')

		self.get_counts()

	def print_dict(self, name, dict):
		print(name)
		for k,v in dict.items():
			print(f'{k}: {v}')
		print('\n')

	def get_counts(self):
		self.counts = dict.fromkeys(self.fieldnames)
		for field in self.counts:
			for row in self.data:
				if row[field]:
					if not self.counts[field]:
						self.counts[field] = 1
					else:
						self.counts[field] += 1
		self.print_dict('Counts', self.counts)

	def get_means(self):
		sum_of_features = dict.fromkeys(self.fieldnames)
		for field in sum_of_features:
			for row in self.data:
				if re.match(r'^-?\d+(?:\.\d+)$', row[field]):
					if not sum_of_features[field]:
						sum_of_features[field] = float(row[field])
					else:
						sum_of_features[field] += float(row[field])
		# print(sum_of_features)
		self.means = dict.fromkeys(self.fieldnames)
		for field in self.means:
			if sum_of_features[field]:
				# self.means[field] = "%.2f" % (sum_of_features[field] / self.counts[field])
				self.means[field] = sum_of_features[field] / self.counts[field]
			else:
				print(f"Field {field} has no numerical data, must be categorical")

		self.print_dict('Means', self.means)

	def get_standard_deviation(self):
		difference_from_means = dict.fromkeys(self.fieldnames)
		for field in difference_from_means:
			for row in self.data:
				if re.match(r'^-?\d+(?:\.\d+)$', row[field]):
					print(row[field])
					if not difference_from_means[field]:
						difference_from_means[field] = float(row[field]) ** 2
					else:
						difference_from_means[field] += float(row[field]) ** 2
		
		self.print_dict('dfm',difference_from_means)
		variances = dict.fromkeys(self.fieldnames)
		self.standard_devations = dict.fromkeys(self.fieldnames)
		for field in variances:
			if difference_from_means[field]:
				# self.means[field] = "%.2f" % (sum_of_features[field] / self.counts[field])
				variances[field] = difference_from_means[field] / self.counts[field]
				self.standard_devations[field] = math.sqrt(variances[field])
			else:
				print(f"Field {field} has no numerical data, must be categorical")

		self.print_dict('Standard Deviations:', self.standard_devations)