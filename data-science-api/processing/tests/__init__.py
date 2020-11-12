import os
import shutil
import subprocess
import warnings
import logging

from api.app import app
from api.v0_1.logging import logger
from pyspark.sql import SparkSession, HiveContext
from fastapi.testclient import TestClient


class PySparkUnittestBase:
    """
    Base class for all unittests in this project
    """

    @classmethod
    def suppress_py4j_logging(cls):
        logger = logging.getLogger("py4j")
        logger.setLevel(logging.ERROR)

    @classmethod
    def setup_class(cls):
        def get_spark_test():
            return get_spark(test=True)

        cls.suppress_py4j_logging()
        warnings.filterwarnings(
            action="ignore", message="unclosed", category=ResourceWarning
        )
        warnings.filterwarnings(
            action="ignore", message="still running", category=ResourceWarning
        )

        # Overwrite default Spark connection to obtain local pyspark for testing
        app.dependency_overrides[get_spark] = get_spark_test
        cls.client = TestClient(app)

        # cls.spark = get_spark_test()
