#!/usr/bin/env python
"""Implementation of an MSS-based FastDiag algorithm.
MSS - Maximal Satisfiable Subset

// MSS-based FastDiag Algorithm
//--------------------
// B: correctConstraints (background knowledge)
// C: possiblyFaultyConstraints
//--------------------
// Func FastDiag(C, B) : Δ
// if isEmpty(C) or consistent(B U C) return Φ
// else return C \\ FD(Φ, C, B)

// Func FD(Δ, C = {c1..cn}, B) : MSS
// if Δ != Φ and consistent(B U C) return C;
// if singleton(C) return Φ;
// k = n/2;
// C1 = {c1..ck}; C2 = {ck+1..cn};
// Δ1 = FD(C2, C1, B);
// Δ2 = FD(C1 - Δ1, C2, B U Δ1);
// return Δ1 ∪ Δ2;
"""

import sys
import time
import logging

import checker
import utils

solver_path = "solver_apps/choco4solver.jar"


def findDiagnosis(C: list, B: list) -> list:
    """
    Activate FastDiag algorithm if there exists at least one constraint,
    which induces an inconsistency in B. Otherwise, it returns an empty set.

    // Func FastDiag(C, B) : Δ
    // if isEmpty(C) or consistent(B U C) return Φ
    // else return C \\ FD(Φ, C, B)
    :param C: a consideration set of constraints
    :param B: a background knowledge
    :return: a diagnosis or an empty set
    """
    logging.info("fastDiag [C={}, B={}]".format(C, B))

    # if isEmpty(C) or consistent(B U C) return Φ
    if len(C) == 0 or checker.is_consistent(B + C, solver_path)[0]:
        logging.info("return Φ")
        return []
    else:  # return C \ FD(C, B, Φ)
        mss = fd([], C, B)
        diag = utils.diff(C, mss)

        logging.info("return {}".format(diag))
        return diag


def fd(Δ: list, C: list, B: list) -> list:
    """
    The implementation of MSS-based FastDiag algorithm.
    The algorithm determines a maximal satisfiable subset MSS (Γ) of C U B.

    // Func FD(Δ, C = {c1..cn}, B) : MSS
    // if Δ != Φ and consistent(B U C) return C;
    // if singleton(C) return Φ;
    // k = n/2;
    // C1 = {c1..ck}; C2 = {ck+1..cn};
    // Δ1 = FD(C2, C1, B);
    // Δ2 = FD(C1 - Δ1, C2, B U Δ1);
    // return Δ1 ∪ Δ2;
    :param Δ: check to skip redundant consistency checks
    :param C: a consideration set of constraints
    :param B: a background knowledge
    :return: a maximal satisfiable subset MSS of C U B
    """
    logging.debug(">>> FD [Δ={}, C={}, B={}]".format(Δ, C, B))

    # if Δ != Φ and consistent(B U C) return C;
    if len(Δ) != 0 and checker.is_consistent(B + C, solver_path)[0]:
        logging.debug("<<< return {}".format(C))
        return C

    # if singleton(C) return Φ;
    if len(C) == 1:
        logging.debug("<<< return Φ")
        return []

    # C1 = {c1..ck}; C2 = {ck+1..cn};
    C1, C2 = utils.split(C)

    # Δ1 = FD(C2, C1, B);
    Δ1 = fd(C2, C1, B)
    # Δ2 = FD(C1 - Δ1, C2, B U Δ1);
    C1withoutΔ1 = utils.diff(C1, Δ1)
    Δ2 = fd(C1withoutΔ1, C2, B + Δ1)

    logging.debug("<<< return [Δ1={} ∪ Δ2={}]".format(Δ1, Δ2))

    # return Δ1 + Δ2
    return Δ1 + Δ2


def main():
    global solver_path

    if len(sys.argv) > 1:
        in_model_filename = sys.argv[1]
        in_req_filename = sys.argv[2]
        solver_path = sys.argv[3]

    else:  # Default values
        in_model_filename = "./data/tests/test_model.cnf"
        in_req_filename = "./data/tests/test_prod_1.cnf"
        solver_path = "solver_apps/org.sat4j.core.jar"

    B, C = utils.prepare_cstrs_sets(in_model_filename, in_req_filename)

    start_time = time.time()
    diag = findDiagnosis(C, B)
    total_time = time.time() - start_time

    print(in_req_filename + "|" + str(total_time) + "|" + str(checker.counter_CC)
          + "|" + str(0) + "|" + str(0)
          + "|" + str(0) + "|fastdiag|" + solver_path + "|" + str(diag))


if __name__ == '__main__':
    main()
