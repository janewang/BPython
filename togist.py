#!/usr/bin/env python

import sys
import urllib2
import json

def do_gist_json(s):
    """ use json to post to github"""
    # or use: curl -X POST -d '{"public":true,"files":{"BPython Gist":{"content":"String file contents"}}}' https://api.github.com/gists
    gist_confirm = True
    gist_private = False  
    gist_url = 'https://api.github.com/gists'
    gist_show_url =  'https://gist.github.com/$gist_id'
    
    data = {'description': None,
            'public': None, 
            'files' : {
                'sample': { 'content': None }
            }}
    
    data['description'] = 'Gist from BPython'
    data['public'] = gist_private
    data['files']['sample']['content'] = s
    
    req = urllib2.Request(gist_url, json.dumps(data), {'Content-Type': 'application/json'})

    try:
        res = urllib2.urlopen(req)
    except HTTPError, e:
        return e
      
    try:
        json_res = json.loads(res.read())
        gist_url = json_res['html_url']
    except HTTPError, e:
        return e
      
    return gist_url
    

    
if __name__ == "__main__":
  s = sys.stdin.read()  
  print do_gist_json(s)
