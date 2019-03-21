from setuptools import setup, find_packages

setup(name='eden client  sdk', version='0.2', description='eden client sdk',  author='Jacki.heo', author_email='jacki.heo@edenchain.io', license='MIT', packages= find_packages() , 
        install_requires=[
            'requests',
            'base58',
            'cryptoconditions',
            'python-rapidjson',
            'pysha3',
            'eth_account'
        ],
        zip_safe=False)
