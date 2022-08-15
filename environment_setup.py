"""
Determine and configure the hardware and software environment.

This module contains the following functions:

    number_of_available_logical_cores

        Determine the number of available logical cores.

    number_of_available_logical_cores_for_batch_processing

        Configure the number of logical cores to be used for batch processing.
"""


import os


#
# To Do
#
#   Perform a thorough analysis to determine number of
#           logical cores reserved for interactive processing.
#
#   Number of cores reserved for interactive processig should be
#   stored in a .ini file.
#
LOGICAL_CORES_RESERVED_FOR_INTERACTIVE_PROCESSING = 2


def number_of_available_logical_cores():
    """
    Determine the number of available logical cores.
    """

    if hasattr(os, "sched_getaffinity"):
        logical_core_count = len(os.sched_getaffinity(0))
    else:
        logical_core_count = os.cpu_count()

    #
    # To Do: Add a warning entry to the log file when os.cpu_count returns None.

    return logical_core_count


def number_of_available_logical_cores_for_batch_processing():
    """
    Determine the number of available logical cores for batch processing.

    Regardless of situation, we will always allocate at least 1 logical core for batch processing.
    """

    available_logical_core_count = number_of_available_logical_cores()

    if available_logical_core_count is None:

        # To Do: Place a warning in log file that available_batch_logical_core_count
        #           has a value of None.

        available_batch_logical_core_count = 1

    else:

        available_batch_logical_core_count = (
            available_logical_core_count
            - LOGICAL_CORES_RESERVED_FOR_INTERACTIVE_PROCESSING
        )

        if available_batch_logical_core_count <= 0:

            # To Do: Place a warning in log file that the computed value
            #           available_batch_logical_core_count was less than
            #           or equal to zero.

            available_batch_logical_core_count = 1

    return available_batch_logical_core_count


if __name__ == "__main__":

    print("Nmber of available logical cores: ", number_of_available_logical_cores())

    print(
        "Nmber of available logical cores assgined to batch processing: ",
        number_of_available_logical_cores_for_batch_processing(),
    )
