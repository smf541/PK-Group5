import unittest
import pkmodel as pk


class SolutionTest(unittest.TestCase):
    """
    Tests the :class:`Solution` class.
    """
    def test_create(self):
        """
        Tests Solution creation.
        """
        solution = pk.Solution()
        self.assertEqual(solution.list, [])

    def test_add(self):
        """
        Tests Solution addition of Models and Protocols.
        """
        solution = pk.Solution()
        model = pk.Model('iv')
        protocol = pk.Protocol()
        with self.assertRaises(TypeError):
            solution.add()
        with self.assertRaises(TypeError):
            solution.add('model')
        with self.assertRaises(TypeError):
            solution.add('model', 'protocol')
        with self.assertRaises(TypeError):
            solution.add(model, 'protocol')
        with self.assertRaises(TypeError):
            solution.add('model', protocol)
        solution.add(model, protocol)
        self.assertEqual(solution.list, [(model, protocol)])
        model2 = pk.Model('sc')
        protocol2 = pk.Protocol(initial_dose=1.1, time_span=1.2)
        solution.add(model2, protocol2)
        self.assertEqual(solution.list, [(model, protocol), (model2, protocol2)])
