"""Fail-closed engineering governance for F118 Factory Automation."""

PROTECTED_ACTIONS = {
    "deploy_control",
    "change_safety_logic",
    "write_live_controller",
    "bypass_interlock",
    "commission_cell",
    "change_plc_logic",
    "change_robot_program",
    "change_operating_setpoint",
}

REQUIRED_REVIEWS = (
    "requirements_reviewed",
    "controls_architecture_reviewed",
    "integration_reviewed",
    "verification_reviewed",
    "functional_safety_reviewed",
    "cybersecurity_reviewed",
    "change_traceability_reviewed",
    "qualified_engineering_approval",
)


def authorize(action: str, context: dict | None = None) -> dict:
    context = context or {}
    if action in PROTECTED_ACTIONS:
        return {"allowed": False, "reason": "operational control authority is outside reference-system scope"}

    missing = [key for key in REQUIRED_REVIEWS if not context.get(key)]
    if missing:
        return {"allowed": False, "reason": "missing required factory-automation review", "missing": missing}

    blockers = []
    if context.get("requirements_gap"):
        blockers.append("automation requirements remain incomplete or inconsistent")
    if context.get("safety_interlock_gap"):
        blockers.append("safety interlock or protective function gap unresolved")
    if context.get("verification_failure"):
        blockers.append("verification or commissioning evidence is incomplete or failed")
    if context.get("live_control_coupling_risk"):
        blockers.append("unsafe coupling to live control is unresolved")
    if context.get("cybersecurity_risk"):
        blockers.append("industrial-control cybersecurity risk unresolved")
    if context.get("unreviewed_logic_change"):
        blockers.append("PLC, robot, HMI, or control-logic change is unreviewed")
    if context.get("traceability_gap"):
        blockers.append("requirements, logic, test, or configuration traceability incomplete")
    if context.get("unsafe_operating_condition"):
        blockers.append("unsafe operating condition or process hazard unresolved")

    if blockers:
        return {"allowed": False, "reason": "factory-automation governance blocker", "blockers": blockers}

    return {"allowed": True, "reason": "factory-automation engineering package approved after qualified human review"}


def review_required(action: str) -> bool:
    return action in PROTECTED_ACTIONS


def enforce(action: str, approved: bool) -> None:
    if review_required(action) and not approved:
        raise PermissionError("Qualified human approval is required for this action.")
