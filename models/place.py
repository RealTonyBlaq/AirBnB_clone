#!/usr/bin/python3
"""Script that define the class place"""
from models.base_model import BaseModel


class Place(BaseModel):
    """class Place that inherit from BaseModel

    Attributes:
        city_id (str): city id
        user_id (str): The user id
        name (str): name of the place
        description (str): description of the place
        number_rooms (int): The number of rooms
        number_bathrooms (int): The number of bathrooms
        max_guest (int): maximum number of guests
        price_by_night (int): price per night
        latitude (float): The latitude of the place
        longitude (float): The longitude of the place
        amenity_ids (list): list of amenity id
    """

    city_id = " "
    user_id = " "
    name = " "
    description = " "
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
