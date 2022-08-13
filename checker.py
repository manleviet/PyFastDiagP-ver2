#!/usr/bin/env python
import logging
import os
import tempfile
import time

from pysat.formula import CNF

counter_CC = 0


def is_consistent(C: list, solver_path: str) -> (bool, float):
    """
    Check if the given CNF formula is consistent using Choco Solver.
    :param solver_path: the path to the Choco Solver jar file
    :param C: a list of clauses
    :return: a tuple of two values:
        - a boolean value indicating whether the given CNF formula is consistent
        - the time taken to check the consistency
    """
    global counter_CC

    with tempfile.NamedTemporaryFile() as f:  # Create a temporary file for the CNF formula
        cnf = CNF()
        for clause in C:
            cnf.append(clause[1])
        cnf.to_file(f.name)  # Write the CNF formula to the temporary file

        start_time = time.time()
        with os.popen("java -jar " + solver_path + " " + f.name) as p:
            counter_CC = counter_CC + 1
            out = p.read()

        total_time = time.time() - start_time

    consistent = "UNSATISFIABLE" not in out
    logging.debug(">>> is_consistent [consistent={}, C={}]".format(consistent, C))
    return consistent, total_time
