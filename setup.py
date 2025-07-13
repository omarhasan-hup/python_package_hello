from setuptools import setup, find_packages 

setup(
    name='hello_package',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts':[
            'hi=hello.hello:main',
            'hi2=hello.hello:hello2',
            'hi3=another_hi.another:new_hi'
            ]
    }

)