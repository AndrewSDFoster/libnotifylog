#!/usr/bin/env python

import glib
import dbus
from dbus.mainloop.glib import DBusGMainLoop

def notifications(bus, message):
    logfile = open("/var/log/libnotify.log", "a")
    notification = list(message.get_args_list())
    output = ""
    for i in [0,3,4]:
        if i < len(notification):
            output += notification[i]+"\t"
    output += "\n"
    logfile.write(str(output))
    logfile.close()

DBusGMainLoop(set_as_default=True)

bus = dbus.SessionBus()
bus.add_match_string_non_blocking("eavesdrop=true, interface='org.freedesktop.Notifications', member='Notify'")
bus.add_message_filter(notifications)

mainloop = glib.MainLoop()
mainloop.run()
