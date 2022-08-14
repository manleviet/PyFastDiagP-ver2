#!/bin/python3
# import logging.config
import os
import time

# logging.config.fileConfig('logging.conf')

cards = ["16"]  # "1", "2", "4", "8",
# lmaxs = ["0"]  # , "1", "2", "3", "4", "5"]
cores = ["32"]  # , "4", "6", "8"
numScenarios = 2

solver_path = "solver_apps/org.sat4j.core.jar"

start_time = time.time()
modelPath = "./data/linux/linux.cnf"
for card in cards:
    for i in range(numScenarios):
        reqPath = "./data/linux/prod_{}_{}.cnf".format(card, i + 1)

        print(
            "python3 ./fastdiag.py " + modelPath + " " + reqPath + " " + solver_path)
        os.system(
            "python3 ./fastdiag.py " + modelPath + " " + reqPath + " " + solver_path + " >>" + " resultFastDiag.csv")

        for core in cores:
            # print(
            #     "python3 ./fastdiagp_v1_1.py " + modelPath + " " + reqPath + " " + solver_path + " " + core)
            # os.system(
            #     "python3 ./fastdiagp_v1_1.py " + modelPath + " " + reqPath + " " + solver_path + " " + core + " >>" + " resultFastDiagPV1_1.csv")

            # print(
            #     "python3 ./fastdiagp_v2_1.py " + modelPath + " " + reqPath + " " + solver_path + " " + core)
            # os.system(
            #     "python3 ./fastdiagp_v2_1.py " + modelPath + " " + reqPath + " " + solver_path + " " + core + " >>" + " resultFastDiagPV2_1.csv")

            # print(
            #     "python3 ./fastdiagp_v3_1.py " + modelPath + " " + reqPath + " " + solver_path + " " + core)
            # os.system(
            #     "python3 ./fastdiagp_v3_1.py " + modelPath + " " + reqPath + " " + solver_path + " " + core + " >>" + " resultFastDiagPV3_1.csv")

            print(
                "python3 ./fastdiagp_v4_1.py " + modelPath + " " + reqPath + " " + solver_path + " " + core)
            os.system(
                "python3 ./fastdiagp_v4_1.py " + modelPath + " " + reqPath + " " + solver_path + " " + core + " >>" + " resultFastDiagPV4_1.csv")

total_time = time.time() - start_time
print("Sat4j time: " + str(total_time))
