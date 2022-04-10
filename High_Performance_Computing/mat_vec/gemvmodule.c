#define PY_SSIZE_T_CLEAN
#include <Python.h>

void blis_gemv_raw(int m, int n, const double *c_matrix, const double *x, double *y);
void blas_gemv_raw(int m, int n, const double *c_matrix, const double *x, double *y);

static PyObject *
blis_dgemv(PyObject *self, PyObject *args)
{
    const void  *a;
    Py_ssize_t asize;
    Py_buffer in_buf, out_buf;
    in_buf.buf = out_buf.buf = NULL;
    in_buf.len = out_buf.len = 0;

    if (!PyArg_ParseTuple(args, "s#s*s*", &a, &asize, &in_buf, &out_buf)) {
        if (in_buf.buf) PyBuffer_Release(&in_buf);
        if (out_buf.buf) PyBuffer_Release(&out_buf);
        return NULL;
    }

    int m, n;
    m = out_buf.len/sizeof(double);
    n = in_buf.len/sizeof(double);
    
    blis_gemv_raw(m, n, a, in_buf.buf, out_buf.buf);
    
	Py_RETURN_NONE;
}

static PyObject *
blas_dgemv(PyObject *self, PyObject *args)
{
    const void  *a;
    Py_ssize_t asize;
    Py_buffer in_buf, out_buf;
    in_buf.buf = out_buf.buf = NULL;
    in_buf.len = out_buf.len = 0;

    if (!PyArg_ParseTuple(args, "s#s*s*", &a, &asize, &in_buf, &out_buf)) {
        if (in_buf.buf) PyBuffer_Release(&in_buf);
        if (out_buf.buf) PyBuffer_Release(&out_buf);
        return NULL;
    }

    int m, n;
    m = out_buf.len/sizeof(double);
    n = in_buf.len/sizeof(double);
    
    blas_gemv_raw(m, n, a, in_buf.buf, out_buf.buf);
    
	Py_RETURN_NONE;
}

static PyMethodDef module_methods[] = {
    {"blis_dgemv", blis_dgemv, METH_VARARGS, NULL},
    {"blas_dgemv", blas_dgemv, METH_VARARGS, NULL},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef gemvmodule = {
    PyModuleDef_HEAD_INIT,
    "gemv",   /* name of module */
    NULL,     /* module documentation, may be NULL */
    -1,       /* size of per-interpreter state of the module,
                 or -1 if the module keeps state in global variables. */
    module_methods
};

PyMODINIT_FUNC
PyInit_gemv(void)
{
    return PyModule_Create(&gemvmodule);
}
