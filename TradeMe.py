from requests_oauthlib import OAuth1Session
from datetime import datetime
'''
4F4CD97D22E4867B9346D12344D86F81
A7630C27A7C75C544C366E1202C8428D
95580253737B7282468767972A0E4AD5
62603E38A04EDB9B6762C3058A0C6ED3
'''##
time = datetime.strptime('1970-01-01 13:00:00',"%Y-%m-%d %H:%M:%S")
oauth_callback = 'https://www.website-tm-access.co.nz/trademe-callback'
oauth_consumer_key = '4F4CD97D22E4867B9346D12344D86F81'
oauth_version= '1.0'
oauth_timestamp= str(int((datetime.now()-time).total_seconds()))    # calculate time in second
oauth_nonce= '7O3kEe'
oauth_signature_method= 'PLAINTEXT'
oauth_signature= 'A7630C27A7C75C544C366E1202C8428D%26'

