#!/usr/bin/python3
"""This is the test class for console."""


import unittest
from unittest.mock import patch
from io import StringIO
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """Test the HBNBCommand class"""

    @classmethod
    def setUpClass(cls):
        """Set up the test class"""
        cls.state = State(name="California")
        cls.state.save()
        cls.city = City(state_id=cls.state.id, name="San Francisco")
        cls.city.save()
        cls.amenity = Amenity(name="Pool")
        cls.amenity.save()
        cls.user = User(first_name="Betty", last_name="Bar", email="bar@example.com", password="password")
        cls.user.save()
        cls.place = Place(city_id=cls.city.id, user_id=cls.user.id, name="House", description="A cozy house",
                          number_rooms=3, number_bathrooms=2, max_guest=4, price_by_night=150, latitude=37.77,
                          longitude=-122.42)
        cls.place.save()
        cls.review = Review(place_id=cls.place.id, user_id=cls.user.id, text="Nice place!")
        cls.review.save()

    @classmethod
    def tearDownClass(cls):
        """Tear down the test class"""
        storage.delete(cls.state)
        storage.delete(cls.city)
        storage.delete(cls.amenity)
        storage.delete(cls.user)
        storage.delete(cls.place)
        storage.delete(cls.review)
        storage.save()

    def test_create(self):
        """Test create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create State name="New York"')
            output = f.getvalue().strip()
            self.assertTrue(len(output) > 0)  # Ensure ID is printed
            all_states = storage.all(State)
            self.assertTrue(any(state.name == "New York" for state in all_states.values()))

    def test_show(self):
        """Test show command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show User {self.user.id}')
            output = f.getvalue().strip()
            self.assertIn(f"[User] ({self.user.id})", output)

    def test_destroy(self):
        """Test destroy command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'destroy User {self.user.id}')
            output = f.getvalue().strip()
            self.assertEqual(output, '')
            self.assertIsNone(storage.all(User).get(f'User.{self.user.id}'))

    def test_update(self):
        """Test update command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update User {self.user.id} first_name "John"')
            output = f.getvalue().strip()
            self.assertEqual(output, '')
            self.assertEqual(storage.all(User)[f'User.{self.user.id}'].first_name, 'John')

    def test_all(self):
        """Test all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('all User')
            output = f.getvalue().strip()
            self.assertIn(f"[User] ({self.user.id})", output)
            self.assertGreater(len(output), 0)

    def test_class_all(self):
        """Test class_all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('class_all User')
            output = f.getvalue().strip()
            self.assertIn(f"[User] ({self.user.id})", output)
            self.assertGreater(len(output), 0)

    def test_count(self):
        """Test count command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('count User')
            output = f.getvalue().strip()
            self.assertEqual(output, '1')

    def test_show_class(self):
        """Test show_class command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show_class User {self.user.id}')
            output = f.getvalue().strip()
            self.assertIn(f"[User] ({self.user.id})", output)

    def test_destroy_class(self):
        """Test destroy_class command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'destroy_class User {self.user.id}')
            output = f.getvalue().strip()
            self.assertEqual(output, '')
            self.assertIsNone(storage.all(User).get(f'User.{self.user.id}'))

    def test_update_class(self):
        """Test update_class command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update_class User {self.user.id} first_name "John"')
            output = f.getvalue().strip()
            self.assertEqual(output, '')
            self.assertEqual(storage.all(User)[f'User.{self.user.id}'].first_name, 'John')

    def test_update_dict(self):
        """Test update_dict command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update_dict User {self.user.id} "{{\'first_name\': \'John\', \'last_name\': \'Doe\'}}"')
            output = f.getvalue().strip()
            self.assertEqual(output, '')
            user = storage.all(User)[f'User.{self.user.id}']
            self.assertEqual(user.first_name, 'John')
            self.assertEqual(user.last_name, 'Doe')

    def test_create_invalid_class(self):
        """Test create command with invalid class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create InvalidClass')
            output = f.getvalue().strip()
            self.assertEqual(output, '** class doesn\'t exist **')

    def test_show_missing_class(self):
        """Test show command with missing class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show')
            output = f.getvalue().strip()
            self.assertEqual(output, '** class name missing **')

    def test_show_missing_id(self):
        """Test show command with missing id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show User')
            output = f.getvalue().strip()
            self.assertEqual(output, '** instance id missing **')

    def test_show_invalid_id(self):
        """Test show command with invalid id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show User InvalidID')
            output = f.getvalue().strip()
            self.assertEqual(output, '** no instance found **')

    def test_destroy_missing_class(self):
        """Test destroy command with missing class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('destroy')
            output = f.getvalue().strip()
            self.assertEqual(output, '** class name missing **')

    def test_destroy_missing_id(self):
        """Test destroy command with missing id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('destroy User')
            output = f.getvalue().strip()
            self.assertEqual(output, '** instance id missing **')

    def test_destroy_invalid_id(self):
        """Test destroy command with invalid id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('destroy User InvalidID')
            output = f.getvalue().strip()
            self.assertEqual(output, '** no instance found **')

    def test_update_missing_class(self):
        """Test update command with missing class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('update')
            output = f.getvalue().strip()
            self.assertEqual(output, '** class name missing **')

    def test_update_missing_id(self):
        """Test update command with missing id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('update User')
            output = f.getvalue().strip()
            self.assertEqual(output, '** instance id missing **')

    def test_update_missing_attr(self):
        """Test update command with missing attribute"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('update User 1234')
            output = f.getvalue().strip()
            self.assertEqual(output, '** attribute name missing **')

    def test_update_missing_value(self):
        """Test update command with missing value"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('update User 1234 first_name')
            output = f.getvalue().strip()
            self.assertEqual(output, '** value missing **')

    def test_update_invalid_class(self):
        """Test update command with invalid class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('update InvalidClass 1234 first_name "John"')
            output = f.getvalue().strip()
            self.assertEqual(output, '** class doesn\'t exist **')

    def test_update_invalid_id(self):
        """Test update command with invalid id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('update User InvalidID first_name "John"')
            output = f.getvalue().strip()
            self.assertEqual(output, '** no instance found **')

    def test_update_invalid_dict(self):
        """Test update_dict command with invalid dictionary"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('update_dict User {first_name: "John"}')
            output = f.getvalue().strip()
            self.assertEqual(output, '** invalid dictionary representation **')

    def test_count_missing_class(self):
        """Test count command with missing class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('count')
            output = f.getvalue().strip()
            self.assertEqual(output, '** class name missing **')

    def test_count_invalid_class(self):
        """Test count command with invalid class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('count InvalidClass')
            output = f.getvalue().strip()
            self.assertEqual(output, '** class doesn\'t exist **')

    def test_show_class_missing_class(self):
        """Test show_class command with missing class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show_class')
            output = f.getvalue().strip()
            self.assertEqual(output, '** class name missing **')

    def test_show_class_missing_id(self):
        """Test show_class command with missing id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show_class User')
            output = f.getvalue().strip()
            self.assertEqual(output, '** instance id missing **')

    def test_show_class_invalid_id(self):
        """Test show_class command with invalid id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show_class User InvalidID')
            output = f.getvalue().strip()
            self.assertEqual(output, '** no instance found **')

    def test_destroy_class_missing_class(self):
        """Test destroy_class command with missing class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('destroy_class')
            output = f.getvalue().strip()
            self.assertEqual(output, '** class name missing **')

    def test_destroy_class_missing_id(self):
        """Test destroy_class command with missing id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('destroy_class User')
            output = f.getvalue().strip()
            self.assertEqual(output, '** instance id missing **')

    def test_destroy_class_invalid_id(self):
        """Test destroy_class command with invalid id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('destroy_class User InvalidID')
            output = f.getvalue().strip()
            self.assertEqual(output, '** no instance found **')

    def test_update_class_missing_class(self):
        """Test update_class command with missing class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('update_class')
            output = f.getvalue().strip()
            self.assertEqual(output, '** class name missing **')

    def test_update_class_missing_id(self):
        """Test update_class command with missing id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('update_class User')
            output = f.getvalue().strip()
            self.assertEqual(output, '** instance id missing **')

    def test_update_class_missing_attr(self):
        """Test update_class command with missing attribute"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('update_class User 1234')
            output = f.getvalue().strip()
            self.assertEqual(output, '** attribute name missing **')

    def test_update_class_missing_value(self):
        """Test update_class command with missing value"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('update_class User 1234 first_name')
            output = f.getvalue().strip()
            self.assertEqual(output, '** value missing **')

    def test_update_class_invalid_class(self):
        """Test update_class command with invalid class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('update_class InvalidClass 1234 first_name "John"')
            output = f.getvalue().strip()
            self.assertEqual(output, '** class doesn\'t exist **')

    def test_update_class_invalid_id(self):
        """Test update_class command with invalid id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('update_class User InvalidID first_name "John"')
            output = f.getvalue().strip()
            self.assertEqual(output, '** no instance found **')

    def test_update_dict_invalid_dict(self):
        """Test update_dict command with invalid dictionary"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('update_dict User 1234 {first_name: "John"}')
            output = f.getvalue().strip()
            self.assertEqual(output, '** invalid dictionary representation **')

if __name__ == '__main__':
    unittest.main()
