from ..modules.external_imports import *
from ..modules.framework_imports import *
from ..modules.application_imports import *

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
