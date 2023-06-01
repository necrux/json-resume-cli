"""Resume related functionality, e.g. samples, validations, etc."""
import json
import sys
from os import path
import schema
import yaml
from resume_sample import JSON_SAMPLE
from resume_schema import SCHEMA

JSON = "resume.json"
YAML = "resume.yaml"


class Resume:
    """Resume related functionality, e.g. samples, validations, etc."""

    def get_json_sample(self) -> None:
        """Generate a JSON sample resume."""
        json_resume = json.dumps(JSON_SAMPLE, indent=2)

        if self.overwrite_confirmation(JSON):
            with open(JSON, "w", encoding="UTF-8") as file:
                file.write(json_resume)
            print(f"Resume sample created: {JSON}")

    def get_yaml_sample(self) -> None:
        """Generate a YAML sample resume."""
        yaml_resume = yaml.dump(JSON_SAMPLE, indent=2)

        if self.overwrite_confirmation(YAML):
            with open(YAML, "w", encoding="UTF-8") as file:
                file.write(yaml_resume)
            print(f"Resume sample created: {YAML}")

    @staticmethod
    def overwrite_confirmation(file: str) -> bool:
        """Confirm whether to overwrite a file."""
        if path.isfile(file):
            print(f"File already exists: {file}")
            answer = input("Do you want to overwrite this file? y/N ").lower()
            if answer != "y":
                return False
        return True

    @staticmethod
    def validate_schema(file: str) -> None:
        """Validate the schema of the provided file."""
        print(f"Validating schema: {file}")

        try:
            with open(file, encoding='UTF-8') as file_contents:
                content = yaml.safe_load(file_contents)
        except FileNotFoundError:
            print(f"File not found: {file}")
            sys.exit(1)

        try:
            SCHEMA.validate(content)
        except schema.SchemaError as schema_error:
            for error in schema_error.errors:
                if error:
                    print(error)
            for error in schema_error.autos:
                if error:
                    print(error)
