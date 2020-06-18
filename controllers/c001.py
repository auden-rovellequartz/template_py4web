from ..modules.external_imports import *
from ..modules.framework_imports import *
from ..modules.application_imports import *

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
@action("page_one")
@action.uses("c001/page_one.html")
@action.uses(db, session)
def page_one():
	session_vars_manager(db, session)
	home = A(
		"go home",
		_href = URL("index")
		)
	return dict(
		home = home,
		session = session,
		)
