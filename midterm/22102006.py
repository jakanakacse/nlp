def resolve_ambiguity(prev_tag, target_word, probabilities):
    candidate_tags = ["NOUN", "VERB"]
    winning_tag = None
    maximum_calculated_score = -1.0

    for tag in candidate_tags:
        p_transition = probabilities["transitions"][prev_tag][tag]
        p_emission = probabilities["emissions"][tag][target_word]
        score = p_transition * p_emission
        print(p_transition, p_emission, score)

        if score > maximum_calculated_score:
            maximum_calculated_score = score
            winning_tag = tag

    return winning_tag, maximum_calculated_score

probabilities = {
    "transitions": {
        "DET": {"NOUN": 0.65, "VERB": 0.01}
    },
    "emissions": {
        "NOUN": {"book": 0.005},
        "VERB": {"book": 0.001}
    }
}

prev_tag = "DET"
target_word = "book"

result = resolve_ambiguity(prev_tag, target_word, probabilities)
print("Result:", result)