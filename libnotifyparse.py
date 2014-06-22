#!/usr/bin/env python

import glib
import dbus
from dbus.mainloop.glib import DBusGMainLoop

def notifications(bus, message):
    notification = [arg for arg in message.get_args_list()]
    output = ""
    for i in [0,3,4]:
        for j in notification[i:i+1:1]:
            output += j+"\t"
    print output

DBusGMainLoop(set_as_default=True)

bus = dbus.SessionBus()
bus.add_match_string_non_blocking("eavesdrop=true, interface='org.freedesktop.Notifications', member='Notify'")
bus.add_message_filter(notifications)

mainloop = glib.MainLoop()
mainloop.run()
