#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import requests
import json

def checkin():
    cookie = os.environ.get('GLADOS_COOKIE')
    if not cookie:
        print('Error: GLADOS_COOKIE not found in environment')
        return False
    
    url = 'https://glados.rocks/api/user/checkin'
    headers = {
        'Cookie': cookie,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    data = {'token': 'glados.one'}
    
    try:
        response = requests.post(url, headers=headers, json=data, timeout=30)
        print(f'Status Code: {response.status_code}')
        print(f'Response: {response.text}')
        
        if response.status_code == 200:
            result = response.json()
            if result.get('code') == 0:
                print('✓ Check-in successful!')
                return True
            else:
                print(f'Check-in failed: {result.get("message")}')
                return False
        else:
            print(f'HTTP Error: {response.status_code}')
            return False
    except Exception as e:
        print(f'Error occurred: {str(e)}')
        return False

if __name__ == '__main__':
    success = checkin()
    exit(0 if success else 1)
