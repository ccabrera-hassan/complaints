import pandas as pd


def parser_date():
       pass

def parser_int():
       pass

def parser_string():
       pass

def generate_ratio():
       pass

# Función para procesar el archivo CSV
def transform_chunk(chunk):
        """ 
        Funcion que se puede utilizar para aplicar distintas tranformaciones al conjunto de datos
        """
        try:  
        
            chunk.rename(columns={
    'Date received': 'date_received',
    'Product': 'product',
    'Sub-product': 'sub_product',
    'Issue': 'issue',
    'Sub-issue': 'sub_issue',
    'Consumer complaint narrative': 'consumer_complaint_narrative',
    'Company public response': 'company_public_response',
    'Company': 'company',
    'State': 'state',
    'ZIP code': 'zip_code',
    'Tags': 'tags',
    'Consumer consent provided?': 'consumer_consent_provided',
    'Submitted via': 'submitted_via',
    'Company response to consumer': 'company_response_to_consumer',
    'Timely response?': 'timely_response',
    'Consumer disputed?': 'consumer_disputed',
    'Complaint ID': 'complaint_id',
    'Date sent to company': 'date_sent_to_company'
}, inplace=True)

            return chunk
        
        except Exception as e:
                e_m = f"Data_Transform:transform_chunk"
                print(f'{e_m} Exeption: {e}')
                
