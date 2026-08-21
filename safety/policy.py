def authorize(action,human_approved=False):
 c={"deploy_control","change_safety_logic","write_live_controller","bypass_interlock"}
 return human_approved if action in c else True