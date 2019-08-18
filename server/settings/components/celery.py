# -*- coding: utf-8 -*-
import djcelery

djcelery.setup_loader()

BROKER_URL = "redis://redis:6379/0"
