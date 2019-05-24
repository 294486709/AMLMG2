class CDLayer(object):
	def __init__(self):
		self.attributes = {}
		self.attributes['type'] = 'TYPE'
		self.attributes['index'] = 'INT'
		self.attributes['units'] = 'INT'
		self.attributes['units_value'] = 16
		self.attributes['activation'] = ['relu', 'softmax', 'elu', 'selu', 'softplus', 'softsign', 'tanh',
											 'hard_sigmoid', 'linear']
		self.attributes['activation_value'] = 0
		self.attributes['use_bias'] = ['False', 'True']
		self.attributes['use_bias_value'] = 0
		self.attributes['kernel_initializer'] = ['None', 'truncatednormal', 'ones', 'initializer', 'randomnormal',
											 'randomuniform', 'variancescaling', 'orthogonal',
											 'identity', 'constant', 'zeros', 'glort_normal', 'florot_uniform',
											 'be_normal', 'lecun_normal', 'he_uniform', 'lecun_uniform']
		self.attributes['kernel_initializer_value'] = 0
		self.attributes['bias_initializer'] = ['None','truncatednormal', 'ones', 'initializer', 'randomnormal',
										   'randomuniform', 'variancescaling', 'orthogonal',
										   'identity', 'constant', 'zeros', 'glort_normal', 'florot_uniform',
										   'be_normal', 'lecun_normal', 'he_uniform', 'lecun_uniform']
		self.attributes['bias_initializer_value'] = 0
		self.attributes['kernel_regularizer'] = ['None','L1', 'L2']
		self.attributes['kernel_regularizer_value'] = 0
		self.attributes['bias_initializer'] = ['None','truncatednormal', 'ones', 'initializer', 'randomnormal',
										   'randomuniform', 'variancescaling', 'orthogonal',
										   'identity', 'constant', 'zeros', 'glort_normal', 'florot_uniform',
										   'be_normal', 'lecun_normal', 'he_uniform', 'lecun_uniform']
		self.attributes['bias_initializer_value'] = 0
		self.attributes['activity_regularizer'] = ['None','L1', 'L2']
		self.attributes['activity_regularizer_value'] = 0
		self.attributes['kernel_constraint'] = ['None','max_norm', 'non_neg', 'unit_norm', 'min_max_norm']
		self.attributes['kernel_constraint_value'] = 0
		self.attributes['bias_constraint'] = ['None','max_norm', 'non_neg', 'unit_norm', 'min_max_norm']
		self.attributes['bias_constraint_value'] = 0
		self.attributes['filters'] = 'INT'
		self.attributes['filters_value'] = 16
		self.attributes['kernel_size'] = 'INT'
		self.attributes['kernel_size_value'] = 16
		self.attributes['strides'] = 'INT'
		self.attributes['strides_value'] = 2
		self.attributes['padding'] = ['same', 'valid']
		self.attributes['padding_value'] = 0



class Dense(CDLayer):
	def __init__(self, index):
		super().__init__()
		self.attributes['type'] = 'Dense'
		self.attributes['filters'] = 'NA'
		self.attributes['kernel_size'] = 'NA'
		self.attributes['strides'] = 'NA'
		self.attributes['padding'] = 'NA'
		self.attributes['index'] = index

class Conv(CDLayer):
	def __init__(self, index):
		super().__init__()
		self.attributes['type'] = 'Conv'
		self.attributes['cnn_type'] = ['Conv1D', 'Conv2D', 'Conv3D']
		self.attributes['cnn_type_value'] = 1
		self.attributes['units'] = 'NA'
		self.attributes['index'] = index


class InputLayer(object):
	def __init__(self, index):
		self.attributes = {}
		self.attributes['type'] = 'INPUT'
		self.attributes['index'] = index
		self.attributes['input_x_file'] = 'NAME'
		self.attributes['input_x_file_value'] = 'xtrain.npy'
		self.attributes['input_y_file'] = 'NAME'
		self.attributes['input_y_file_value'] = 'ytrain.npy'
		self.attributes['training_ratio'] = 'INT1'
		self.attributes['training_ratio_value'] = 80
		self.attributes['model_name'] = 'NAME'
		self.attributes['model_name_value'] = 'model.py'


class OutputLayer(object):
	def __init__(self, index):
		self.attributes = {}
		self.attributes['type'] = 'OUTPUT'
		self.attributes['index'] = index
		self.attributes['output_name'] = 'NAME'
		self.attributes['output_name_value'] = ''

class Pooling(object):
	def __init__(self, index):
		self.attributes = {}
		self.attributes['type'] = 'POOLING'
		self.attributes['index'] = index
		self.attributes['pooling_type'] = ['MaxPooling1D', 'MaxPooling2D', 'MaxPooling3D',
										   'AveragePooling1D', 'AveragePooling2D', 'AveragePooling3D']
		self.attributes['pooling_type_value'] = 1
		self.attributes['pool_size'] = 'INT'
		self.attributes['pool_size_value'] = 2
		self.attributes['strides'] = 'INT'
		self.attributes['strides_value'] = 0
		self.attributes['padding'] = ['valid', 'same']
		self.attributes['padding_value'] = 0

