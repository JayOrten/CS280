#!/bin/bash
export AIRFLOW_HOME=/home/<your username here>/airflow-cs280
cd /home/<your username here>/airflow-cs280
ls
source /home/<your username here>/miniconda3/bin/activate
conda activate /home/<your username here>/miniconda3/envs/airflow-env
export GOOGLE_APPLICATION_CREDENTIALS="/home/<your username here>/airflow-cs280/auth/bucket_auth.json"
nohup airflow scheduler >> scheduler.log &
nohup airflow webserver -p 8080 >> webserver.log &
