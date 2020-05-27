#!/usr/bin/env python3
import dbus
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib
import os
import traceback

WOBPIPE = os.getenv("WOBPIPE")

def signal_handler(signal):
  print('BrightnessChanged dbus signal received with value:', signal)
  fifo = open(WOBPIPE, 'w')
  fifo.write('{}\n'.format(signal*50))

def main():
  DBusGMainLoop(set_as_default=True)
  bus = dbus.SystemBus()

  try:
    object = bus.get_object('org.freedesktop.UPower', '/org/freedesktop/UPower/KbdBacklight')
    object.connect_to_signal('BrightnessChanged', signal_handler, dbus_interface='org.freedesktop.UPower.KbdBacklight')
  except dbus.DBusException:
    traceback.print_exc()
    sys.exit(1)
  
  loop = GLib.MainLoop()
  loop.run()

if __name__ == '__main__':
  main()
