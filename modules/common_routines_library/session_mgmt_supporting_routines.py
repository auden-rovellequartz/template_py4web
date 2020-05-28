from ...modules.external_imports import *
from ...modules.framework_imports import *
from ...modules.app_constants import *

def logout(session):
	session.clear()
	return ()
def session_vars_manager(db, session):
	page = request.path.lstrip("/")
	if (not session.get("page")):
		session["page"] = None
	if (not session.get("previous_page")):
		session["previous_page"] = None
	session["previous_page"] = session.get("page")
	session["page"] = page
	return ()






