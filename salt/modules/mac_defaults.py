# -*- coding: utf-8 -*-
'''
Set defaults on Mac OS

'''

# Import python libs
from __future__ import absolute_import
import logging

# Import salt libs
import salt.utils

log = logging.getLogger(__name__)
__virtualname__ = 'macdefaults'


def __virtual__():
    '''
    Only work on Mac OS
    '''
    if salt.utils.is_darwin():
        return __virtualname__
    return False


def write(domain, key, value, type='string', user=None):
    '''
    Write a default to the system

    CLI Example:

    .. code-block:: bash

        salt '*' macdefaults.write com.apple.CrashReporter DialogType Server

        salt '*' macdefaults.write NSGlobalDomain ApplePersistence True type=bool

    domain
        The name of the domain to write to

    key
        The key of the given domain to write to

    value
        The value to write to the given key

    type
        The type of value to be written, vaid types are string, data, int[eger],
        float, bool[ean], date, array, array-add, dict, dict-add

    user
        The user to write the defaults to


    '''
    if type == 'bool' or type == 'boolean':
        if value is True:
            value = 'TRUE'
        elif value is False:
            value = 'FALSE'

    cmd = 'defaults write "{0}" "{1}" -{2} "{3}"'.format(domain, key, type, value)
    return __salt__['cmd.run_all'](cmd, runas=user)


def read(domain, key, user=None):
    '''
    Write a default to the system

    CLI Example:

    .. code-block:: bash

        salt '*' macdefaults.read com.apple.CrashReporter DialogType

        salt '*' macdefaults.read NSGlobalDomain ApplePersistence

    domain
        The name of the domain to read from

    key
        The key of the given domain to read from

    user
        The user to write the defaults to

    '''
    cmd = 'defaults read "{0}" "{1}"'.format(domain, key)
    return __salt__['cmd.run'](cmd, runas=user)