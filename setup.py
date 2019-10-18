from setuptools import setup

package_name = 'envirophat_node'

setup(
    name=package_name,
    version='0.0.1',
    packages=[],
    data_files = [
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/example.launch.py']),
    ],
    py_modules=[
        'src/envirophat_node',
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Michael Ramos',
    author_email="cheymber@protonmail.com",
    maintainer='Michael Ramos',
    maintainer_email="cheymber@protonmail.com",
    keywords=['ROS', 'ROS2'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='ROS2 node for the Pimeroni Envirophat',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'envirophat_node = src.envirophat_node:main',
        ],
    },
)
