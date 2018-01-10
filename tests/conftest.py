# -*- coding: utf-8 -*-

import os
import pytest
import shutil

@pytest.fixture(autouse=True)
def ignore_app_ini(request):
    settings_file = 'phinisid/phinisidApp.ini'
    backup_file = 'phinisid/_phinisidApp.ini'

    if os.path.exists(settings_file):
        app_ini_found = True
        shutil.copy(settings_file, backup_file)
        os.remove(settings_file)
    else:
        app_ini_found = False

    def restore_app_ini():
        if app_ini_found and os.path.exists(backup_file):
            shutil.copy(backup_file, settings_file)
            os.remove(backup_file)

    request.addfinalizer(restore_app_ini)


@pytest.fixture(scope="session")
def app(request):
    """Uses the InteractiveLauncher to provide access to an app instance.

    The finalizer stops the launcher once the tests are finished.

    Returns:
      :class:`phinisidApp`: App instance
    """
    from kivy.interactive import InteractiveLauncher
    from phinisid.phinisid import phinisidApp
    launcher = InteractiveLauncher(phinisidApp('en'))

    def stop_launcher():
        launcher.safeOut()
        launcher.stop()

    request.addfinalizer(stop_launcher)

    launcher.run()
    launcher.safeIn()
    return launcher.app