class Compile(object):
	def __init__(self, index):
		self.attributes = {}
		self.attributes['type'] = 'COMPILE'
		self.attributes['index'] = index
		self.attributes['optimizer'] = ['SGD', 'RMSprop', 'Adagrad', 'Adadelta', 'Adam', 'Adamax', 'Nadam']
		self.attributes['optimizer_value'] = 0
		self.attributes['loss'] = ['mean_squared_error', 'mean_absolute_error', 'mean_absolute_percentage_error',
								   'mean_squared_logarithmic_error', 'squared_hinge', 'hinge', 'categorical_hinge',
								   'logcosh', 'categorical_crossentropy', 'sparse_categorical_crossentropy',
								   'binary_crossentropy', 'kullback_leibler_divergence', 'poission', 'cosine_proximity']
		self.attributes['loss_value'] = 0
		self.attributes['metrics'] = ['accuracy', 'None']
		self.attributes['metrics_value'] = 0
		self.attributes['batch_size'] = 'INT'
		self.attributes['batch_size_value'] = 16
		self.attributes['epoch'] = 'INT'
		self.attributes['epoch_value'] = 5


class Flatten(object):
	def __init__(self, index):
		self.attributes = {}
		self.attributes['type'] = 'FLATTEN'
		self.attributes['index'] = index


class LayerFactory:
	def __init__(self):
		self.Product = []

	def make(self, Type, index):
		accept_list = ['Dense', 'Conv', 'Input', 'Output', 'Compile', 'Pooling', 'Flatten']
		if Type not in accept_list:
			print('Wrong input type')
			raise TypeError
		else:
			if Type == 'Dense':
				return Dense(index)
			else:
				if Type == 'Conv':
					return Conv(index)
				elif Type == 'Input':
					return InputLayer(index)
				elif Type == 'Output':
					return OutputLayer(index)
				elif Type == 'Compile':
					return Compile(index)
				elif Type == 'Pooling':
					return Pooling(index)
				elif Type == 'Flatten':
					return Flatten(index)

class InstructionFactory(object):
	def __init__(self):
		pass

	def PropertyManage(self, statement, target, skiplist):

		attributes = target.attributes
		print('----------------')
		print(target)
		for i in attributes:
			print(i)
			if i not in skiplist and i[-6:] != '_value':
				if i == 'strides':
					try:
						matrix = self.MatrixGen(attributes['cnn_type_value']+1, attributes['strides_value'])
					except KeyError:
						try:
							matrix = self.MatrixGen((attributes['pooling_type_value'] + 1) % 3, attributes['strides_value'])
						except:
							pass
					statement += ', {}={}'.format('strides', matrix)
					continue
				if attributes[i] == 'NA':
					continue
				if attributes[i][int(attributes[i + '_value'])] != 'None' and attributes[i][int(attributes[i + '_value'])] != 'False':
					statement += ', {}=\'{}\''.format(i, attributes[i][int(attributes[i + '_value'])])
				else:
					continue
			else:
				continue
		statement += '))\n'
		return statement

	def GenerateInstruction(self, temp, temp0):
		attributes = temp.attributes
		print(temp)
		if type(temp) == type(Dense(999)):
			skiplist = ['type', 'index', 'units', 'activation', 'strides']
			statement = 'model.add(layers.Dense({}, activation=\'{}\''.format(attributes['units_value'], attributes['activation'][(int(attributes['activation_value']))])
			statement = self.PropertyManage(statement, temp, skiplist)
			return statement
		elif type(temp) == type(Flatten(999)):
			statement = 'model.add(layers.Flatten())\n'
			return statement
		elif type(temp) == type(Conv(999)):
			matrix = self.MatrixGen(attributes['cnn_type_value']+1, attributes['kernel_size_value'])
			statement = 'model.add(layers.{}({}, {}, activation=\'{}\''.format(attributes['cnn_type'][attributes['cnn_type_value']], attributes['filters_value'], matrix, attributes['activation'][(int(attributes['activation_value']))])
			skiplist = ['type', 'index', 'units', 'activation', 'kernel_size', 'filters', 'cnn_type', 'pooling_type']
			statement = self.PropertyManage(statement, temp, skiplist)
			return statement
		elif type(temp) == type(Pooling(999)):
			skiplist = ['type', 'index', 'units', 'activation', 'pool_size', 'pooling_type']
			matrix = self.MatrixGen((attributes['pooling_type_value'] + 1)%3, attributes['pool_size_value'])
			statement = 'model.add(layers.{}({}'.format(attributes['pooling_type'][int(attributes['pooling_type_value'])], matrix)
			statement = self.PropertyManage(statement, temp, skiplist)
			return statement
		elif type(temp) == type(Compile(999)):
			statement = 'model.compile(optimizer=\'{}\', loss=\'{}\', metrics=[\'{}\'])\n'.format(attributes['optimizer'][int(attributes['optimizer_value'])],
																				 attributes['loss'][int(attributes['loss_value'])],
																				 attributes['metrics'][int(attributes['metrics_value'])])
			statement += 'xtrain = np.load({})\n'.format(temp0.attributes['input_x_file_value'])
			statement += 'ytrain = np.load({})\n'.format(temp0.attributes['input_y_file_value'])
			statement += 'model.fit({}, {}, epochs={}, batch_size={})\n'.format('xtrain', 'ytrain', temp.attributes['epoch_value'], temp.attributes['batch_size_value'])
			print(statement)
			return statement




	def MatrixGen(self, CnnType, Value):
		matrix = '('
		for i in range(CnnType):
			matrix += '{}, '.format(Value)
		matrix = matrix[:-2]
		matrix += ')'
		return matrix











