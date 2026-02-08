"""
Insecure Deserialization Vulnerability Example
This code demonstrates deserialization vulnerabilities that Snyk can detect.
"""

import pickle
import yaml
import json


def load_user_data(data):
    """
    VULNERABLE: Insecure deserialization with pickle
    """
    # VULNERABILITY: Using pickle.loads on untrusted data
    user_object = pickle.loads(data)
    return user_object


def load_config_from_yaml(yaml_string):
    """
    VULNERABLE: Unsafe YAML loading
    """
    # VULNERABILITY: Using yaml.load without Loader parameter
    config = yaml.load(yaml_string)
    return config


def deserialize_object(serialized_data):
    """
    VULNERABLE: Pickle deserialization from file
    """
    # VULNERABILITY: Unpickling untrusted data
    with open(serialized_data, 'rb') as f:
        obj = pickle.load(f)
    return obj


def load_yaml_file(filepath):
    """
    VULNERABLE: Unsafe YAML loading from file
    """
    # VULNERABILITY: yaml.load without safe loader
    with open(filepath, 'r') as f:
        data = yaml.load(f)
    return data


# Example of SAFE implementation (for comparison)
def load_config_safe(yaml_string):
    """
    SAFE: Using safe YAML loader
    """
    # SAFE: Using yaml.safe_load
    config = yaml.safe_load(yaml_string)
    return config


def load_json_data(json_string):
    """
    SAFE: Using JSON instead of pickle
    """
    # SAFE: JSON is safer for serialization
    data = json.loads(json_string)
    return data
