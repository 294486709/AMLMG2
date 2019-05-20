import numpy as np


class CDLayer(object):
	attributes = {}
	def __init__(self):
		self.attributes['units'] = 'INT'
		self.attributes['activation'] = ['softmax', 'elu', 'selu', 'softplus', 'softsign', 'relu', 'tanh',
										 'hard_sigmoid', 'linear']
		self.attributes['use_bias'] = 'BOOL'
		self.attributes['kernel_initializer'] = ['truncatednormal', 'ones', 'initializer', 'randomnormal',
												 'randomuniform', 'variancescaling', 'orthogonal',
												 'identity', 'constant', 'zeros', 'glort_normal', 'florot_uniform',
												 'be_normal', 'lecun_normal', 'he_uniform', 'lecun_uniform']
		self.attributes['bias_initializer'] = ['truncatednormal', 'ones', 'initializer', 'randomnormal',
											   'randomuniform', 'variancescaling', 'orthogonal',
											   'identity', 'constant', 'zeros', 'glort_normal', 'florot_uniform',
											   'be_normal', 'lecun_normal', 'he_uniform', 'lecun_uniform']
		self.attributes['kernel_regularizer'] = ['l1', 'l2']
		self.attributes['bias_initializer'] = ['truncatednormal', 'ones', 'initializer', 'randomnormal',
											   'randomuniform', 'variancescaling', 'orthogonal',
											   'identity', 'constant', 'zeros', 'glort_normal', 'florot_uniform',
											   'be_normal', 'lecun_normal', 'he_uniform', 'lecun_uniform']
		self.attributes['activity_regularizer'] = ['l1', 'l2']
		self.attributes['kernel_constraint'] = ['max_norm', 'non_neg', 'unit_norm', 'min_max_norm']
		self.attributes['bias_constraint'] = ['max_norm', 'non_neg', 'unit_norm', 'min_max_norm']
		self.attributes['filters'] = 'INT'
		self.attributes['kernel_size'] = 'INT'
		self.attributes['strides'] = 2
		self.attributes['padding'] = ['same', 'valid']
		self.attributes['dilation_rate'] = 2


class Dense(CDLayer):
	def __init__(self):
		super(Dense, self).__init__()
		self.attributes['filters'] = 'NA'
		self.attributes['kernel_size'] = 'NA'
		self.attributes['strides'] = 'NA'
		self.attributes['padding'] = 'NA'
		self.attributes['dilation_rate'] = 'NA'

class CDFactory(CDLayer):
	def __init__(self, type):
		accept_list = ['Dense', 'Conv1D', 'Conv2D', 'Conv3D']
		if type not in accept_list:
			print('Wrong input type')
			raise TypeError
		else:
			super(CDFactory, self).__init__()
			if type == 'Dense':
				self.attributes['filters'] = 'NA'
				self.attributes['kernel_size'] = 'NA'
				self.attributes['strides'] = 'NA'
				self.attributes['padding'] = 'NA'
				self.attributes['dilation_rate'] = 'NA'
			else:
				self.attributes['units'] = 'NA'
				if type == 'Conv1D':
					self.attributes['strides'] = 1
				elif type == 'Conv2D':
					self.attributes['strides'] = 2
				else:
					self.attributes['strides'] = 3

			self.return_result()
	def return_result(self):
		return self


print(CDFactory('Conv3D').attributes['strides'])






