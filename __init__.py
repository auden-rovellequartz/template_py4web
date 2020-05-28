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

@action("index")
@action.uses("default/index.html")
@action.uses(db, session)
def index():
	session_vars_manager(db, session)
	page_001 = A(
		"go to page one",
		_href = URL("page_one")
		)
	page_002 = A(
		"go to page two",
		_href = URL("page_two")
		)
	return dict(
		session = session,
		page_001 = page_001,
		page_002 = page_002,
		)




