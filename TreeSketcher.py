from PIL import Image, ImageDraw



# Used to map the generation of the tree
class Node(object):
	def __init__(self, sketcher, position, parent):
		self.sketcher = sketcher
		self.x, self.y = position
		self.parent = parent


# Will be used to render the tree using the 'nodeList' collection
class Sketcher(object):
	def __init__(self, image):
		self.image = image
		self.width, self.height = self.image.size
		self.nodeList = []

		self.root = Node(self, (960, 540), None)
		self.nodeList.append(self.root)

		self.testNode1 = Node(self, (960, 600), self.root)
		self.nodeList.append(self.testNode1)

		draw = ImageDraw.Draw(self.image)
		for node in self.nodeList:
			if (node.parent != None):
				draw.line((node.x, node.y, node.parent.x, node.parent.y), fill=128)





def main():
	new_image = Image.new('RGB', (1920, 1080), (0, 0, 0))

	sketcher = Sketcher(new_image);

	new_image.save('test.png')


if __name__ == "__main__":
	main()
