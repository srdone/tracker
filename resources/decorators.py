def rename(newname):
	'Creates a decorator that allows customization of function name for later printing'
	def decorator(f):
		f.__name__ = newname
		return f
	return decorator