# -*- coding: utf-8 -*-

from ncclient import manager

Host = ''
User = 'admin'
Password = ''

with manager.connect(host=Host, port=830, username=User, hostkey_verify=False, device_params={'name':'csr'}) as m:
    c = m.get_config(source='running').data_xml
    with open("%s.xml" % Host, 'w') as f:
        f.write(c)
