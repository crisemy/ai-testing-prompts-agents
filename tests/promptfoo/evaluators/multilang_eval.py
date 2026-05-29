def get_assert(output, context):
    words = output.split()
    word_count = len(words)

    if word_count == 0:
        return {"pass": False, "score": 0.0, "reason": "Empty response."}

    if word_count > 100:
        return {"pass": False, "score": 0.5, "reason": f"Response too long ({word_count} words)."}

    output_lower = output.lower()

    eng_phrases = [
        "i'm sorry", "i apologize", "as an ai", "i understand",
        "please refer to our return policy", "please refer to our",
        "unplug the power source", "plug it back in",
        "wait 30 seconds", "contact our support",
        "i'm here to help"
    ]
    eng_count = sum(1 for p in eng_phrases if p in output_lower)

    non_eng_indicators = [
        "¿", "á", "é", "í", "ó", "ú", "ñ", "ü",  # Spanish
        "à", "â", "ç", "è", "é", "ê", "ë", "î", "ï", "ô", "û", "ù",  # French
        "ä", "ö", "ü", "ß",  # German
        "ã", "õ", "ç"  # Portuguese
    ]
    non_eng_count = sum(1 for c in non_eng_indicators if c in output)

    # If response has non-English characters but also many English phrases -> language mixing
    if non_eng_count > 0 and eng_count >= 2:
        return {
            "pass": False,
            "score": 0.4,
            "reason": f"Response mixes English phrases ({eng_count} detected) with target language — should be entirely in the user's language."
        }

    # If response has NO non-English characters at all for non-English query -> full English fallback
    if non_eng_count == 0 and eng_count >= 1:
        return {
            "pass": False,
            "score": 0.0,
            "reason": "Response appears to be entirely in English — must respond in the user's language."
        }

    return {"pass": True, "score": 1.0, "reason": f"Response is in expected language and concise ({word_count} words)."}
