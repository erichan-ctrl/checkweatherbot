import unittest
from main_weather_tg_bot import get_weather
from googletrans import Translator


class TestBot(unittest.TestCase):

  async def test_incorrect_city(self):
    self.assertEqual(await get_weather('sdsdsd'), "✨ Проверьте название города ✨")

  async def test_correct_city(self):
    self.assertIsNotNone(await get_weather('Москва'))
  

class TestTranslator(unittest.TestCase):
  def setUp(self):
    self.translator = Translator()

  async def test_translated_city(self):
    self.assertEqual(self.translator.translate("Moscow").text, 'Москва')
