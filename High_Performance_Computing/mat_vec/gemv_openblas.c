#include "cblas.h"

void blas_gemv_raw(int m, int n, double *c_matrix, double *x, double *y)
{
    double one = 1.0;
    double zero = 0.0;
    int ione= 1;

    cblas_dgemv(CblasRowMajor, CblasNoTrans, 
                m, n, 1, 
                c_matrix, n, x, 1, 0, y, 1);
}
