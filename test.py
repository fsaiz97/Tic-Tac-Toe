import unittest

from game_logic_classes import Coordinate


class TestCoordinate(unittest.TestCase):
    def test_eq_method(self):
        """Tests if Coordinates __eq__ method works as intended."""
        self.assertEqual(Coordinate(1, 2), Coordinate(1, 2))

    def test_transform_string_to_coordinate_Using_valid_string(self):
        """Tests if Coordinate can transform a valid string into a Coordinate instance"""

        coord_string = "1 2"
        coord = Coordinate.transform_string_to_coordinate(coord_string)

        self.assertEqual(coord, Coordinate(1, 2))

    def test_transform_string_to_coordinate_When_char_input_Raise_ValueError(self):
        """Tests if transform_string_to_coordinate raises ValueError on char input"""
        coord_string = "a b"

        with self.assertRaises(ValueError):
            Coordinate.transform_string_to_coordinate(coord_string)

    def test_transform_string_to_coordinate_Wrong_dimension_Raises_TypeError(self):
        """Tests if transform_string_to_coordinate will accept a string with the wrong dimension."""
        coord_string = "1 2 3"

        with self.assertRaises(TypeError):
            Coordinate.transform_string_to_coordinate(coord_string)


class TestGame(unittest.TestCase):
    pass


if __name__ == "__main__":
    unittest.main()
