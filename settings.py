DEBUG = False

PRODUCTION_URL = "https://ebs1rsk4m6.execute-api.us-east-1.amazonaws.com/production"

if DEBUG:
    PRODUCTION_URL = "http://localhost:5000"

# by default, scrape San Francisco
DEFAULT_LOCATION = 44961364

DEFAULT_CURSOR = ""

PAGE_SIZE = 50