"""
    Edenchain configuration related
"""
import os

class EdenConfig:
    def __init__(self):
        self.apis=[
            {
            },
            {
                'api_key': 'AIzaSyAxk1aIqRAd4hiaOPHexj3vFXo0gmeEDDE',
                'api_end_point': 'https://104.197.252.130/api'
            }
        ]


    def getConfig(self, network):
        if len(self.apis) <= network or network < 0:
            return False,{}
            
        return True, self.apis[network] 
