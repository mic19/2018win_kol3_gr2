import unittest
from task import *

#https://github.com/AFrankowicz/kol1_gr2/blob/master/task.py
class test_task(unittest.TestCase):
	def setUp(self):
		self.plane = Plane()

	def test_new_orientation(self):
		self.plane.new_orientation(10)
		self.plane.new_orientation(20)

		self.assertEqual(20, self.plane.orientation)
		self.assertEqual(10, self.plane.prev_orientation)

	def test_correct_orientation(self):
		self.plane.new_orientation(1)
		self.plane.new_orientation(1)
		self.plane.correct_orientation()

		self.assertEqual(0, self.plane.orientation)

	def test_current_orientation(self):
		self.assertEqual("Current orientation is: 0.0 degrees.", self.plane.current_orientation())

	def test_did_crach(self):
		pass
		#self.plane.new_orientation(-271)
		#self.assertRaises(SystemExit, self.plane.did_crash())

if __name__ == "__main__":
	unittest.main()

