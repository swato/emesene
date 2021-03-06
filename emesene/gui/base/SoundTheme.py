'''a module that contains a class that describes a sound theme'''
# -*- coding: utf-8 -*-

#    This file is part of emesene.
#
#    emesene is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 3 of the License, or
#    (at your option) any later version.
#
#    emesene is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with emesene; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

import os

class SoundTheme(object):
    '''a class that contains information of a sound theme
    '''

    def __init__(self, path):
        '''constructor

        get information from the theme located in path
        '''
        self.path           = None
        self.sound_alert    = None
        self.sound_nudge    = None
        self.sound_offline  = None
        self.sound_online   = None
        self.sound_send     = None
        self.sound_type     = None

        self.load_information(path)

    def load_information(self, path):
        '''load the information of the theme on path
        '''
        self.path = path

        self.sound_alert    = os.path.join(self.path, "alert.wav")
        self.sound_nudge    = os.path.join(self.path, "nudge.wav")
        self.sound_offline  = os.path.join(self.path, "offline.wav")
        self.sound_online   = os.path.join(self.path, "online.wav")
        self.sound_send     = os.path.join(self.path, "send.wav")
        self.sound_type     = os.path.join(self.path, "type.wav")

    def get_sound_theme_path(self):
        return self.path
