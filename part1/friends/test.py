import os
import sys
import unittest
from pathlib import Path
from bs4 import BeautifulSoup


BASENAME = 'lesson10-and-tests'
cwd = Path.cwd()
parts = cwd.parts
basefolder_index = parts.index(BASENAME)
basepath = Path(*parts[:basefolder_index + 1])
sys.path.append(str(basepath))
from ttools.skyprotests.tests import SkyproTestCase  # noqa: E402
task_path = basepath.joinpath('part1', 'friends')
os.chdir(task_path)

class TrendTestCase(SkyproTestCase):
    def setUp(self):
        with open("friends.html", 'r') as file:
            soup = BeautifulSoup(file, "html.parser")
        self.main = soup.body.main

    def test_header(self):
        header = self.main.h2
        self.assertIsNotNone(
            header,
            "%@Проверьте, что добавили заголовок 2 уровня.")
        self.assertEqual(
            header.text, 'Ваши друзья',
            "%@Проверьте что заголовок 2 уровня содержит правильный текст")
        
    def test_list(self):
        html_list = self.main.ul
        self.assertIsNotNone(
            html_list,
            "%@Проверьте, что добавили тег 'Маркирвоанный список'")
        li_elements = html_list.find_all('li')
        len_elements = len(li_elements)
        self.assertEqual(
            len_elements, 7,
            ("%@Проверьте что добавили все элементы списка."
             f" Должно быть 7, тогда как у вас {len_elements}"))
        friends = [
            '@happycorgi',
            '@landscapeswow',
            '@skypro',
            '@msverdlove',
            '@inpiration_ru',
            '@techirktsk',
            '@awwawwaww',
        ]
        for trend, element, index in zip(friends, li_elements, range(10)):
            self.assertIsNotNone(
                element.a, "%@Проверьте что все элементы списка содержат тег 'ссылка'"
            )
            self.assertIsNotNone(
                element.a.attrs.get('href'),
                "%@Проверьте что все ссылки имеют аттрибут href"
            )
            self.assertEqual(
                element.a.attrs.get('href'), '#',
                "%@Проверьте, что всем аттрибутам href присвоено значение заглушки '#'"
            )
            self.assertEqual(
                element.a.text, trend,
                f"%@Проверьте, что {index+1} элемент списка имеет верное значение"
            )
        

if __name__ == "__main__":
    unittest.main()