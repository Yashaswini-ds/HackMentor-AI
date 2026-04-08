import json
import re

class HybridScoringEngine:
    def __init__(self):
        pass

    def evaluate(self, idea_text, domain, team_size, timeline_hours, tech_level, llm_evaluation):
        """
        Takes LLM generated scores and applies deterministic rules.
        llm_evaluation is expected to be a dictionary:
        {
            "innovation": {"score": 8, "reasoning": "..."},
            "feasibility": {"score": 6, "reasoning": "..."},
            "impact": {"score": 9, "reasoning": "..."}
        }
        """
        
        # 1. Initialize with LLM Scores
        scores = {
            "innovation": llm_evaluation.get("innovation", {}).get("score", 5),
            "feasibility": llm_evaluation.get("feasibility", {}).get("score", 5),
            "impact": llm_evaluation.get("impact", {}).get("score", 5)
        }
        
        adjustments = []
        idea_lower = idea_text.lower()
        
        # 2. Apply Deterministic Rules
        
        # Rule 1: Hardware/IoT is harder to hack in a short time
        if re.search(r'\b(hardware|iot|raspberry pi|arduino|sensor)\b', idea_lower):
            scores["feasibility"] -= 1
            adjustments.append({"dimension": "feasibility", "adjustment": -1, "reason": "Hardware/IoT components generally reduce feasibility in constrained hackathon timelines."})
            
        # Rule 2: "Existing API" or "No-code" might be less innovative
        if re.search(r'\b(existing api|no-code|nocode|low-code|lowcode|wrapper)\b', idea_lower):
            scores["innovation"] -= 1
            adjustments.append({"dimension": "innovation", "adjustment": -1, "reason": "Heavy reliance on existing APIs/no-code tools slightly reduces the core innovation score."})
            
        # Rule 3: High impact domains
        if re.search(r'\b(health|healthcare|medical|agriculture|farming|education|climate|environment)\b', domain.lower() + " " + idea_lower):
            scores["impact"] += 1
            adjustments.append({"dimension": "impact", "adjustment": +1, "reason": "Tackling critical domains like Health, Agriculture, or Education increases potential impact."})
            
        # Rule 4: Team size constraints
        try:
            team_size_int = int(team_size)
            if team_size_int <= 2:
                scores["feasibility"] -= 1
                adjustments.append({"dimension": "feasibility", "adjustment": -1, "reason": "A small team (≤2) might struggle to deliver a complex solution within the timeframe."})
        except:
            pass
            
        # Rule 5: Timeline constraints
        try:
            timeline_int = int(timeline_hours)
            if timeline_int <= 24:
                scores["feasibility"] -= 1
                adjustments.append({"dimension": "feasibility", "adjustment": -1, "reason": "Very short hackathon timeline (≤24h) decreases feasibility."})
        except:
            pass
            
        # Rule 6: Large user base / scalability
        if re.search(r'\b(mass|millions|global|scale|crowdsource|platform)\b', idea_lower):
            scores["impact"] += 1
            adjustments.append({"dimension": "impact", "adjustment": +1, "reason": "Designing for scale or a large user base increases potential impact."})
            
        # Rule 7: Advanced Tech 
        if re.search(r'\b(ml|ai|machine learning|artificial intelligence|blockchain|web3|llm|generative)\b', idea_lower):
             scores["innovation"] += 1
             adjustments.append({"dimension": "innovation", "adjustment": +1, "reason": "Incorporating advanced technologies (AI/ML/Web3) tends to boost innovation."})
             if tech_level.lower() in ['beginner', 'non-technical']:
                 scores["feasibility"] -= 1
                 adjustments.append({"dimension": "feasibility", "adjustment": -1, "reason": "Advanced tech planned by beginner/non-technical team reduces feasibility."})


        # 3. Clamp scores between 0 and 10 and calculate average
        for k in scores:
            scores[k] = max(0, min(10, scores[k]))
            
        total_score = round(sum(scores.values()) / 3.0, 1)
        
        # 4. Final Verdict
        if total_score >= 8.5:
            verdict = "🏆 Hackathon Winner Potential"
        elif total_score >= 7.0:
            verdict = "🚀 Strong Idea — Refine & Submit"
        elif total_score >= 5.0:
            verdict = "🔧 Needs Work — See Suggestions"
        else:
            verdict = "💡 Pivot Recommended"
            
        return {
            "initial_llm_scores": llm_evaluation,
            "final_scores": scores,
            "adjustments": adjustments,
            "total_score": total_score,
            "verdict": verdict
        }
