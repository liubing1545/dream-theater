# -*- utf-8 -*-

import qiniu
from flask import current_app

def get_token():
    q = qiniu.Auth(current_app.config['QINIU_ACCESS_KEY'], current_app.config['QINIU_SECRET_KEY'])
    token = q.upload_token(current_app.config['PIC_BUCKET'])
    return token
