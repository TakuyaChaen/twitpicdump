#!/usr/bin/env python
#    Copyright (C) 2018  Takuya Chaen
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import urllib.request
import re
import sys

class TwitPic():

    get_url = "https://twitter.com/#username#/media?count="
    headers = { "User-Agent" :  "Mozilla/4.0" }

    def get_image_url(self,username,number):
        media_url = self.get_url.replace("#username#",username)
        media_url = media_url + number
        req = urllib.request.Request(media_url, None, self.headers)
        response = urllib.request.urlopen(req)
        get_data = response.read().decode('utf-8')
        get_regex = 'data-aria-label-part\ src\=\"(.+\.(jpg|png))'
        url_list = re.findall(get_regex,str(get_data))
        return url_list

if __name__ == '__main__':
    args = sys.argv
    if len(args) > 2:
        get_user = args[1]
        number  = args[2]
        twitpic = TwitPic()
        all_url = twitpic.get_image_url(get_user,number)
        for fetched_url in all_url:
            print(fetched_url[0])
    else:
        print("usage: python3 twitpicudmp.py user_name max_num")
        print("   ex: python3 twitpicudmp.py user_name 10 > user_url.txt")
