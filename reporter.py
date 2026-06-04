import json

def save_results_to_json(result: dict):
    result = serializer(result)
    result = json.dumps(result)
    

def serializer(result: dict):
    for username, data in result.items():
        data["timestamp"] = data["timestamp"].isoformat()
    return result

