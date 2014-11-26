"""
Barbican attestation request plugin Setup class
#boat/attestation/setup.py
"""
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='attestation-plugin',
    version='1.0',

    description='Barbican OAT Attestation Plugin',

    author='BlueChip',
    author_email='divya.chandra.sekar@west.cmu.edu',

    url='https://github.com/divya-csekar/barbican',
    download_url='http://divya-csekar.github.io/barbican/',

    classifiers=['Development Status :: 3 - Alpha',
                 'License :: OSI Approved :: Apache Software License',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.2',
                 'Programming Language :: Python :: 3.3',
                 'Intended Audience :: Developers',
                 'Environment :: Console',
                 ],

    platforms=['Any'],

    scripts=[],

    provides=['boat.attestation',
              ],

    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'boat.attestation.attester': [
            'simple = boat.attestation.simple_attest:SimpleAttestPlugin',
        ],
    },

    zip_safe=False,
)

