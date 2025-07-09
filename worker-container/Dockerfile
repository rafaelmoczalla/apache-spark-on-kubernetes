FROM apache/spark

USER root

RUN DEBIAN_FRONTEND=noninteractive apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y python3 python3-pip && \
    pip3 install pyspark && \
    rm -rf /var/lib/apt/lists/*

COPY start-spark.sh /usr/local/bin/start-spark.sh

ENTRYPOINT ["/usr/local/bin/start-spark.sh"]

