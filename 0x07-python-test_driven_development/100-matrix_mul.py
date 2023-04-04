#!/usr/bin/python3
'''a get_matrix_size and a matrix_mul function'''


def get_matrix_size(matrix, name):
    '''Computes the size of a matrix and performs some
    matrix validation'''
    error_messages = (
        '{} must be a list'.format(name),
        '{} can\'t be empty'.format(name),
        '{} must be a list of lists'.format(name),
        '{} should contain only integers or floats'.format(name),
        'each row of {} must be of the same size'.format(name),
    )
    size = [0, 0]
    if not isinstance(matrix, list):
        raise TypeError(error_messages[0])
    size[0] = len(matrix)
    if size[0] == 0:
        raise ValueError(error_messages[1])
    if not all(map(lambda x: isinstance(x, list), matrix)):
        raise TypeError(error_messages[2])
    if all(map(lambda x: len(x) == 0, matrix)):
        raise ValueError(error_messages[1])
    if not all(map(
        lambda x: all(map(
            lambda y: isinstance(y, (int, float)), x)), matrix)):
        raise TypeError(error_messages[3])
    size[1] = len(matrix[0])
    if not all(map(lambda x: len(x) == size[1], matrix)):
        raise TypeError(error_messages[4])
    return size


def matrix_mul(m_a, m_b):
    '''Multiplies 2 matrices.'''
    a = get_matrix_size(m_a, 'm_a')
    b = get_matrix_size(m_b, 'm_b')
    # AB only works iff column_count in A == row_count in B
    if a[1] != b[0]:
        raise ValueError('m_a and m_b can\'t be multiplied')
    else:
        result = []
        for row_a in m_a:
            row_result = []
            for i in range(b[1]):
                value = map(
                        lambda x: x[1] * m_b[x[0]][i],
                        zip(range(a[1]), row_a)
                        )
                row_result.append(sum(list(value)))
            result.append(row_result)
        return result
