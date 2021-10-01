import logging

#RECURSIVE
# Create a custom logger
recursive_logger = logging.getLogger("RECURSIVE")
detection_logger = logging.getLogger("DETECTION")
classification_logger = logging.getLogger("CLASSIFICATION")
auxilar_logger = logging.getLogger("AUXILIAR")


# Create handlers
l_handler = logging.FileHandler(filename='logs.log', mode='a')
s_handler = logging.StreamHandler()
format = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
# logging.basicConfig(filename='example.log', filemode='w', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
l_handler.setFormatter(format)
s_handler.setFormatter(format)

# Add handlers to the logger
recursive_logger.addHandler(l_handler)
recursive_logger.addHandler(s_handler)

detection_logger.addHandler(l_handler)
detection_logger.addHandler(s_handler)

classification_logger.addHandler(l_handler)
classification_logger.addHandler(s_handler)

auxilar_logger.addHandler(l_handler)
auxilar_logger.addHandler(s_handler)

# recursive_logger.addHandler(s_handler)