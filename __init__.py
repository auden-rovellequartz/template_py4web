# check compatibility
import py4web
from .modules.framework_imports import *
from .modules.application_imports import *

assert py4web.check_compatible("0.1.20190709.1")

# by importing db you expose it to the _dashboard/dbadmin
from .models import db
from .common import *

# by importing controllers you expose the actions defined in it
from .controllers import c001
from .controllers import c002


