from setuptools import setup, Extension

module1 = Extension('gemv',
                    sources=['gemvmodule.c'],
                    extra_objects=['gemv_blis.o', '/home/dhruv/blis/lib/libblis.a', 
                                   'gemv_blas.o', '/home/dhruv/OpenBLAS/lib/libopenblas.a'],
                    libraries=['m', 'pthread'],
                    extra_compile_args=['-fopenmp'],
                    extra_link_args=['-fopenmp', '-m64'])

setup(name='gemv', version='0.1',
      ext_modules=[module1])
