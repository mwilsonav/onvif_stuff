#!/usr/bin/env python3

from onvif import ONVIFCamera

mycam = ONVIFCamera('192.168.2.11', 80, 'admin', '123456')

media_service = mycam.create_media_service()
profiles = media_service.GetProfiles()
token = profiles[0].token

obj = media_service.create_type('GetStreamUri')
obj.ProfileToken = token
obj.StreamSetup = {'Stream': 'RTP-Unicast', 'Transport': {'Protocol': 'RTSP'}}
print(media_service.GetStreamUri(obj))
