from orchestration.orchestrator import orchestrate


def base():
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


SCENARIOS = [
    ({}, False),
    (base(), True),
    ({**base(), "qualified_engineering_approval": False}, False),
    ({**base(), "requirements_gap": True}, False),
    ({**base(), "safety_interlock_gap": True}, False),
    ({**base(), "verification_failure": True}, False),
    ({**base(), "live_control_coupling_risk": True}, False),
    ({**base(), "cybersecurity_risk": True}, False),
    ({**base(), "unreviewed_logic_change": True}, False),
    ({**base(), "traceability_gap": True}, False),
]


def main():
    passed = 0
    for context, expected in SCENARIOS:
        passed += orchestrate(context)["release_allowed"] is expected
    print(f"held-out: {passed}/{len(SCENARIOS)} passed")
    raise SystemExit(0 if passed == len(SCENARIOS) else 1)


if __name__ == "__main__":
    main()
