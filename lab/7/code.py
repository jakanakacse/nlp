def resolve_ambiguity(prev_tag, target_word, probabilities):
    candidate_tags = ["NOUN", "VERB"]
    best_tag = None
    max_score = -1.0

    print(f"{'Tag':<10} {'P(Transition)':<15} {'P(Emission)':<15} {'Total Score':<15}")
    print("-" * 55)

    for tag in candidate_tags:
        p_trans = probabilities["transitions"][prev_tag][tag]
        p_emiss = probabilities["emissions"][tag][target_word]
        score = p_trans * p_emiss
        print(f"{tag:<10} {p_trans:<15.4f} {p_emiss:<15.4f} {score:<15.6f}")

        if score > max_score:
            max_score = score
            best_tag = tag

    return best_tag, max_score

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

print(f"Given Previous Tag: '{prev_tag}' and Word: '{target_word}'\n")
best_tag, score = resolve_ambiguity(prev_tag, target_word, probabilities)
print("-" * 55)
print(f"Disambiguated POS Tag: {best_tag} (Score: {score:.6f})")

