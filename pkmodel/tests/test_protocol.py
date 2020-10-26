import unittest
import pkmodel as pk


class ProtocolTest(unittest.TestCase):
    """
    Tests the :class:`Protocol` class.
    """
    def test_create(self):
        """
        Tests Protocol creation.
        """
        with self.assertRaises(TypeError):
            protocol = pk.Protocol('string')
        protocol = pk.Protocol()
        self.assertEqual(protocol.name,
                         'Protocol-initial_dose=1.0-time_span=1.0')

    def test_encapsulation(self):
        """
        Tests Protocol values are encapsulated.
        """
        protocol = pk.Protocol()
        with self.assertRaises(AttributeError):
            protocol.Name
        with self.assertRaises(AttributeError):
            protocol.Initial_dose
        with self.assertRaises(AttributeError):
            protocol.Time_span
        with self.assertRaises(AttributeError):
            protocol._Name
        with self.assertRaises(AttributeError):
            protocol._Initial_dose
        with self.assertRaises(AttributeError):
            protocol._Time_span
        with self.assertRaises(AttributeError):
            protocol.__Name
        with self.assertRaises(AttributeError):
            protocol.__Initial_dose
        with self.assertRaises(AttributeError):
            protocol.__Time_span

    def test_create_defaults(self):
        """
        Tests Protocol creation default values.
        """
        protocol = pk.Protocol()
        self.assertEqual(protocol.initial_dose, 1.0)
        self.assertEqual(protocol.time_span, 1.0)

    def test_create_initvalues(self):
        """
        Tests Protocol creation with initial values.
        """
        protocol = pk.Protocol(initial_dose=1.1, time_span=1.2)
        self.assertEqual(protocol.initial_dose, 1.1)
        self.assertEqual(protocol.time_span, 1.2)

    def test_create_initvalues_typeerror(self):
        """
        Tests Protocol creation with invalid initial values.
        """
        with self.assertRaises(TypeError):
            protocol = pk.Protocol(inital_dose='a')
        with self.assertRaises(TypeError):
            protocol = pk.Protocol(time_span='b')  # noqa: F841
            # inline comment tells flake8 to ignore unused variable for test

    def test_create_dose(self):
        """
        Tests Protocol dose function creation.
        """
        protocol = pk.Protocol()
        dose = protocol.dose
        self.assertEqual(str(type(dose)), "<class 'function'>")
        dose_func_in = lambda y, t: 0
        dose_func_out = protocol.add_dose_function(func=dose_func_in)
        self.assertEqual(dose_func_in, dose_func_out)
        with self.assertRaises(TypeError):
            dose_func = lambda z: 0
            protocol.add_dose_function(func=dose_func)
