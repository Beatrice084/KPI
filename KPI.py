# For authorizing the google analytics API session
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import os

import pandas as pd
import numpy as np


class KPI:
    """ Object for interacting with the Analytics API """

    def __init__(self):
        # Initialize the API object
        self.analytics = self._initialize_API_()

    def _initialize_API_(self):
        print("initializing google analytics api with proper credentials")
        # If the API key has not yet been turned into a file, do that now
        credentials = {}
        if os.path.isfile('client_secrets.json') == False:
            # Create the file from the env
            with open('client_secrets.json', 'w') as f:
                f.write(os.environ['GA-CLIENT-SECRETS'])

        """ Initialize the Analytics API object """
        _SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
        _KEY_FILE_LOCATION = 'client_secrets.json'
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            _KEY_FILE_LOCATION, _SCOPES)

        ServiceAccountCredentials.from_json
        # Build the service object.
        return build('analyticsreporting', 'v4', credentials=credentials)

    def get_id(self, platform):
        ids = {
            'gccollab': '127642570',
            'gcconnex': '55943097',
            'gcpedia': '39673253',
            'aurora': '181987687'
        }
        return ids[platform]

    def get_sessions_by_country(self, platform='gccollab'):
        return self.analytics.reports().batchGet(
            body={
                'reportRequests': [
                    {
                        'viewId': self.get_id(platform),
                        'dateRanges': [{'startDate': '7daysAgo', 'endDate': 'today'}],
                        'metrics': [{'expression': 'ga:sessions'}],
                        'dimensions': [{'name': 'ga:country'}]
                    }]
            }
        ).execute()

    '''     
    Returns the bounce rate for the given platform. The platfrom can
    be either 'gccollab', 'gcconnex', or 'gcpedia'. If not givem a platform
    gccollab is assumed.    

    (String)->(dict)     

    Example:
    get_bounce_rate('gcpedia')->{'reports': [{'columnHeader': {'metricHeader':
    {'metricHeaderEntries': [{'name': 'ga:bounceRate', 'type': 'PERCENT'}]}},
    'data': {'rows': [{'metrics': [{'values': ['51.54448944379209']}]}], 'totals':
    [{'values': ['51.54448944379209']}], 'rowCount': 1, 'minimums': [{'values':
    ['51.54448944379209']}], 'maximums': [{'values': ['51.54448944379209']}]}}]}
    '''
    def get_bounce_rate(self, platform='gccollab'):
        return self.analytics.reports().batchGet(
            body={
                'reportRequests': [
                    {
                        'viewId': self.get_id(platform),
                        'dateRanges': [{'startDate': '7daysAgo', 'endDate': 'today'}],
                        'metrics': [{'expression': 'ga:bounceRate'}]
                    }]
            }
        ).execute()

    '''     
    Returns the average time of page  for the given platform. The platfrom can
    be either 'gccollab', 'gcconnex', or 'gcpedia'. If not givem a platform
    gccollab is assumed.    

    (String)->(dict)     
    
    Example: 
    get_avg_time_on_page()->{'reports': [{'columnHeader':
    {'metricHeader': {'metricHeaderEntries': [{'name': 'ga:avgTimeOnPage',
    'type': 'TIME'}]}}, 'data': {'rows': [{'metrics': [{'values':
    ['251.72985570597024']}]}], 'totals': [{'values':
    ['251.72985570597024']}], 'rowCount': 1, 'minimums': [{'values':
    ['251.72985570597024']}], 'maximums': [{'values':
    ['251.72985570597024']}]}}]} 
    ''' 
    def get_avg_time_on_page(self, platform='gccollab'):
        return self.analytics.reports().batchGet(
            body={
                'reportRequests': [
                    {
                        'viewId': self.get_id(platform),
                        'dateRanges': [{'startDate': '7daysAgo', 'endDate': 'today'}],
                        'metrics': [{'expression': 'ga:avgTimeOnPage'}]
                    }]
            }
        ).execute()

    '''     
    Returns the unique page views for the given platform. The platfrom can
    be either 'gccollab', 'gcconnex', or 'gcpedia'. If not givem a platform
    gccollab is assumed.    

    (String)->(dict)     
    
    Example:  
    get_unique_views()->{'reports': [{'columnHeader':
    {'metricHeader': {'metricHeaderEntries': [{'name': 'ga:uniquePageviews',
    'type': 'INTEGER'}]}}, 'data': {'rows': [{'metrics': [{'values':
    ['33985']}]}], 'totals': [{'values': ['33985']}], 'rowCount': 1,
    'minimums': [{'values': ['33985']}], 'maximums': [{'values':
    ['33985']}]}}]} 
    '''
    def get_unique_views(self, platform='gccollab'):
        return self.analytics.reports().batchGet(
            body={
                'reportRequests': [
                    {
                        'viewId': self.get_id(platform),
                        'dateRanges': [{'startDate': '7daysAgo', 'endDate': 'today'}],
                        'metrics': [{'expression': 'ga:uniquePageviews'}]
                    }]
            }
        ).execute()

    '''     
    Returns the pageviews per session for the given platform. The platfrom can
    be either 'gccollab', 'gcconnex', or 'gcpedia'. If not givem a platform
    gccollab is assumed.    

    (String)->(dict)     
    
    Example:   
    get_page_views_per_session()->{'reports': [{'columnHeader':
    {'metricHeader': {'metricHeaderEntries': [{'name':
    'ga:pageviewsPerSession', 'type': 'FLOAT'}]}}, 'data': {'rows':
    [{'metrics': [{'values': ['6.995852842809365']}]}], 'totals': [{'values':
    ['6.995852842809365']}], 'rowCount': 1, 'minimums': [{'values':
    ['6.995852842809365']}], 'maximums': [{'values':
    ['6.995852842809365']}]}}]} '''
    def get_page_views_per_session(self, platform='gccollab'):
        return self.analytics.reports().batchGet(
            body={
                'reportRequests': [
                    {
                        'viewId': self.get_id(platform),
                        'dateRanges': [{'startDate': '7daysAgo', 'endDate': 'today'}],
                        'metrics': [{'expression': 'ga:pageviewsPerSession'}]
                    }]
            }
        ).execute()

    '''     
    Returns the top landing page for the given platform. The platfrom can
    be either 'gccollab', 'gcconnex', or 'gcpedia'. If not givem a platform
    gccollab is assumed.  

    (String)->(dict)     
    
    Example: 
    get_top_landing_page()->{'reports': [{'columnHeader':
    {'dimensions': ['ga:LandingPagePath'], 'metricHeader':
    {'metricHeaderEntries': [{'name': 'ga:entrances', 'type': 'INTEGER'},
    {'name': 'ga:bounceRate', 'type': 'PERCENT'}]}}, 'data': {'rows':
    [{'dimensions': ['/splash/'], 'metrics': [{'values': ['12611',
    '49.48854174926651']}]}, {'dimensions': ['/newsfeed/'], 'metrics':
    [{'values': ['4821', '3.671437461107654']}]}, {'dimensions':
    ['/missions/main'], 'metrics': [{'values': ['594',
    '6.228956228956229']}]}], 'totals': [{'values': ['30918',
    '24.272970274709348']}], 'rowCount': 2954, 'minimums': [{'values': ['0',
    '0.0']}], 'maximums': [{'values': ['12611', '100.0']}]}, 'nextPageToken':
    '3'}]} '''
    def get_top_landing_page(self, platform='gccollab'):
        return self.analytics.reports().batchGet(
            body={
                'reportRequests': [
                    {
                        "viewId": self.get_id(platform),
                        "dateRanges": [
                            {
                                "startDate": "30daysAgo",
                                "endDate": "yesterday"
                            }
                        ],
                        "metrics": [
                            {
                                "expression": "ga:entrances"
                            },
                            {
                                "expression": "ga:bounceRate"
                            }
                        ],
                        "dimensions": [
                            {
                                "name": "ga:LandingPagePath"
                            }
                        ],
                        "pageSize": 3,  # change this to increase number of pages returned
                        "orderBys": [
                            {
                                "fieldName": "ga:entrances",
                                "sortOrder": "DESCENDING"
                            }
                        ]
                    }
                ]
            }
        ).execute()

    '''     
    Returns the top exit page for the given platform. The platfrom can
    be either 'gccollab', 'gcconnex', or 'gcpedia'. If not givem a platform
    gccollab is assumed.  

    (String)->(dict)     
    
    Example: 
    get_top_exit_page()->{'reports': [{'columnHeader':
    {'dimensions': ['ga:exitPagePath'], 'metricHeader':
    {'metricHeaderEntries': [{'name': 'ga:exits', 'type': 'INTEGER'}, {'name':
    'ga:pageviews', 'type': 'INTEGER'}]}}, 'data': {'rows': [{'dimensions':
    ['/splash/'], 'metrics': [{'values': ['7103', '9706']}]}, {'dimensions':
    ['/newsfeed/'], 'metrics': [{'values': ['2241', '10244']}]},
    {'dimensions': ['/missions/main'], 'metrics': [{'values': ['690',
    '6399']}]}], 'totals': [{'values': ['30918', '227694']}], 'rowCount':
    6807, 'minimums': [{'values': ['0', '0']}], 'maximums': [{'values':
    ['7103', '10244']}]}, 'nextPageToken': '3'}]}'''
    def get_top_exit_page(self, platform='gccollab'):
        return self.analytics.reports().batchGet(
            body={
                'reportRequests': [
                    {
                        "viewId": self.get_id(platform),
                        "dateRanges": [
                            {
                                "startDate": "30daysAgo",
                                "endDate": "yesterday"
                            }
                        ],
                        "metrics": [
                            {
                                "expression": "ga:exits"
                            },
                            {
                                "expression": "ga:pageviews"
                            }
                        ],
                        "dimensions": [
                            {
                                "name": "ga:exitPagePath"
                            }
                        ],
                        "pageSize": 3,  # change this to increase number of pages returned
                        "orderBys": [
                            {
                                "fieldName": "ga:exits",
                                "sortOrder": "DESCENDING"
                            }
                        ]
                    }
                ]
            }
        ).execute()
