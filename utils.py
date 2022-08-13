#!/usr/bin/env python
"""Provides utility functions for processing list of CNF clauses."""
from pysat.formula import CNF


def get_hashcode(C: list) -> str:
    """
    Returns the hashcode of the given CNF formula.
    :param C: a list of clauses
    :return: the hashcode of the given CNF formula
    """
    C = sorted(C, key=lambda x: x[0])
    return str(C)


def diff(x: list, y: list) -> list:
    """
    Returns the difference of two lists.
    :param x: list
    :param y: list
    :return: list
    """
    return [item for item in x if item not in y]


def split(C: list) -> (list, list):
    """
    Splits the given CNF formula into two parts.
    :param C: a list of clauses
    :return: a tuple of two lists
    """
    half_size = len(C) // 2
    return C[:half_size], C[half_size:]


def prepare_cstrs_sets(in_model_filename: str, in_req_filename: str) -> (list, list):
    """
    Prepares the background knowledge B and the possibly faulty constraints C.
    To our evaluation, the background knowledge is only the root constraint.
    The possibly faulty constraints include all the constraints converted from the feature model,
    and the requirement.
    :param in_model_filename: the name of the file containing the feature model (CNF)
    :param in_req_filename: the name of the file containing the requirement (CNF)
    :return: a tuple of two lists:
        - B: the background knowledge
        - C: the possibly faulty constraints
    """
    model_cnf = CNF(from_file=in_model_filename)
    requirements_cnf = CNF(from_file=in_req_filename)

    C_cnf = CNF(from_clauses=model_cnf.clauses[1:])
    C_cnf.extend(requirements_cnf.clauses)

    B_cnf = CNF(from_clauses=model_cnf.clauses[0:1])

    B = sorted(enumerate(B_cnf.clauses, start=0), key=lambda x: x[0])
    C = sorted(enumerate(C_cnf.clauses, start=len(B_cnf.clauses)), key=lambda x: x[0])

    return B, C


def hasIntersection(list1: list, list2: list) -> bool:
    return any(i in list1 for i in list2)


def contains(listofList: list, aList: list) -> bool:
    return any(aList == x for x in listofList)


def containsAll(greater: list, smaller: list) -> bool:
    return all(i in smaller for i in greater)
