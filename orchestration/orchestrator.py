from AGENTS.controls_architecture_agent import run as controls_architecture
from AGENTS.integration_agent import run as integration
from AGENTS.requirements_agent import run as requirements
from AGENTS.safety_agent import run as safety
from AGENTS.verification_agent import run as verification
from safety.policy import authorize


def orchestrate(context: dict) -> dict:
    """Run factory-automation specialists and apply fail-closed engineering governance."""
    results = [
        requirements(context),
        controls_architecture(context),
        integration(context),
        verification(context),
        safety(context),
    ]
    governance = authorize("factory_automation_release", context)
    return {
        "system": "F118",
        "results": results,
        "governance": governance,
        "release_allowed": governance["allowed"],
        "human_engineering_review_required": True,
        "autonomous_live_control_authority": False,
        "autonomous_safety_logic_authority": False,
    }
