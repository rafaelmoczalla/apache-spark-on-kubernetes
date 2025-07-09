FROM bitnami/spark

USER root

RUN DEBIAN_FRONTEND=noninteractive apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y python3 python3-pip && \
    pip3 install pyspark && \
    rm -rf /var/lib/apt/lists/*

USER 1001

