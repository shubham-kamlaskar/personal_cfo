def generate_client_id(client_count: int) -> str:
    base_code = "2600"
    sequence = str(client_count + 1).zfill(3)   # 001, 002, 003
    return sequence