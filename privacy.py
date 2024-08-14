import hashlib

def anonymize_user_id(user_id):
    return hashlib.sha256(user_id.encode()).hexdigest()

def secure_log_storage(log_data):
    # Example of encrypting logs (simple hash for illustration, should use proper encryption in practice)
    return hashlib.sha256(log_data.encode()).hexdigest()

def store_secure_log(user_id, activity):
    anonymized_id = anonymize_user_id(user_id)
    secure_log = secure_log_storage(activity)
    log_activity(anonymized_id, secure_log)
