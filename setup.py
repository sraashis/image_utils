from setuptools import setup

setup(name='imgcommons',
      version='0.33',
      description='Simple but very useful image related utilities',
      url='https://github.com/sraashis/image_utils',
      download_url='https://github.com/sraashis/imgcommons/releases/tag/Working',
      author='Aashis Khanal',
      author_email='sraahis@gmail.com',
      license='MIT',
      packages=['imgcommons'],
      install_requires=['numpy', 'PILLOW', 'scipy', 'opencv-python'],
      classifiers=[
          "Programming Language :: Python :: 3",
          'License :: OSI Approved :: MIT License',
          "Operating System :: OS Independent",
      ],
      zip_safe=True)
