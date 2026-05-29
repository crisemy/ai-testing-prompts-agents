def get_assert(output, context):
    words = output.split()
    word_count = len(words)

    if word_count > 100:
        return {
            "pass": False,
            "score": 0.0,
            "reason": f"Response is too long ({word_count} words). It should be more concise."
        }

    return {
        "pass": True,
        "score": 1.0,
        "reason": f"Response is concise ({word_count} words)."
    }
