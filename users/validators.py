def validate_password(value):
    """Validate password"""
    if value:
        if len(value) > 4:
            return value
    return False
