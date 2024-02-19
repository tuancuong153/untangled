import logging

def get_last_row_index(service, spreadsheet_id, sheet_name, range_data = 'A1:Z'):
    try:
        result = service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id,
            range=f'{sheet_name}!{range_data}'
        ).execute()
        
        values = result.get('values', [])
        if not values:
            logging.info('No data')
        else:
            last_row_index = None
            for index, row in enumerate(reversed(values)):
                if any(row):
                    last_row_index = len(values) - index
                    break
            return last_row_index
    except Exception as e:
        logging.error(e)

def update_data(service, spreadsheet_id, sheet_name, data, position_update):
    try:
        cell_to_update = f'{sheet_name}!{position_update}'
        new_values = data
        value_range_body = {
            'values': new_values
        }
        request = service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id,
            range=cell_to_update,
            valueInputOption='RAW',
            body=value_range_body
        )
        response = request.execute()
        logging.info('Finished insert data')
    except Exception as e:
        logging.error(e)

def get_data(service, spreadsheet_id, sheet_name):
    try:
        range_name = f'{sheet_name}'
        result = service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id, range=range_name).execute()
        return result.get('values', [])
    except Exception as e:
        logging.error(e)

def delete_data(service, spreadsheet_id, sheet_name, position_delete):
    try:
        cell_to_update = f'{sheet_name}!{position_delete}'
        request = service.spreadsheets().values().clear(
            spreadsheetId=spreadsheet_id,
            range=cell_to_update,
            body={}
        )
        response = request.execute()
        logging.info('Finished delete data')
    except Exception as e:
        logging.error(e)