class CDLayer(object):
	def __init__(self):
		self.attributes = {}
		self.attributes['type'] = 'TYPE'
		self.attributes['index'] = 'INDEX'
		self.attributes['units'] = 'INT'
		self.attributes['activation'] = ['relu', 'softmax', 'elu', 'selu', 'softplus', 'softsign', 'tanh',
											 'hard_sigmoid', 'linear']
		self.attributes['activation_value'] = 0
		self.attributes['use_bias'] = 'BOOL'
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
		self.attributes['kernel_size'] = 'INT'
		self.attributes['strides'] = 2
		self.attributes['padding'] = ['same', 'valid']
		self.attributes['padding_value'] = 0
		self.attributes['dilation_rate'] = 2


class Dense(CDLayer):
	def __init__(self, index):
		super().__init__()
		self.attributes['type'] = 'Dense'
		self.attributes['filters'] = 'NA'
		self.attributes['kernel_size'] = 'NA'
		self.attributes['strides'] = 'NA'
		self.attributes['padding'] = 'NA'
		self.attributes['dilation_rate'] = 'NA'
		self.attributes['index'] = index

class Conv1D(CDLayer):
	def __init__(self, index):
		super().__init__()
		self.attributes['strides'] = 1
		self.attributes['type'] = 'Conv1D'
		self.attributes['units'] = 'NA'
		self.attributes['index'] = index


class Conv2D(CDLayer):
	def __init__(self, index):
		super().__init__()
		self.attributes['strides'] = 2
		self.attributes['type'] = 'Conv2D'
		self.attributes['units'] = 'NA'
		self.attributes['index'] = index

class Conv3D(CDLayer):
	def __init__(self, index):
		super().__init__()
		self.attributes['strides'] = 3
		self.attributes['type'] = 'Conv3D'
		self.attributes['units'] = 'NA'
		self.attributes['index'] = index


class CDFactory:
	def __init__(self):
		self.Product = []

	def make(self, Type, index):
		Temp = CDLayer()
		accept_list = ['Dense', 'Conv1D', 'Conv2D', 'Conv3D']
		if Type not in accept_list:
			print('Wrong input type')
			raise TypeError
		else:
			if Type == 'Dense':
				return Dense(index)
			else:
				if Type == 'Conv1D':
					return Conv1D(index)
				elif Type == 'Conv2D':
					return Conv2D(index)
				else:
					return Conv3D(index)










