"""Definition for the JSON resume schema."""
import schema

SCHEMA = schema.Schema({
    "meta": {
        "theme": str,
    },
    "basics": {
        "name": str,
        "label": str,
        "image": str,
        "email": str,
        "phone": str,
        "url": str,
        "summary": str,
        "location": {
            "city": str,
            "countryCode": str
        },
        schema.Optional("profiles"): list,
    },
    schema.Optional("Skills"): list,
    schema.Optional("work"): list,
    schema.Optional("Certifications"): list,
    schema.Optional("education"): list,
    }, ignore_extra_keys=True)
