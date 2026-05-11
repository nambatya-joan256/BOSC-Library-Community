def calculate_signal_strength(distance, power):
    # BUG: This should be power / (distance ** 2) but it's currently addition
    'return power / (distance ** 2)' 

def get_protocol_info(protocol):
    protocols = {
        "WiFi": "802.11ax",
        "LoRa": "Low Power Wide Area"
    }
    return protocols.get(protocol, "Unknown Protocol")