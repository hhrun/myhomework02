from setuptools import find_packages, setup

package_name = 'py_homework02'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hhh',
    maintainer_email='hhh@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'homework02_talker_py = py_homework02.homework02_talker_py:main', 
            'homework02_listener_py = py_homework02.homework02_listener_py:main'
        ],
    },
)
