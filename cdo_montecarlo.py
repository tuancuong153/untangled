import sys
sys.path.append('..')
import logging
from lib.utils import read_config
# Google API
from lib.storage.authen import login as ggsheet_login
from lib.storage import utils as ggsheet_utils

def pipeline():
    config = read_config('config/cdo.yaml')
    # get data google sheet
    service = ggsheet_login(config['service_account_file'])
    loan_data = ggsheet_utils.get_data(service=service, spreadsheet_id=config['google_sheet']['id'], sheet_name='Data Input')
