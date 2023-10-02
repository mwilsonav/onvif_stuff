#!/usr/bin/env python3

import argparse
from onvif import ONVIFCamera

def usage():
    parser = argparse.ArgumentParser(description='Connect to an ONVIF camera and get the snapshot URI.')
    parser.add_argument('hostname', help='Hostname or IP address of the camera.')
    parser.add_argument('-p', '--port', default=80, type=int, help='Port number for the camera (default: 80).')
    parser.add_argument('-u', '--username', default='admin', help='Username for the camera (default: admin).')
    parser.add_argument('-w', '--password', default='123456', help='Password for the camera (default: 123456).')
    return parser.parse_args()

def main():
    args = usage()

    mycam = ONVIFCamera(args.hostname, args.port, args.username, args.password)

    media_service = mycam.create_media_service()
    profiles = media_service.GetProfiles()
    token = profiles[0].token

    obj = media_service.create_type('GetSnapshotUri')
    obj.ProfileToken = token
    #obj.StreamSetup = {'Stream': 'RTP-Unicast', 'Transport': {'Protocol': 'RTSP'}}
    print(media_service.GetSnapshotUri(obj))

if __name__ == '__main__':
    main()

