import requests

class Ratp:
  def __init__(self):
    self.url = 'https://api-ratp.pierre-grimaud.fr/v4'


  def __fetch(self, route):
    r = requests.get(f'{self.url}{route}')

    return r.json()

  def get_destinations(self, code):
    return self.__fetch(f'/destinations/{self.__get_type(code)}/{code}')

  def get_lines(self, type):
    return self.__fetch(f'/lines/{type}')['result'][type]

  def get_stations(self, type, code):
    return self.__fetch(f'/stations/{type}/{code}')['result']['stations']

  def get_traffic(self, type, code):
    return self.__fetch(f'/traffic/{type}/{code}')['result']['message']
  
  def get_schedules(self, type, code, station, way):
    if way == 'aller':
      parsed_way = 'A'
    elif way == 'retour':
      parsed_way = 'R'
    elif way == 'aller-retour':
      parsed_way = 'A+R'

    return self.__fetch(f'/schedules/{type}/{code}/{station}/{parsed_way}')['result']['schedules']
  



