#!/bin/python

import requests
import json
import time

def check_quota(api_key,url):
    #Assemble Header
    headers = {"User-Agent": "python-api-wrapper","Authorization": api_key}
    
    #Send request and parse response
    response = requests.get(url+"quota", headers=headers, verify=False)
    response_json = json.loads(response.content)
    print "Threat Emulation Quota Statistics"
    print  "Current Status: " + response_json['response'][0]['action']
    print "\n"
    print "Monthly"
    print "Assigned Quota: " + str(response_json['response'][0]['assigned_quota_month'])
    print "Remaining Quota: " + str(response_json['response'][0]['remain_quota_month'])
    print "\n"
    print "Hourly:"
    print "Assigned Quota: " + str(response_json['response'][0]['assigned_quota_hour'])
    print "Remaining Quota: " + str(response_json['response'][0]['remain_quota_hour'])

    