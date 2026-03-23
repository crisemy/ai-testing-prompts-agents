def get_assert(output, context):
    words = output.split()
    word_count = len(words)
    
    # Tech support should be concise and direct. Let's say under 100 words.
    if word_count > 100:
        return {
            "pass": False,
            "score": 0.0,
            "reason": f"Response is too long ({word_count} words). It should be more concise."
        }
        
    # Check for direct instruction
    output_lower = output.lower()
    if "unplug" not in output_lower and "disconnect" not in output_lower:
        return {
            "pass": False,
            "score": 0.5,
            "reason": "Missing expected direct instructions (e.g. 'unplug' or 'disconnect')."
        }
        
    return {
        "pass": True,
        "score": 1.0,
        "reason": f"Response is concise ({word_count} words) and explicitly direct."
    }
