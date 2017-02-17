from PIL import Image, ImageDraw

# Used to map the generation of the tree
class Node(object):
	def __init__(self, sketcher, position):
		self.sketcher = sketcher
		self.x, self.y = position
		self.cluster = []
		self.grandchildren = []
		self.children = []
		self.parent = None

		# Will be used to render the tree using the 'nodeList' collection
	def set_parent(self, p):
		self.parent = p

	def set_children(self, children):
		self.children = children

	def add_child(self, c):
		self.children.append(c)

	def set_cluster(self, cluster):
		self.cluster = cluster

	def add_cluster_node(self, c):
		self.cluster.append(c)

	def set_grandchildren(self, grandchildren):
		self.grandchildren = grandchildren

	def add_grandchild(self, g):
		self.grandparents.append(g)

class Sketcher(object):
	def __init__(self, image):
		self.image = image
		self.width, self.height = self.image.size
		self.nodeList = []

		self.root = Node(self, (960, 540))
		self.nodeList.append(self.root)

		self.create_tree()
		self.create_tree()
		self.create_tree()

		self.draw = ImageDraw.Draw(self.image)

		self.render_tree(self.root, self.draw)

	def render_tree(self, n, draw):
		if n.cluster:
			if n.children:
				for c in n.cluster:
					for ch in n.children:
						draw.line((n.x, n.y, ch.x, ch.y), fill=128)
						draw.line((c.x, c.y, ch.x, ch.y), fill=128)
						if ch.cluster:
							for ch_c in ch.cluster:
								draw.line((n.x, n.y, ch_c.x, ch_c.y), fill=128)
								draw.line((c.x, c.y, ch_c.x, ch_c.y), fill=128)
						self.render_tree(ch, draw)

	def create_tree(self):
		#while self.nodeList:
		current = self.nodeList.pop(0)
		next = Node(self, (current.x, current.y-200))
		self.nodeList.append(next)
		current.add_child(next)
		next.set_parent(current)

		cluster_1 = Node(self, (current.x + 5, current.y + 5))
		cluster_2 = Node(self, (current.x - 5, current.y - 5))
		cluster_3 = Node(self, (current.x - 7, current.y))
		cluster_4 = Node(self, (current.x + 7, current.y))
		current.set_cluster([cluster_1, cluster_2, cluster_3, cluster_4])




def main():
	new_image = Image.new('RGB', (1920, 1080), (255, 255, 255))

	sketcher = Sketcher(new_image);

	new_image.save('test.png')


if __name__ == "__main__":
	main()
