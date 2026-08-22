from orchestration.orchestrator import orchestrate
from safety.policy import authorize


def valid_context():
    return {
        "requirements_reviewed": True,
        "controls_architecture_reviewed": True,
        "integration_reviewed": True,
        "verification_reviewed": True,
        "functional_safety_reviewed": True,
        "cybersecurity_reviewed": True,
        "change_traceability_reviewed": True,
        "qualified_engineering_approval": True,
    }


def test_complete_review_can_release_engineering_package():
    result = orchestrate(valid_context())
    assert result["release_allowed"] is True
    assert result["autonomous_live_control_authority"] is False


def test_missing_engineering_approval_fails_closed():
    context = valid_context()
    context["qualified_engineering_approval"] = False
    assert orchestrate(context)["release_allowed"] is False


def test_live_controller_write_is_never_autonomous():
    assert authorize("write_live_controller", valid_context())["allowed"] is False


def test_safety_interlock_gap_blocks_release():
    context = valid_context()
    context["safety_interlock_gap"] = True
    assert orchestrate(context)["release_allowed"] is False


def test_verification_failure_blocks_release():
    context = valid_context()
    context["verification_failure"] = True
    assert orchestrate(context)["release_allowed"] is False


def test_cybersecurity_risk_blocks_release():
    context = valid_context()
    context["cybersecurity_risk"] = True
    assert orchestrate(context)["release_allowed"] is False


def test_unreviewed_logic_change_blocks_release():
    context = valid_context()
    context["unreviewed_logic_change"] = True
    assert orchestrate(context)["release_allowed"] is False


def test_traceability_gap_blocks_release():
    context = valid_context()
    context["traceability_gap"] = True
    assert orchestrate(context)["release_allowed"] is False
