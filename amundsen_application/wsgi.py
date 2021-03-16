# Copyright Contributors to the Amundsen project.
# SPDX-License-Identifier: Apache-2.0

import os
from amundsen_application import create_app
from amundsen_application.middleware import PrefixMiddleware

application = create_app(
    config_module_class=os.getenv('FRONTEND_SVC_CONFIG_MODULE_CLASS') or 'amundsen_application.config.LocalConfig')

if __name__ == '__main__':
    application.wsgi_app = PrefixMiddleware(application.wsgi_app, prefix=os.getenv('BASE_URL'))
    application.run(host='0.0.0.0')
