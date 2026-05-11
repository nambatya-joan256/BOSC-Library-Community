def calculate_signal_strength(distance, power):
    # This was fixed in Issue #1
    return power / (distance ** 2) 

def get_protocol_info(protocol):
    # This is being fixed in Issue #2
    protocols = {
        "WiFi": "802.11ax",
        "LoRa": "Low Power Wide Area",
        "5G": "3GPP Release 16"  # We added this line!
    }
    return protocols.get(protocol, "Unknown Protocol")