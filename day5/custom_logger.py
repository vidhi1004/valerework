import logging

logger = logging.getLogger(__name__)

logger.setLevel(level=logging.INFO)

handler = logging.FileHandler("test.log")

formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(message)s")

handler.setFormatter(formatter)

logger.addHandler(handler)

logger.info("testing custom logger")

logger = logging.getLogger("my_custom_logger")

handler = logging.FileHandler("test1.log")



logger.setLevel(level=logging.DEBUG)

formatter = logging.Formatter("%(levelname)s: %(message)s")

handler.setFormatter(formatter)

logger.addHandler(handler)

logger.error("testing custom logger")
