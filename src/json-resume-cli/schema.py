"""Schema related functionality, e.g. samples, validations, etc."""
import json
import yaml
from sample import JSON_SAMPLE

JSON_DEST = "resume.json"
YAML_DEST = "resume.yaml"


class Schema:
    """Schema related functionality, e.g. samples, validations, etc."""
    @staticmethod
    def get_json_sample():
        """Generate a JSON sample resume."""
        json_resume = json.dumps(JSON_SAMPLE, indent=2)

        with open(JSON_DEST, "w", encoding="UTF-8") as file:
            file.write(json_resume)

    @staticmethod
    def get_yaml_sample():
        """Generate a YAML sample resume."""
        yaml_resume = yaml.dump(JSON_SAMPLE, indent=2)

        with open(YAML_DEST, "w", encoding="UTF-8") as file:
            file.write(yaml_resume)
