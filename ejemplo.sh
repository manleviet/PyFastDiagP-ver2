#!/bin/bash
#---------------Script SBATCH - NLHPC ----------------
#SBATCH -J FastDiag
#SBATCH -p general
#SBATCH -n 44
#SBATCH --ntasks-per-node=44
#SBATCH -c 1
#SBATCH --mem-per-cpu=4250
#SBATCH --mail-user=vietman.le@ist.tugraz.at
#SBATCH --mail-type=ALL
#SBATCH -o FastDiag_%j.out
#SBATCH -e FastDiag_%j.err

#-----------------Toolchain---------------------------
# ----------------Modulos----------------------------
# ----------------Comando--------------------------
pip install python-sat --no-binary :all: --user
python evaluate_v2.py