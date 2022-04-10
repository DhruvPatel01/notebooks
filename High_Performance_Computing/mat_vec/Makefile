BLIS_LIB  := $(HOME)/blis/lib/libblis.a
BLIS_INC  := $(HOME)/blis/include/blis
BLAS_LIB  := $(HOME)/OpenBLAS/lib/libopenblas.a
BLAS_INC  := $(HOME)/OpenBLAS/include

# indicate how the object files are to be created
CC         := gcc
LINKER     := $(CC)
CFLAGS     := -O3 -m64 -mavx2 -std=c99 -march=native -fopenmp -D_POSIX_C_SOURCE=200809L
LDFLAGS    := -lpthread -m64 -lm -fopenmp

clean: *.o *.so build
	rm -rf *.o *.so build

obj_blis: gemv_blis.c
	$(CC) -c $(CFLAGS) -I$(BLIS_INC) gemv_blis.c

obj_blas: gemv_openblas.c
	$(CC) -c $(CFLAGS) -I$(BLAS_INC) gemv_openblas.c -o gemv_blas.o


# gemv: obj_blis obj_blas
# 	$(CC)  -shared gemv_blis.o gemv_blas.o $(BLIS_LIB) $(BLAS_LIB) -o gemv.so $(LDFLAGS)

py: clean obj_blis obj_blas
	python setup.py build_ext --inplace