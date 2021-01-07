from page_objects import PageElement, PageObject  #引入库


# howdoi python logging -n8
# https://stackoverflow.com/questions/63782454/python-logging-from-multiple-package-hierarchies-without-using-root-logger
import logging

# setup logging output for this module
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(logging.Formatter("APP ONE: %(message)s"))
logger = logging.getLogger(__name__)
#logger.setLevel(logging.INFO)
logger.addHandler(stream_handler)

# add handler other modules / packages
pkg_logger = logging.getLogger('lib_package')
pkg_logger.addHandler(stream_handler)
#pkg_logger.setLevel(logging.INFO)
del pkg_logger

logger.warning("hello from app_one_main")


# https://stackoverflow.com/questions/7370801/how-to-measure-elapsed-time-in-python
import time

start = time.time()
print("hello")
end = time.time()
print(end - start)

