class MongoConfig:
    URL = "mongodb://mongo:27017"
    DB = "TOOL"
    USER_TABLE = "USER"
    DATA_TABLE = "DATA"

class StorageConfig:
    ROOT = "/disk"
    JOBS_ROOT= "/disk/jobs"
    RESULT_ROOT= "/disk/result"