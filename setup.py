import setuptools
try:
    import numpy as np
    from Cython.Build import cythonize

    import scipy  # nessesary for cython files
    ext_modules = cythonize([
        'pb_bss/extraction/cythonized/get_gev_vector.pyx',
        'pb_bss/extraction/cythonized/c_eig.pyx',
    ])
    include_dirs = [np.get_include()]
except ModuleNotFoundError as e:
    print("""
This package has some Cython files that will be compilled,\n
when you install this package. The Cython files use numpy and scipy.\n
If you need the cython files, install dependecies before:\n
    'conda install numpy Cython scipy'
or
    'pip install numpy Cython scipy'
""")
    ext_modules = []
    include_dirs = []


setuptools.setup(
    name="pb_bss_eval",
    version='0.0.1',
    author="Lukas Drude",
    author_email="mail@lukas-drude.de",

    description="EM algorithms for integrated spatial and spectral models.",
    long_description=open('README.md', encoding='utf-8').read(),

    packages=setuptools.find_packages(),

    install_requires=[
        # Strict InputMetrics / OutputMetrics dependencies
        'cached_property',
        'einops',
        'pystoi',
        'mir_eval',
        'pesq'
    ],

    extras_require={
        'all': [
            'dataclasses',
            'matplotlib',
            'scikit-learn',
            'sympy',  # Bingham mixture model symbolic solution dependency
            'soundFile',
            'nara_wpe',
            'lazy_dataset',
            'jsonpickle',
            'pytest',
            'nose',
            'parameterized',
            'pytest-rerunfailures',
            'paderbox @ git+https://github.com/fgnt/paderbox',
        ]
    },

    classifiers=[
        'Programming Language :: Python :: 3.6',
    ],

    ext_modules=ext_modules,
    include_dirs=include_dirs,
)
