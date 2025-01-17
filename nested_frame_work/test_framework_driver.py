
#! /usr/bin/env python

#-------------------------------------------------------------------------------
#
#  IPS wrapper for TEST Driver component.
#
#-------------------------------------------------------------------------------

from component import Component
import subprocess
import os
import sys

#-------------------------------------------------------------------------------
#
#  TEST Driver Class
#
#-------------------------------------------------------------------------------
class test_framework_driver(Component):

#-------------------------------------------------------------------------------
#
#  test_framework_driver Component Constructor
#
#-------------------------------------------------------------------------------
    def __init__(self, services, config):
        print('test_framework_driver: Construct')
        Component.__init__(self, services, config)
        self.running_components = {}
        self.ports = {}

#-------------------------------------------------------------------------------
#
#  test_framework_driver Component init method.
#
#-------------------------------------------------------------------------------
    def init(self, timeStamp=0.0, **keywords):
        print('test_framework_driver: init')

        self.platform_conf = self.services.get_config_param('PLATFORM_FILE')
        self.simulation_conf = self.services.get_config_param('TEST_COMPONENT_CONF')
        self.ips_path = self.services.get_config_param('IPS_PATH')

#-------------------------------------------------------------------------------
#
#  test_framework_driver Component step method.
#
#-------------------------------------------------------------------------------
    def step(self, timeStamp=0.0):
        print('test_framework_driver: step')

        os.environ['PWD'] = os.getcwd()

        if sys.version_info[0] == 3:
            process = subprocess.Popen(['python3', self.ips_path + '/ips.py', '--platform={}'.format(self.platform_conf), '--simulation={}'.format(self.simulation_conf)], env=os.environ)
        else:
            process = subprocess.Popen(['ips.py', '--platform={}'.format(self.platform_conf), '--simulation={}'.format(self.simulation_conf)], env=os.environ)
        process.wait();
    
#-------------------------------------------------------------------------------
#
#  test_framework_driver Component finalize method.
#
#-------------------------------------------------------------------------------
    def finalize(self, timeStamp=0.0):
        print('test_framework_driver: finalize')
