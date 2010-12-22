from setuptools import setup, find_packages

setup(
    name='django-jeditable',
    version='0.1.0',
    description='Inplace editing with the Django.',
    author='Neskie Manuel',
    author_email='neskiem@gmail.com',
    url='http://github.com/neskie/django-jeditable/',
    packages=find_packages(),
    package_data = {'jeditable': ['templates/jeditable/*.html',
        'templatetags/*.py']},
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
