#!/usr/bin/python3
'''a lazy_matrix_mul function'''
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    '''Multiplies 2 matrices'''
    return np.matmul(m_a, m_b)
    # return np.array(m_a).dot(np.array(m_b))
