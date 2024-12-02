import numpy as np
import matplotlib.pyplot as plt

class RandomToggleSet:
    def __init__(self):
        pass

    def add(self, element):
        """
        Add an element, toggling it to True. If the element is already in the set, 
        don't add it twice, but toggle it to True if it isn't already

        Parameters
        ----------
        element: object (hashable)
            Element to add
        """
        pass

    def toggle(self, element):
        """
        Toggle whether an element can be selected or not. Specifically, 
        if the element is in the set and is False, change it to True. 
        If the element is in the set and is True, change it to False
        If the element is not in the set, you should throw an exception
        Parameters
        ----------
        element: object (hashable)
        """
        pass

    def sample(self):
        """
        Select and return an element uniformly at random from among 
        the elements that are set to True

        Returns
        -------
        object: Some object in the set that's set to True
        """
        return None ## TODO: This is a dummy value
    
