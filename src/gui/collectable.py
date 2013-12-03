from gui import entity

class Collectable(entity.Entity):
	"""A collectable in the game gui"""
	
	_id = 0
	
	def __init__(self, screen, image, x, y, id):
		self._id = id
		self.init(screen, image, x ,y)