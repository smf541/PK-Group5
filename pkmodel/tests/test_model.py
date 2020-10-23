import unittest
import pkmodel as pk


class ModelTest(unittest.TestCase):
    """
    Tests the :class:`Model` class.
    """
    def test_create(self):
        """
        Tests Model creation.
        """
        with self.assertRaises(ValueError):
            model = pk.Model('string')
        model = pk.Model('sc')
        self.assertEqual(model.name, 'Model-sc-V_c=1.0-CL=1.0-Ka=1.0-0compartments')  # noqa: E501
        # inline comment to flake8 to ignore line length required for name

    def test_encapsulation(self):
        """
        Tests Model values are encapsulated.
        """
        model = pk.Model('sc')
        with self.assertRaises(AttributeError):
            model.Name
        with self.assertRaises(AttributeError):
            model.V_c
        with self.assertRaises(AttributeError):
            model.CL
        with self.assertRaises(AttributeError):
            model.Ka
        with self.assertRaises(AttributeError):
            model._Name
        with self.assertRaises(AttributeError):
            model._V_c
        with self.assertRaises(AttributeError):
            model._CL
        with self.assertRaises(AttributeError):
            model._Ka
        with self.assertRaises(AttributeError):
            model.__Name
        with self.assertRaises(AttributeError):
            model.__V_c
        with self.assertRaises(AttributeError):
            model.__CL
        with self.assertRaises(AttributeError):
            model.__Ka

    def test_create_defaults(self):
        """
        Tests Model creation default values.
        """
        model = pk.Model('iv')
        self.assertEqual(model.v_c, 1.0)
        self.assertEqual(model.cl, 1.0)
        self.assertEqual(model.ka, 1.0)

    def test_create_initvalues(self):
        """
        Tests Model creation with initial values.
        """
        model = pk.Model('iv', V_c=1.1, CL=1.2, Ka=1.4)
        self.assertEqual(model.v_c, 1.1)
        self.assertEqual(model.cl, 1.2)
        self.assertEqual(model.ka, 1.4)

    def test_create_initvalues_typeerror(self):
        """
        Tests Model creation with initial values.
        """
        with self.assertRaises(TypeError):
            model = pk.Model('iv', V_c='a')
        with self.assertRaises(TypeError):
            model = pk.Model('iv', CL='b')
        with self.assertRaises(TypeError):
            model = pk.Model('iv', Ka='c')  # noqa: F841
            # inline comment tells flake8 to ignore unused variable for test

    def test_compartments(self):
        """
        Tests Model compartments.
        """
        model = pk.Model('iv')
        with self.assertRaises(TypeError):
            model.add_compartment()
        with self.assertRaises(TypeError):
            model.add_compartment(1.0)
        with self.assertRaises(TypeError):
            model.add_compartment('a', 'b')
        added = model.add_compartment(V_p_new=1.0, Q_p_new=1.1)  # noqa: F841
        # inline comment tells flake8 to ignore unused variable for test
        self.assertEqual(model.list_compartments(), [[1.0, 1.1]])
        model.add_compartment(1.2, 1.3)
        self.assertEqual(model.list_compartments(), [[1.0, 1.1], [1.2, 1.3]])

