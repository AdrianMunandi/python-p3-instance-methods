#!/usr/bin/env python3

import unittest
from dog import Dog
import io
import sys
import types

class TestDog(unittest.TestCase):
    def test_is_class(self):
        '''Dog in dog.py is a class with the name "Dog"'''
        fido = Dog("Buddy", "Golden Retriever")
        self.assertTrue(isinstance(fido, Dog))

class TestBark(unittest.TestCase):
    def test_is_method(self):
        '''Dog.bark() in dog.py is an instance method'''
        fido = Dog("Buddy", "Golden Retriever")
        self.assertTrue(isinstance(fido.bark, types.MethodType))

    def test_prints_woof(self):
        '''Dog.bark() in dog.py prints "Woof!"'''
        fido = Dog("Buddy", "Golden Retriever")
        captured_out = io.StringIO()
        sys.stdout = captured_out
        fido.bark()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_out.getvalue(), "Woof!\n")

class TestSit(unittest.TestCase):
    def test_is_method(self):
        '''Dog.sit() in dog.py is an instance method'''
        fido = Dog("Buddy", "Golden Retriever")
        self.assertTrue(isinstance(fido.sit, types.MethodType))

    def test_prints_the_dog_is_sitting(self):
        '''Dog.sit() in dog.py prints "The dog is sitting."'''
        fido = Dog("Buddy", "Golden Retriever")
        captured_out = io.StringIO()
        sys.stdout = captured_out
        fido.sit()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_out.getvalue(), "The dog is sitting.\n")

if __name__ == '__main__':
    unittest.main()
