from .eligibility_engine import calculate_eligibility_score

def recommend_schemes(user, schemes):
    """
    Generate ranked scheme recommendations for a user.
    """
    recommendations = []

    for _, scheme in schemes.iterrows():
        score, explanation = calculate_eligibility_score(user, scheme)

        if score >= 50:
            recommendations.append({
                "scheme_name": scheme["scheme_name"],
                "score": score,
                "reason": explanation
            })

    recommendations.sort(key=lambda x: x["score"], reverse=True)
    return recommendations
