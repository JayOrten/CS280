#!/bin/bash
export AIRFLOW_HOME=/<Your Name>/airflow-cs280
cd /home/mosesof<Your Name>/airflow-cs280
ls
source /home/mosesof<Your Name>/miniconda3/bin/activate
conda activate /home/mosesof<Your Name>/miniconda3/envs/airflow-env
nohup airflow scheduler >> scheduler.log &
nohup airflow webserver -p 8080 >> webserver.log &