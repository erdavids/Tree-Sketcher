from PIL import Image, ImageDraw

# Used to map the generation of the tree
class Node(object):
	def __init__(self, sketcher, position):
		self.sketcher = sketcher
		self.x, self.y = position
		self.parents = []
		self.grandparents = []

		# Will be used to render the tree using the 'nodeList' collection

	def set_parents(self, parents):
		self.parents = parents

	def add_parent(self, p):
		self.parents.append(p)

	def set_grandparents(self, grandparents):
		self.grandparents = grandparents

	def add_grandparent(self, g):
		self.grandparents.append(g)

class Sketcher(object):
	def __init__(self, image):
		self.image = image
		self.width, self.height = self.image.size
		self.nodeList = []

		self.root = Node(self, (960, 540))
		self.nodeList.append(self.root)

		self.testNode1 = Node(self, (960, 600))
		self.nodeList.append(self.testNode1)
		self.testNode1.add_parent(self.root)

		draw = ImageDraw.Draw(self.image)
		for node in self.nodeList:
			if node.parents:
				for p in node.parents:
					draw.line((node.x, node.y, p.x, p.y), fill=128)
			if node.grandparents:
				for g in node.grandparents:
					draw.line((node.x, node.y, g.x, g.y), fill=128)


def main():
	new_image = Image.new('RGB', (1920, 1080), (255, 255, 255))

	sketcher = Sketcher(new_image);

	new_image.save('test.png')


if __name__ == "__main__":
	main()
