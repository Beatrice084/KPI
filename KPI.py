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

    def get_landing_page(self, platform='gccollab'):
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
                      "pageSize": 3,
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
