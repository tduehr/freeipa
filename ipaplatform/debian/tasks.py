#
# Copyright (C) 2017  FreeIPA Contributors see COPYING for license
#

"""
This module contains default Debian-specific implementations of system tasks.
"""

from ipaplatform.base.tasks import BaseTaskNamespace
from ipaplatform.redhat.tasks import RedHatTaskNamespace


class DebianTaskNamespace(RedHatTaskNamespace):
    @staticmethod
    def restore_pre_ipa_client_configuration(fstore, statestore,
                                             was_sssd_installed,
                                             was_sssd_configured):
        # Debian doesn't use authconfig, nothing to restore
        return True

    @staticmethod
    def set_nisdomain(nisdomain):
        # Debian doesn't use authconfig, nothing to set
        return True

    @staticmethod
    def modify_nsswitch_pam_stack(sssd, mkhomedir, statestore):
        # Debian doesn't use authconfig, this is handled by pam-auth-update
        return True

    @staticmethod
    def modify_pam_to_use_krb5(statestore):
        # Debian doesn't use authconfig, this is handled by pam-auth-update
        return True

    @staticmethod
    def backup_auth_configuration(path):
        # Debian doesn't use authconfig, nothing to backup
        return True

    @staticmethod
    def restore_auth_configuration(path):
        # Debian doesn't use authconfig, nothing to restore
        return True

    @staticmethod
    def parse_ipa_version(version):
        return BaseTaskNamespace.parse_ipa_version(version)

tasks = DebianTaskNamespace()
