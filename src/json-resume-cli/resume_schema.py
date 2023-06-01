"""Definition for the JSON resume schema."""
import schema

SCHEMA = schema.Schema({
    schema.Optional("meta"): {
        schema.Optional("theme"): str,
    },
    schema.Optional("basics"): {
        schema.Optional("name"): str,
        schema.Optional("label"): str,
        schema.Optional("image"): str,
        schema.Optional("email"): str,
        schema.Optional("phone"): str,
        schema.Optional("url"): str,
        schema.Optional("summary"): str,
        schema.Optional("location"): {
            schema.Optional("city"): str,
            schema.Optional("countryCode"): str
        },
        schema.Optional("profiles"): list,
    },
    schema.Optional("skills"): list,
    schema.Optional("work"): list,
    schema.Optional("certificates"): list,
    schema.Optional("education"): list,
    }, ignore_extra_keys=True)
