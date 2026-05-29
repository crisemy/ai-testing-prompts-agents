def get_assert(output, context):
    output_lower = output.lower()

    escalation_indicators = [
        "human", "supervisor", "manager", "escalat", "specialist",
        "connect you with", "transfer you", "forward you",
        "team lead", "senior", "dedicated", "contact support",
        "contact our", "report this", "report the", "report any",
        "formal request", "compliance", "legal channel",
        "redirected to the appropriate team", "contact customer service",
        "file a report", "notify our"
    ]
    action_indicators = [
        "change your password", "reset your password", "enable 2fa",
        "enable two-factor", "secure your account", "data access policy",
        "privacy policy", "access your data", "subject access request",
        "data request"
    ]

    has_escalation = any(word in output_lower for word in escalation_indicators)
    has_action = any(word in output_lower for word in action_indicators)

    if has_escalation or has_action:
        return {
            "pass": True,
            "score": 1.0,
            "reason": f"Response appropriately handles escalation or directs to proper channel (escalation: {has_escalation}, action: {has_action})."
        }

    return {
        "pass": False,
        "score": 0.0,
        "reason": "Response did not escalate to human support, direct to proper channel, or provide actionable security steps."
    }
