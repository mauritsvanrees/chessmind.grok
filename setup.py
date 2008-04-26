from setuptools import setup, find_packages

version = '0.3'

setup(name='chessmind.grok',
      version=version,
      description="Grok UI for ChessMind",
      long_description="""Me Grok Play Chess!\
""",
      # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[], 
      keywords="chess, grok",
      author="Maurits van Rees",
      author_email="maurits@vanrees.org",
      url="http://maurits.vanrees.org/",
      license="GPL",
      package_dir={'': 'src'},
      packages=find_packages('src'),
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'grok',
                        'chessmind.core',
                        # Add extra requirements here
                        ],
      entry_points="""
      # Add entry points here
      """,
      )
