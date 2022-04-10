#include "blis.h"

void blis_gemv_raw(int m, int n, double *c_matrix, double *x, double *y)
{
    double one = 1.0;
    double zero = 0.0;
    bli_dgemv(BLIS_NO_TRANSPOSE, BLIS_NO_CONJUGATE, 
              m, n, &one, c_matrix, n, 1, 
              x, 1, 
              &zero, 
              y, 1);
}
