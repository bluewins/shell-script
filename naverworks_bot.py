#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
import time, jwt, requests, json
#### Config ####
client_id = '' 
client_secret = ''
service_account = ''
private_key = '' 
bot_id = ''
channel_id = ''
#################
def getAccessToken():
    secret = private_key
    iat = time.time()
    exp = iat + 3600
    payload = {
                'iss': client_id,
                'sub': service_account,
                'iat': iat,
                'exp': exp
            }
    jwt_options = {
            'verify_signature': False,
             'verify_aud': False,
             }
    signed_jwt = jwt.encode(payload, secret, algorithm='RS256')
    token_url = 'https://auth.worksmobile.com/oauth2/v2.0/token'
    token_h = {
            'Content-Type':'application/x-www-form-urlencoded' 
        }
    toekn_p = {
            'grant_type':'urn:ietf:params:oauth:grant-type:jwt-bearer',
            'client_id': client_id,
            'client_secret': client_secret,
            'assertion':signed_jwt,
            'scope':'bot'
            }
    token_r = requests.post(token_url, headers=token_h, params=toekn_p)
    if token_r.status_code != 200:
        print("Response Code : " + str(token_r.status_code) + "\n" + token_r.text)
    a = json.dumps(token_r.json()["access_token"])
    a = a.replace("\"", "")
    return(a)

def sandMessage():
    auth_token = getAccessToken()
    msg_url = 'https://www.worksapis.com/v1.0/bots/'+ bot_id + '/channels/' + channel_id + '/messages'
    msg_h = {
            'Content-Type':'application/json; charset=UTF-8' ,
            'Authorization':'Bearer ' + auth_token,
        }
    msg_d = {
    "content": { 
        "type": "text", 
        "text": "Hello. World" 
  	 }	 
    }
    send = requests.post(msg_url, headers=msg_h, json=msg_d)
    print(send)

sandMessage()
