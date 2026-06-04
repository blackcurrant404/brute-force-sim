import json

def save_results_to_json(result: dict):
    result = serializer(result)
    result_json = json.dumps(result, indent=4, sort_keys=True)
    with open("logs/result.json", "w") as new_file:
        new_file.write(result_json)
    

def serializer(result: dict):
    for username, data in result.items():
        if data["timestamp"] != None:
            data["timestamp"] = data["timestamp"].isoformat()
    return result

