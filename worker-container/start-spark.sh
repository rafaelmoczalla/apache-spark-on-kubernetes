if [ "$SPARK_MODE" = "master" ]; then
    spark-class org.apache.spark.deploy.master.Master --host spark-master
else if [ "$SPARK_MODE" = "worker" ]; then
    spark-class org.apache.spark.deploy.worker.Worker $SPARK_MASTER_URL --memory $SPARK_WORKER_MEMORY --cores $SPARK_WORKER_CORES
fi

