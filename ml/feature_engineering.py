def generate_features(user, scheme):
    """
    Generate feature values for eligibility scoring.
    """
    features = {}

    features["income_match"] = int(
        scheme["min_income"] <= user["income"] <= scheme["max_income"]
    )

    features["state_match"] = int(
        scheme["state"] == "ALL" or scheme["state"] == user["state"]
    )

    features["category_match"] = int(
        scheme["category"] == user["category"]
    )

    features["age_match"] = int(
        scheme["min_age"] <= user["age"] <= scheme["max_age"]
    )

    return features
