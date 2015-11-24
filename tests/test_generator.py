import unittest
import tempdir
from wand.image import Image
from static_map_generator.generator import Generator
import os.path

class MapMakerTests(unittest.TestCase):

    def setUp(self):
        self.tempdir = tempdir.TempDir()

    def tearDown(self):
        pass

    def test_static_map_generator(self):
        file_path = os.path.join(self.tempdir.name, 'test.png')
        width = 500
        height = 500
        simple_config = {
            'params': {
                 'filename': file_path,
                'epsg': 31370,
                'filetype': 'png',
                'width': width,
                'height': height,
                'bbox': [145000, 195000, 165000, 215000]
            },
            'layers':
                [{'layer': {
                    'type': 'text',
                    'name': 'text.png',
                    'text': 'This is a test',
                    'color': '#FF3366',
                    'borderwidth': 0,
                    'font_size': 24,
                    'text_color': '#FF3366'
                }
                  }
                 ]
        }
        Generator.generate(simple_config)
        self.assertTrue(os.path.isfile(file_path))
        image = Image(filename=file_path)
        self.assertEqual(image.width, width)
        self.assertEqual(image.height, height)

    def test_static_map_generator2(self):
        width = 500
        height = 500
        simple_config = {
            'params': {
                'epsg': 31370,
                'filetype': 'png',
                'width': width,
                'height': height,
                'bbox': [145000, 195000, 165000, 215000]
            },
            'layers':
                [{'layer': {
                    'type': 'text',
                    'name': 'text.png',
                    'text': 'This is a test',
                    'color': '#FF3366',
                    'borderwidth': 0,
                    'font_size': 24,
                    'text_color': '#FF3366'
                }
                  }
                 ]
        }
        Generator.generate(simple_config)


    def test_invalid_layer(self):
        file_path = os.path.join(self.tempdir.name, 'test.png')
        width = 500
        height = 500
        simple_config = {
            'params': {
                'filename': file_path,
                'epsg': 31370,
                'filetype': 'png',
                'width': width,
                'height': height,
                'bbox': [145000, 195000, 165000, 215000]
            },
            'layers':
                [
                {'layer': {
                    'type': 'text',
                    'name': 'text.png',
                    'text': 'This is a test',
                    'color': '#FF3366',
                    'borderwidth': 0,
                    'font_size': 24,
                    'text_color': '#FF3366'
                }
                  },
                {'layer': {
             'type': 'wms',
             'name': 'ONBESTAAND',
             'url': 'https://geo.onroerenderfgoed.be/geoserver/wms?',
             'layers': 'vioe_geoportaal:onbestaande_laag'
         }
          }
                 ]
        }
        Generator.generate(simple_config)


    def test_all_types(self):
        file_path = os.path.join(self.tempdir.name, 'test.png')
        width = 500
        height = 500
        config_31370 = {
    'params': {
        'filename': file_path,
        'epsg': 31370,
        'filetype': 'png',
        'width': width,
        'height': height,
        'bbox': [145000, 195000, 165000, 215000]
    },
    'layers':
        [{'layer': {
            'type': 'text',
            'name': 'text.png',
            'text': 'This is a test',
            'color': '#FF3366',
            'borderwidth': 1,
            'font_size': 24,
            'text_color': '#FF3366'
        }
          },
         {'layer': {
             'type': 'logo',
             'name': 'logo.png',
             'path': 'logo.png',
             'opacity': 0.5
         }
          },
         {'layer': {
             'type': 'wkt',
             'name': 'WKT',
             'wkt': 'POLYGON ((155000 215000, 160000 210000, 160000 215000, 155000 215000))',
             'color': 'steelblue',
             'opacity': 0.5
         }
          },
         {'layer': {
             'type': 'wms',
             'name': 'OE',
             'url': 'https://geo.onroerenderfgoed.be/geoserver/wms?',
             'layers': 'vioe_geoportaal:landschapsbeheersplannen',
             'featureid': 'landschapsbeheersplannen.3816'
         }
          },
         {'layer': {
             'type': 'wms',
             'name': 'ONBESTAAND',
             'url': 'https://geo.onroerenderfgoed.be/geoserver/wms?',
             'layers': 'vioe_geoportaal:onbestaande_laag'
         }
          },
         {'layer': {
             'type': 'wms',
             'name': 'GRB',
             'url': 'http://geo.api.agiv.be/geodiensten/raadpleegdiensten/GRB-basiskaart/wmsgr?',
             'layers': 'GRB_BSK'
         }
          }
         ]
}
        Generator.generate(config_31370)